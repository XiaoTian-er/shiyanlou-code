for i in range(1,101):
    if i % 7 == 0:
        continue
    else:
        a = i
        c = 0
        while a > 0:
            if a % 10 == 7:
                c += 1
                break
            else:
                a = a // 10


        if c == 0:
            print(i)


