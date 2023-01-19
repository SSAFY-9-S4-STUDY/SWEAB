h,m = map(int,input().split())
print((h+((m-45)//60))%24,(m-45)%60)
