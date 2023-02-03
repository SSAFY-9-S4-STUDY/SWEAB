
word_dict = {}
N = int(input())

for i in range(N):
    word = input()
    word_dict.update({word: len(word)})
sorted_words = sorted(word_dict.items(), key=lambda x: (x[1], x[0]))
for _ in sorted_words:
    print(_[0])