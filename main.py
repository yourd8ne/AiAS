from tests.test3_15heap import *
from tests.dijkstraTest import *
from tests.showTime import *
import multiprocessing

file_lock = multiprocessing.Lock()


def run_test(test_func):
    with file_lock:
        test_func()


if __name__ == '__main__':



    # processes = [
    #     # multiprocessing.Process(target=run_test, args=(first_test_a,)),
    #     # multiprocessing.Process(target=run_test, args=(first_test_b,)),
    #     # multiprocessing.Process(target=run_test, args=(second_test_a,)),
    #     # multiprocessing.Process(target=run_test, args=(second_test_b,)),
    #     multiprocessing.Process(target=run_test, args=(third_test,)),
    #     multiprocessing.Process(target=run_test, args=(fourth_test_a,)),
    #     multiprocessing.Process(target=run_test, args=(fourth_test_b,))
    # ]
    #
    # for process in processes:
    #     process.start()
    #
    # for process in processes:
    #     process.join()
    # first_test_a()
    # first_test_b()
    # second_test_a()
    # second_test_b()
    # fourth_test_a()
    third_test()
    # fourth_test_b()
    # dijkstra1()
    # dijkstra2()
   
    