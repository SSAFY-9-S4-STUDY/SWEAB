n1 = input()
n2 = input()
multi1 = int(n2[-1]) * int(n1)
multi2 = int(n2[1]) * int(n1)
multi3 = int(n2[0]) * int(n1)
result = multi1 + multi2 * 10 + multi3 * 100
print(multi1, multi2, multi3, result, end = "")