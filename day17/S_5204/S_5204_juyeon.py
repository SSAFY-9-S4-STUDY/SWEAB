# 런타임 에러 집에가서 수정할예정,,,, 


def partial_sort(arr:list):   
    global cnt

    partial_sorted_list = []

    if arr[0] and arr[1] and arr[0][-1] > arr[1][-1]:
        cnt += 1

    while arr:
        arr = list(filter(lambda x : bool(x), arr)) 
        try:
          if len(arr) == 1:
              partial_sorted_list.extend(arr[0]) 
              break 
            
          elif arr[0][0] < arr[1][0]:
              partial_sorted_list.append(arr[0].pop(0))
          elif arr[0][0] > arr[1][0]:
              partial_sorted_list.append(arr[1].pop(0))
          elif arr[0][0] == arr[1][0]:
              partial_sorted_list.append(arr[1].pop(0))            
              partial_sorted_list.append(arr[0].pop(0))
        except:
            pass
    return partial_sorted_list


def merge_sort(lst):
    
    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        return partial_sort([[lst[0]],[lst[1]]])
    else:
        N = len(lst) // 2
        return partial_sort([merge_sort(lst[:N]), merge_sort(lst[N:])])
  


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    cnt = 0
    arr = merge_sort(numbers)

    print(f'#{tc} {arr[N//2]} {cnt}')