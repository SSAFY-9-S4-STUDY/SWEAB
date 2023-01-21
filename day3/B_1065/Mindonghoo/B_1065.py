num = int(input())

def new_num(x):
    new_nums = []
    digits = len(str(x))
    if digits <= 2:
        for i in range(1,x+1) :
            new_nums.append(i)
        return print(len(new_nums))
    elif digits == 3:
        for i in range(1, 100) :
            new_nums.append(i)
        for i in range(100, x+1) :
            for j in range(0, len(str(x))-2) :
                if int(str(i)[j]) - int(str(i)[j+1]) == int(str(i)[j+1]) - int(str(i)[j+2]) :
                    new_nums.append(i)
        return print(len(new_nums))
    elif digits == 4:
        for i in range(1, 100) :
            new_nums.append(i)
        for i in range(100, 1000) :
            if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]) :
                new_nums.append(i)
        for i in range(1000, x+1) : 
            if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]) == int(str(i)[2]) - int(str(i)[3]) :
                new_nums.append(i)
        return print(len(new_nums))

new_num(num)
