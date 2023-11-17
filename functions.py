import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import copysign, fabs, floor, isfinite, modf

def coding(f):
    if not isfinite(f):
        return repr(f)  # inf nan

    sign = '-' * (copysign(1.0, f) < 0)
    frac, fint = modf(fabs(f))  # split on fractional, integer parts
    n, d = frac.as_integer_ratio()  # frac = numerator / denominator
    assert d & (d - 1) == 0  # power of two

    return f'{sign}{floor(fint):b}.{n:0{d.bit_length()-1}b}'

def decoding(x):
    x = x.split('.')
    if random.randint(0, 100) <= 10:
        l = random.randint(2,len(x[1])-1)
        x[1] = x[1][:l-1]+str(1 - int(x[1][l]))+x[1][l+1:]

    r = 0
    for i in range(len(x[0])):
        r = r + int(x[0][len(x[0])-(i+1)])*(2**(i))

    for i in range(len(x[1])):
        r = r + int(x[1][i])*(2**(0-i-1))

    
    return r

# Массив со случайными числами в диапазоне от 0 до 1 (не включая 0)(и чтобы в сумме давали 1)
def r_o():
    o = []

    w1 = random.uniform(0, 1)
    o.append(w1)

    w2 = random.uniform(0, 1-w1)
    o.append(w2)

    w3 = 1-w2-w1
    o.append(w3)

    # w1 = random.uniform(0, 1)
    # w2 = random.uniform(0, 1)
    # w3 = random.uniform(0, 1)

    # o = normalized([w1,w2,w3])

    return o

# Строит диграмму по "приспособлению"
# Принимает на вход "популяцию" "особей" затем ожидаемые доходности
def diagramm(p, o_d):

    # Рассчитывание "приспособления" для каждой "особи"
    prisp = np.dot(p, o_d)

    # a = []
    # # Округлить все числа в списке до двух знаков после запятой
    # for i in range(len(p)):
    #     for j in range(len(p[i])):
    #         p[i][j] = round(p[i][j], 2)

    # # prisp в процентном соотношении
    # for i in range(len(prisp)):
    #     a.append((prisp[i]*100)/sum(prisp))

    # # Создание круговой диаграммы
    # plt.pie(prisp, labels=p, autopct='%1.1f%%', startangle=140)

    # # Заголовок
    # plt.title('Рулетка')

    # # Отображение диаграммы
    # plt.show()

    otbor_w = dict()

    for i in range(len(prisp)):
        otbor_w[prisp[i]] = p[i]

    return otbor_w

def normalized(a):
    s = sum(a)
    b = a
    b[0] = b[0]/s
    b[1] = b[1]/s
    b[2] = b[2]/s

    return b

def printTabel(a, b, c):
    # Создание DataFrame из данных
    a = '['+str(a[0])+'\n'+str(a[1])+'\n'+str(a[2])+']'
    data = {
        'Название': [
            'Самые выгодные весы\n\n', 
            'Максимальное значение приспособления', 
            'Среднее значение приспособления'
        ],
        'Значение': [a, b, c]
    }
    df = pd.DataFrame(data)

    # Рисование таблицы с корректировкой размера и масштаба
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center', edges='closed')

    # Настройка стиля таблицы
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 4)

    # # Для красоты :)
    # soft_blue = "#add8e6"  # Мягкий синий
    # soft_green = "#90ee90"  # Мягкий зеленый
    # cells = table.properties()["celld"]
    # for i in range(len(df)+1):
    #     cells[i, 0].set_facecolor(soft_blue)   # Красим первый столбец в мягкий синий
    #     cells[i, 0].set_text_props(color='black')
    #     cells[i, 1].set_facecolor(soft_green)  # Красим второй столбец в мягкий зеленый
    #     cells[i, 1].set_text_props(color='black')
    plt.show()