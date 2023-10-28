import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')



def showTime():
    x1 = [10, 100, 500, 1000, 5000, 25000, 50000]
    y1 = [0.0003, 0.0015, 1.39, 2.81, 11.58, 51.83, 99.40]
    
    x2 = [10, 100, 500, 1000, 5000, 25000, 50000]
    y2 = [0.0004, 0.0016, 1.42,  2.85,  11.16, 50.68, 99.39]
    
    plt.plot(x1, y1, marker='o', linestyle='-', color='b', label='3-куча')
    plt.plot(x2, y2, marker='o', linestyle='-', color='g', label='15-куча')
    plt.title('Зависимость времени выполнения от параметра')
    plt.xlabel('Количество вершин и ребер')
    plt.ylabel('Время выполнения (сек)')
    plt.legend()
    plt.grid(True)
    plt.show()
