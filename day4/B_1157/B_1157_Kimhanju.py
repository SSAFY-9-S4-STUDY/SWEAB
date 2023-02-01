s = list(map(lambda x:x.upper(),input()))
set_word = set(s)

max_num, max_word = 0, ''
for w in set_word:
    cnt = s.count(w)
    if cnt > max_num:
        max_num, max_word = cnt, w
    elif cnt == max_num:
        max_word += w

print('?' if len(max_word) >1 else max_word)
