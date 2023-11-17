from functions import *

# Массив ожидаемых доходностей
o_d = [6.08, 2.24, 1.97]

def Genetic_algoritm(o_d):
    # Массив "особей" - "популяция"
    p = []
    m = 3
    k = 0
    l = 0
    m_array = []
    sr_array = []

    # Предварительное заполнение популяции
    for i in range(4):
            p.append(r_o())

    while True:
        # Заполнение "популяции" пятью "особями"
        for i in range(6):
            p.append(r_o())


        # Отбор наиболее "приспособленных" "особей"
        otbor_all = diagramm(p, o_d)
        otbor = []
        for key, value in otbor_all.items():
            otbor.append(key)
        otbor = sorted(otbor)
        otbor = otbor[(len(otbor)//2):]
        
        print('\nМассив отборочных \"приспособлений\"')
        print(otbor)


        # Массив весов
        otbor_w = []
        for key, value in otbor_all.items():
            for i in range(len(otbor)):
                if otbor[i]==key:
                    otbor_w.append(value)

        print('\nМассив весов по отборочным')
        print(otbor_w)

        sr = sum(otbor)/len(otbor)
        sr_array.append(sr)
        m_array.append(m)
        if (m - max(otbor)) < 0.01:
            k+=1
            if k == 50:
                x = []
                y = m_array
                for i in range(len(m_array)):
                    x.append(i)
                plt.plot(x, y)
                plt.title('Рост приспособления')
                plt.xlabel('Итерация')
                plt.ylabel('Максимальное приспособление')
                plt.show()
                y = sr_array
                plt.plot(x, y)
                plt.title('Среднее приспособление')
                plt.xlabel('Итерация')
                plt.ylabel('Средние значения')
                plt.show()
                break
        else:
            k = 0
        print('\nОтклонение от предыдущего максимального приспосбления '+str(m - max(otbor)))
        m = max(otbor)
        

        # Кодирование
        print('\nКодирование')
        otbor_c = []
        for i in otbor_w:
            a = []
            for j in i:
                a.append(coding(j))
            otbor_c.append(a)

        print(otbor_c)

        # Скрещивание
        print('\nСкрещивание')
        otbor_sc = []

        for i in range(1, len(otbor_c)):
            a0 = '0'
            b0 = otbor_c[i-1][0].split('.')[1][:(len(otbor_c[i-1][0].split('.')[1])//2-1)] + otbor_c[i][0].split('.')[1][(len(otbor_c[i][0].split('.')[1])//2):]
            a1 = '0'
            b1 = otbor_c[i-1][1].split('.')[1][:(len(otbor_c[i-1][1].split('.')[1])//2-1)] + otbor_c[i][1].split('.')[1][(len(otbor_c[i][1].split('.')[1])//2):]
            a2 = '0'
            b2 = otbor_c[i-1][2].split('.')[1][:(len(otbor_c[i-1][2].split('.')[1])//2-1)] + otbor_c[i][2].split('.')[1][(len(otbor_c[i][2].split('.')[1])//2):]
            ab = [a0+'.'+b0, a1+'.'+b1, a2+'.'+b2]
            otbor_sc.append(ab)

        print(otbor_sc)

        # Декодирование
        print('\nДекодирование')
        otbor_dc = []

        for i in otbor_sc:
            a = []
            for j in i:
                a.append(decoding(j))
            otbor_dc.append(a)

        print(otbor_dc)

        # Нормализация (сумма весов должна быть равна 1)
        print('\nНормализация')
        otbor_norm = []
        for i in range(len(otbor_dc)):
            otbor_norm.append(normalized(otbor_dc[i]))

        print(otbor_norm)
        p = []
        for i in range(len(otbor_norm)):
            p.append(otbor_norm[i])

    printTabel(otbor_all[max(otbor)], max(otbor), sum(sr_array)/len(sr_array))
    return otbor_all[max(otbor)]

Genetic_algoritm(o_d)