import os
import importlib
import compileall
import subprocess
import re
#import resource
import datetime
from threading import Timer

from timeit import default_timer as timer
from tqdm import tqdm


class Test(object):
    MY_PATH = NotImplemented
    COURSE_PATH = NotImplemented
    IS_PRINT_OUTPUTS = False
    SEE_STDERR = False
    MAX_VIRTUAL_MEMORY = 512 * 1024 * 1024
    TIME_LIMIT = 5.0
    PERMOTATIONS = 100

    def limit_virtual_memory(self):
        pass
        # The tuple below is of the form (soft limit, hard limit). Limit only
        # the soft part so that the limit can be increased later (setting also
        # the hard limit would prevent that).
        # When the limit cannot be changed, setrlimit() raises ValueError.
        # TODO: add memory limit for win
        #resource.setrlimit(resource.RLIMIT_AS,
        #(self.MAX_VIRTUAL_MEMORY, resource.RLIM_INFINITY))

    def run_test(self, data, paths):
        times = []
        results = []
        for path in paths:
            result, time = self.run_subprocess(data, path, self.TIME_LIMIT * 5)
            results.append(result)
            times.append(time)
        if not self.compare_output(results[0], results[1]):
            if self.IS_PRINT_OUTPUTS:
                print('my result:' + results[0])
                print('course result:' + results[1])
                print('data:' + data)
            raise ArithmeticError("dont match")
        return [float(x) for x in times]

    def run_only_me(self, data):
        my_result, my_time = self.run_subprocess(data, self.path_to_me,
                                                 self.TIME_LIMIT)
        if self.IS_PRINT_OUTPUTS:
            print('my result:' + my_result)
            print('data:' + data)
        if self.validate_result(my_result, data):
            return True, float(-1.0), float(my_time)
        else:
            return False, float(-1.0), float(my_time)

    def validate_result(self, result, data):
        raise NotImplemented

    def run_subprocess(self, data, path, time_limit):
        start = timer()
        proc = subprocess.Popen(["python", path],
                                stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                #preexec_fn=self.limit_virtual_memory,
                                cwd=os.path.dirname(path))
        try:
            stdout, stderr = proc.communicate(bytes(data + '\n', 'ascii'),
                                              timeout=time_limit)
            end = timer()
            result = str(stdout, 'utf-8')
            #time = re.search(r'\d+\.\d+', str(stderr, 'utf-8')).group()
            time = end - start
            if float(time) > time_limit:
                print('timeout:' + str(time_limit))
                return '', 0
            elif self.SEE_STDERR:
                print(stderr)
                return result, time
            else:
                return result, time
        except subprocess.TimeoutExpired:
            print('data:' + str(data))
            print('more than {0} seconds'.format(time_limit * 3))

    def data_creator(self):
        raise NotImplementedError

    def compare_output(self, my_result, course_result):
        return my_result.strip() == course_result.strip()

    def compile_file(self, name):
        compileall.compile_dir(name)

    def compile(self, path):
        if not os.path.isfile(path):
            raise Exception("file dont exzist:" + self.MY_PATH)
        self.compile_file(path)
        return importlib.util.cache_from_source(path)

    def test_main(self):
        times = []
        for path in [self.MY_PATH, self.COURSE_PATH]:
            if not os.path.isfile(path):
                raise Exception("file dont exzist:" + self.MY_PATH)
            self.compile_file(path)

            self.compiled_path = importlib.util.cache_from_source(path)
            total_time = 0

        my_total_time = 0
        course_total_time = 0
        for x in tqdm(range(self.PERMOTATIONS)):
            data = self.data_creator()
            my_time, course_time = self.run_test(data, [self.MY_PATH, self.COURSE_PATH])
            my_total_time += my_time
            course_total_time += course_time
        print("ME:" + str(my_total_time / self.PERMOTATIONS))
        print("him:" + str(course_total_time / self.PERMOTATIONS))
        print('precentage:' + str(int(my_total_time / course_total_time * 100)) +
              '%')

    def unit_test(self, data):
        real_result, time = self.run_subprocess(data,
                                                self.MY_PATH,
                                                self.TIME_LIMIT)
        return real_result.strip()

    def test_aginst_function(self):
        if not os.path.isfile(self.MY_PATH):
            raise Exception("file dont exzist:" + self.MY_PATH)
        self.compile_file(self.MY_PATH)
        self.path_to_me = importlib.util.cache_from_source(self.MY_PATH)
        total_time_my = 0
        for x in tqdm(range(self.PERMOTATIONS)):
            data = self.data_creator()
            a, time_test, time_my = self.run_only_me(data)
            total_time_my += time_my
            if not a:
                raise ArithmeticError("result dont match the data")
        print("ME:" + str(total_time_my))
