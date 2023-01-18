org_number = int(input())
number = org_number
trial = 0

while True:
    next_number = number // 10 + number % 10
    new_number = number % 10 * 10 + next_number % 10
    trial = trial + 1
    if org_number == new_number :
        print(trial)
        break
    else :
        number = new_number
