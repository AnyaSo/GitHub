import random
zagad_ch=[]
while len(zagad_ch)!=4:
    rand = random.randint(0,9)
    if rand not in zagad_ch:
        zagad_ch.append(rand)
print("Число загадано!")

vved_ch=[]
spis=[]
n=0
while True:
    n = n + 1
    print("Попытка № ",n)
    ch = input("Введите 4х-значное число: ")

    for i in ch:
        spis.append(i)

    if ch == 'prompt':
        print(zagad_ch)
        vved_ch.clear()
        continue

    if len(ch) != 4:
        print("Должно быть 4х-значное число!")
        spis.clear()
        vved_ch.clear()
        continue

    if spis[0]==spis[1]or spis[0]==spis[2]or spis[0]==spis[3]or spis[1]==spis[2]or spis[1]==spis[3]or spis[2]==spis[3]:
        print("Цифры в числе не должны повторяться!")
        spis.clear()
        continue

    for i in ch:
        i=int(i)
        if i not in vved_ch:
            vved_ch.append(i)

    bull = 0
    for i in range(4):
        if zagad_ch[i] == vved_ch[i]:
            bull = bull + 1

    if bull == 4:
        print("Вы угадали число!")
        break

    cow = 0
    for i in range(4):
        for j in range(4):
            if vved_ch[i] == zagad_ch[j]:
                cow = cow + 1

    print("Быков: ",bull)
    print("Коров: ",cow)
    vved_ch.clear()
    spis.clear()
        
