N = int(input())

long = 0
my_words = []
for _ in range(N):
    word = input()
    my_words.append(word)
    if len(word) > long: long = len(word)

new_words = [set() for _ in range(long + 1)]

for w in my_words: new_words[len(w)].add(w)

for k in new_words:
    if k :
        k = sorted(list(k))
        for x in k:
            print(x)