# a = int(input())
# b = int(input())
# c = str(input())
# d = int(input())
# e = str(input())
# f = int(input())
# g = str(input())

# cl = list(map(int, c.split()))
# el = list(map(int, e.split()))
# gl = list(map(int, g.split()))

# print('#1' + ' ' + str(max(cl) - min(cl)))
# print('#2' + ' ' + str(max(el) - min(el)))
# print('#3' + ' ' + str(max(gl) - min(gl)))

N = int(input())

for case in range(1, N + 1):
    k = int(input())
    kl = list(map(int, str(input()).split()))
    ans = max(kl) - min(kl)
    print(f'#{case} {ans}')