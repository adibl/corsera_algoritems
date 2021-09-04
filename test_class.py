import os
import resource
import subprocess

from timeit import default_timer as timer
import tqdm


class Test(object):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    MY_PATH = NotImplemented
    COURSE_PATH = NotImplemented
    IS_PRINT_OUTPUTS = False
    SEE_STDERR = False
    MAX_VIRTUAL_MEMORY = 512 * 1024 * 1024
    TIME_LIMIT = 5.0
    PERMOTATIONS = 100
    IDE=False

    def limit_virtual_memory(self):
        pass
        # The tuple below is of the form (soft limit, hard limit). Limit only
        # the soft part so that the limit can be increased later (setting also
        # the hard limit would prevent that).
        # When the limit cannot be changed, setrlimit() raises ValueError.
        # TODO: add memory limit for win
        resource.setrlimit(resource.RLIMIT_AS,
        (self.MAX_VIRTUAL_MEMORY, resource.RLIM_INFINITY))

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

    def run_subprocess(self, data, path, time_limit):
        start = timer()
        proc = subprocess.Popen(["python3", self.ROOT_DIR + path],
                                stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                preexec_fn=self.limit_virtual_memory,
                                cwd=os.path.dirname(self.ROOT_DIR + path))
        try:
            stdout, stderr = proc.communicate(bytes(data + '\n', 'ascii'),
                                              timeout=time_limit)
            end = timer()
            result = str(stdout, 'utf-8')
            #time = re.search(r'\d+\.\d+', str(stderr, 'utf-8')).group()
            time = end - start
            if float(time) > time_limit:
                print('timeout:' + str(time_limit))
                raise TimeoutError("excede time limit- took{} insted of {}".format(time, time_limit))
            if self.SEE_STDERR:
                print("STDERR:" + str(stderr))
            return result, time
        except subprocess.TimeoutExpired:
            raise TimeoutError('more than {0} seconds'.format(time_limit))

    def data_creator(self):
        raise NotImplementedError

    def compare_output(self, my_result, course_result):
        return my_result.strip() == course_result.strip()

    def test_main(self):
        for path in [self.MY_PATH, self.COURSE_PATH]:
            if not os.path.isfile(self.ROOT_DIR + path):
                raise Exception("file dont exzist:" + self.ROOT_DIR + path)

        my_total_time = 0
        course_total_time = 0
        if self.IDE:
            func = tqdm.gui.tqdm
        else:
            func = tqdm.tqdm
        for _ in func(range(self.PERMOTATIONS)):
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

