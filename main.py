from tests.test3_15heap import *
from tests.dijkstraTest import *
from tests.showTime import *
import multiprocessing

file_lock = multiprocessing.Lock()
def run_test(test_func):
    with file_lock:
        test_func()

if __name__ == '__main__':
    
    processes = [
        # multiprocessing.Process(target=run_test, args=(first_test_a,)),
        # multiprocessing.Process(target=run_test, args=(first_test_b,))
        # multiprocessing.Process(target=run_test, args=(second_test_a,)),
        # multiprocessing.Process(target=run_test, args=(second_test_b,))
        # multiprocessing.Process(target=run_test, args=(third_test,))
        # multiprocessing.Process(target=run_test, args=(fourth_test_a,)),
        # multiprocessing.Process(target=run_test, args=(fourth_test_b,))
    ]
    
    for process in processes:
        process.start()
    
    for process in processes:
        process.join()


    # file_path = 'res_1a.csv'
    # parsed_data = parse_csv_file(file_path)

    # algorithm_3_heap = '3-куча'
    # algorithm_15_heap = '15-куча'

    # plot_graph(parsed_data, algorithm_3_heap)
    # plot_graph(parsed_data, algorithm_15_heap)
    # first_test_a()
    # first_test_b()
    # second_test_a()
    # second_test_b()
    third_test()
    # fourth_test_a()
    # fourth_test_b()
    # results_file = "res_1a.txt"
    # data3, data15 = parse_results(results_file)
    # results_file = "D:\\code\\AiAS\\res_1a.txt"
    # plot_results(results_file)







    # fifth_test()
    # sixth_test()
    # seventh_test()
    # eighth_test()
    # ninth_test()
    # tenth_test()
    # eleventh_test()
    # twelfth_test()
    # thirteenth_test()
    # fourteenth_test()
    # test_rand()
    # test_poln(100)
    # showTime()
   
    