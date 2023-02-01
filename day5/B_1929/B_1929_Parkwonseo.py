M, N = map(int, input().split())

def print_prime(small_num, large_num):
    
    for number in range(small_num, large_num + 1):
        if number == 1:
            continue
        
        this_is_Prime = True
        for check in range(2, number):
            if check * check > number:
                break
            else:
                if number % check == 0:
                    this_is_Prime = False
                    break

        if this_is_Prime == True:
            print(number)


print_prime(M, N)

