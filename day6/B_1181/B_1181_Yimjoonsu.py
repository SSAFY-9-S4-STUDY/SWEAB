N = int(input())
words_lst = []

for test_case in range(1, N+1):
    words_lst.append(input())

words_lst = sorted(set(words_lst))
words_lst.sort(key=lambda x: len(x))

for i in words_lst:
    print(i)
    