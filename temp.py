import random as rd 
def masss(n): #функция с одним входным параметром (количество массивов)
    mainma=[] #главный список 
    ma=[] #подсписки
    voz={} #будущий словарь с ключами-длиной и значениями-списками для четных позиций
    ub={} #будущий словарь с ключами-длиной и значениями-списками для нечетных позиций
    proverochka=[] #список для проверки размеров подсписков
    for i in range(n): #заводим цикл для главного массива
        f=rd.randint(1, n) #генерируем случайное число (длина будущего подсписка)
        while f in proverochka: #если подсписок такого размера уже есть
            f=rd.randint(1, n) #генерируем случайное число снова, пока размерность не перестанет совпадать с уже существующеми длинами подсписков
        proverochka.append(f) #добавляем новую длину в проверочный список
        for j in range(f): #заводим цикл для подсписка 
            m=rd.randint(0, 9)
            ma.append(m) #генерируем числа и помещаем в наш подсписок
        mainma.append(ma) #добавляем очередной подсписок в список
        ma=[]
        for k in range(len(mainma)):#проверяем четность и нечетность индексов главного списка для будущей сортировки
            if k%2!=0:#нечетные позиции добавляем в словарь для сортировки значений по убыванию
                ub[len(mainma[k])]=mainma[k]
            else:#четные - в словарь для сортировки значений по возрастанию
                voz[len(mainma[k])]=mainma[k]
    e=sorted(ub.items(),reverse=False) #сортируем наши словари должным образом
    ee=sorted(voz.items(),reverse=True)
    ee.extend(e) #соединяем в общий массив оба словаря, получается [(длина,[с,п,и,с,о,к]),...]
    good=[]
    foot=[]
    for z in ee: #(длина,[с,п,и,с,о,к]) - item  в списке
        good.append(z[1])#[с,п,и,с,о,к])
        foot.append(z[0])#(длина
    return good,foot


n=int(input('Введите количество желаемых массивов (натуральное число): ')) 
while n<=0:
    n=int(input('Введенное Вами число не является натуральным. Попробуйте еще раз: '))
out=masss(n)
q=int(input('Введите 0 если хотите вывести массив с массивами или введите 1, если хотите вывести массив с длинами массивов: '))
if q==0:
    print(out[0])
elif q==1:
    print(out[1])
else:
    print('Такой команды не существует')
