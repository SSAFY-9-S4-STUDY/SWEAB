import sys
sys.stdin = open("input_S_11315.txt")

# 이걸 리뷰하시는 분께 감사함을 표하며...

t = int(input())
for tc in range(1, t + 1):
    n = int(input())  # n * n

    checker = [input() for _ in range(n)]
    # 행, 열,
    # 대각선
    # (위 모서리에서 아래로...아래에서부터 5칸의 여유가 있는가)
    # (위 모서리에서 반대방향으로... 옆에서 부터 5칸의 여유가 있는가)
    
    
    def omok(n):
        tmp = ""
        for i in range(n):
            if "ooooo" in "".join(checker[i]):
                return "YES"
            for j in range(n):
                tmp += checker[j][i]
            if "ooooo" in tmp:
                return "YES"
            else: tmp = ""

        for a in range(n - 4):
            for i in range(n):
                if i + a < n:
                    tmp += checker[i + a][i]
            if "ooooo" in tmp:
                return "YES"
            else: tmp = ""

        for a in range(n - 4):    
            for i in range(n):
                if i + a < n:
                    tmp += checker[i][i + a]
            if "ooooo" in tmp:
                return "YES"
            else: tmp = ""

        for a in range(n - 4):
            for i in range(n):
                if i + a < n:
                    tmp += checker[i + a][n - 1 - i]
            if "ooooo" in tmp:
                return "YES"
            else: tmp = ""

        for a in range(n - 4):
            for i in range(n):
                if i + a < n:
                    tmp += checker[i][n - 1 - (i + a)]
            if "ooooo" in tmp:
                return "YES"
            else: tmp = ""
        
        return "NO"
                    
    print(f"#{tc} {omok(n)}")
