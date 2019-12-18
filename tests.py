import os
import subprocess
import random
import re
import resource
from tqdm import tqdm

class Test(object):
    MY_PATH = NotImplemented
    COURSE_PATH = NotImplemented
    FILE_NAME = NotImplemented
    MAX_VIRTUAL_MEMORY = 512 *1024 *1024
    TIME_LIMIT = 5.0
    PERMOTATIONS = 100

    def limit_virtual_memory(self):
        # The tuple below is of the form (soft limit, hard limit). Limit only
        # the soft part so that the limit can be increased later (setting also
        # the hard limit would prevent that).
        # When the limit cannot be changed, setrlimit() raises ValueError.
        resource.setrlimit(resource.RLIMIT_AS, (self.MAX_VIRTUAL_MEMORY, resource.RLIM_INFINITY))


    def test(self, data):
        course_result, course_time = self.run_test(data, self.COURSE_PATH, self.FILE_NAME)
        my_result, my_time = self.run_test(data, self.MY_PATH, self.FILE_NAME)
        if my_result != course_result:
            print('my result:' + my_result)
            print('course result:' + course_result)
            print('data:' + data)
            return False, float(course_time), float(my_time)
        return True, float(course_time), float(my_time)

    def run_test(self, data, path, filename):
        proc = subprocess.Popen(['time', "python", path + filename], stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                              stderr=subprocess.PIPE, preexec_fn=self.limit_virtual_memory)
        try:
            stdout, stderr = proc.communicate(bytes(data + '\n', 'ascii'), timeout=self.TIME_LIMIT)
            result = str(stdout)
            time = re.search(r'\d+\.\d+', str(stderr)).group()
            return result, time

        except subprocess.TimeoutExpired:
            proc.terminate()
            print('timeout')
            return '', 0


    def data_creator(self):
        raise NotImplemented

    def main(self):
        total_time_test = 0
        total_time_my = 0
        for x in tqdm(range(self.PERMOTATIONS)):
            data = self.data_creator()
            a, time_test, time_my = self.test(data)
            total_time_test += time_test
            total_time_my += time_my
            if not a:
                print('BAG')
                break
        print("ME:" + str(total_time_my))
        print("him:" + str(total_time_test))
        print('precentage:' + str(int(total_time_my/total_time_test*100)) + '%')