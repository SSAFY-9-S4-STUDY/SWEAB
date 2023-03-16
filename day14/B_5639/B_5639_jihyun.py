def order(start, end):
    if start > end:
        return

    root = lst[start]
    for i in range(start+1, end+1):
        if root < lst[i]:
            idx = i
            break
    else:
        idx = end + 1

    order(start + 1, idx - 1)
    order(idx, end)
    print(root)


lst = []
while True:
    try:
        lst.append(int(input()))
    except:
        break

order(0, len(lst)-1)