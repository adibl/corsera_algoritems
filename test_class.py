import os
import importlib
import compileall
import subprocess
import re
import resource
from tqdm import tqdm


class Test(object):
    MY_PATH = NotImplemented
    COURSE_PATH = NotImplemented
    FILE_NAME = NotImplemented
    IS_PRINT_OUTPUTS = False
    SEE_STDERR = False
    MAX_VIRTUAL_MEMORY = 512 * 1024 * 1024
    TIME_LIMIT = 5.0
    PERMOTATIONS = 100

    def limit_virtual_memory(self):
        # The tuple below is of the form (soft limit, hard limit). Limit only
        # the soft part so that the limit can be increased later (setting also
        # the hard limit would prevent that).
        # When the limit cannot be changed, setrlimit() raises ValueError.
        resource.setrlimit(resource.RLIMIT_AS,
                           (self.MAX_VIRTUAL_MEMORY, resource.RLIM_INFINITY))

    def run_test(self, data):
        course_result, course_time = self.run_subprocess(
            data, self.path_to_course, self.TIME_LIMIT * 5)
        my_result, my_time = self.run_subprocess(data, self.path_to_me,
                                                 self.TIME_LIMIT)
        if not self.compare_output(my_result, course_result):
            if self.IS_PRINT_OUTPUTS:
                print('my result:' + my_result)
                print('course result:' + course_result)
                print('data:' + data)
            return False, float(course_time), float(my_time)
        elif self.IS_PRINT_OUTPUTS:
            print('my result:' + my_result)
            print('course result:' + course_result)
            print('data:' + data)
            return True, float(course_time), float(my_time)
        return True, float(course_time), float(my_time)

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
        return NotImplemented

    def run_subprocess(self, data, path, time_limit):
        proc = subprocess.Popen(['time', "python", path],
                                stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                preexec_fn=self.limit_virtual_memory,
                                cwd=os.path.dirname(path))
        try:
            stdout, stderr = proc.communicate(bytes(data + '\n', 'ascii'),
                                              timeout=time_limit * 3)
            result = str(stdout, 'utf-8')
            time = re.search(r'\d+\.\d+', str(stderr, 'utf-8')).group()
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

    def main(self):
        if not os.path.isfile(self.MY_PATH + self.FILE_NAME):
            print("file dont exzist:" + self.MY_PATH + self.FILE_NAME)
            return
        if not (self.COURSE_PATH + self.FILE_NAME):
            print("file dont exzist:" + self.COURSE_PATH + self.FILE_NAME)
            return
        self.compile_file(self.MY_PATH)
        self.compile_file(self.COURSE_PATH)

        self.path_to_course = importlib.util.cache_from_source(
            self.COURSE_PATH + self.FILE_NAME)
        self.path_to_me = importlib.util.cache_from_source(self.MY_PATH +
                                                           self.FILE_NAME)
        total_time_test = 0
        total_time_my = 0

        for x in tqdm(range(self.PERMOTATIONS)):
            data = self.data_creator()
            a, time_test, time_my = self.run_test(data)
            total_time_test += time_test
            total_time_my += time_my
            if not a:
                print('BAG')
                break
        print("ME:" + str(total_time_my))
        print("him:" + str(total_time_test))
        print('precentage:' + str(int(total_time_my / total_time_test * 100)) +
              '%')

    def unit_test(self, data):
        real_result, time = self.run_subprocess(data,
                                                self.MY_PATH + self.FILE_NAME, self.TIME_LIMIT)
        return real_result.strip()

    def test_aginst_function(self):
        if not os.path.isfile(self.MY_PATH + self.FILE_NAME):
            print("file dont exzist:" + self.MY_PATH + self.FILE_NAME)
            return
        self.compile_file(self.MY_PATH)
        self.path_to_me = importlib.util.cache_from_source(self.MY_PATH +
                                                           self.FILE_NAME)
        total_time_my = 0
        for x in tqdm(range(self.PERMOTATIONS)):
            data = self.data_creator()
            a, time_test, time_my = self.run_only_me(data)
            total_time_my += time_my
            if not a:
                print('BAG')
                break
        print("ME:" + str(total_time_my))
