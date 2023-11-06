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
    # third_test()
    # fourth_test_b()
    # dijkstra1()
    # dijkstra2()

    csv_file_path = 'res_1a.csv'

    algorithm_name = 'Дейкстра'
    plot_graph_vertex(csv_file_path, algorithm_name)
    csv_file_path = 'res_1b.csv'

    algorithm_name = 'Дейкстра'
    plot_graph_vertex(csv_file_path, algorithm_name)
    csv_file_path = 'res_2a.csv'

    algorithm_name = 'Дейкстра'
    plot_graph_vertex(csv_file_path, algorithm_name)
    csv_file_path = 'res_2b.csv'

    algorithm_name = 'Дейкстра'
    plot_graph_vertex(csv_file_path, algorithm_name)

    csv_file_path = 'res_3.csv'

    algorithm_name = 'Дейкстра'
    plot_graph_edges(csv_file_path, algorithm_name)
    csv_file_path = 'res_4a.csv'

    algorithm_name = 'Дейкстра'
    plot_graph_weight(csv_file_path, algorithm_name)
    csv_file_path = 'res_4b.csv'

    algorithm_name = 'Дейкстра'
    plot_graph_weight(csv_file_path, algorithm_name)

    # # Настраиваем внешний вид графика
    # plt.figure(figsize=(8, 6))  # Размеры графика
    # plt.plot(data['x'], data['y'], color='blue', linewidth=2, marker='o', markersize=5)  # Цвет, толщина и маркер линии
    # plt.xlabel('X-Label')  # Подпись оси X
    # plt.ylabel('Y-Label')  # Подпись оси Y
    # plt.title('График')  # Заголовок графика
    # plt.grid(True)  # Отображение сетки на графике
    # plt.legend([algorithm_name], loc='upper left')  # Легенда
    #
    # # Отображаем график
    # plt.show()