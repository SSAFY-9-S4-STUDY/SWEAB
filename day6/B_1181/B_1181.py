n = int(input())

word_set = set([input() for _ in range(n)])

word_list=sorted(word_set,key= lambda x:(len(x),x))
print(word_list)
