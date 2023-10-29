import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')



def showTime():
    x1 = [10, 100, 500, 1000, 5000, 10000, 25000, 50000, 75000]
    y1 = [0.0003, 0.0015, 1.39, 2.81, 11.58, 20.42, 51.83, 99.40, 150.85]
    
    x2 = [10, 100, 500, 1000, 5000, 10000, 25000, 50000, 75000]
    y2 = [0.0004, 0.0016, 1.42,  2.85,  11.16, 20.70, 50.68, 97.39, 141.21]
    
    plt.plot(x1, y1, marker='o', linestyle='-', color='b', label='3-куча')
    plt.plot(x2, y2, marker='o', linestyle='-', color='g', label='15-куча')
    plt.title('Зависимость времени выполнения от параметра')
    plt.xlabel('Количество вершин и ребер')
    plt.ylabel('Время выполнения (сек)')
    plt.legend()
    plt.grid(True)
    plt.show()
