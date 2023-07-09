l1 = [1,2,3,4,6,7,8,9,10,24,45,67,199,967,35357,4685785]

def insert_sort(lst:list, num:int) -> list:   
    ln = len(lst)
    mid = ln//2
    a = 1
    LN = ln 
    while True:
        if num <=lst[0]:
            lst = [num] + lst[1:]
            return lst
        elif num >= lst[-1]:
            lst.append(num)
            return lst
        elif num == lst[mid] or  (num < lst[mid] and num>= lst[mid-1]):
            lst = lst[:mid] + [num] + lst[mid:]
            return lst
        elif num > lst[mid] and num <= lst[mid+1]:
            lst = lst[:mid+1] +[num] + lst[mid+1:]
            return lst
        elif num < lst[mid]:
            mid -= (LN//2**a)//2
            a += 1
        else:
            mid += (LN//2**a)//2 
            a += 1

nl = insert_sort(l1, 0)
print(nl)
  
    
        
    


  
