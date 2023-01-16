N1 = int(input())
N2 = input()
answer = 0
sqr=0

for i in N2[::-1]:
    print(int(i)*N1)
    answer += int(i)*N1*(10**sqr)
    sqr += 1

print(answer)