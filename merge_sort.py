def merge_sort(l1, l2):
    res = []
    i=0
    j=0
    while len(l1)>0 and len(l2)>0:
        if l1[i] < l2[j]:
            res.append(l1.pop(i))
                        
        elif l2[j] < l1[i]:
            res.append(l2.pop(j))
            
        elif l1[i] == l2[j]:           
            res.append(l1.pop(i)) 
            res.append(l2.pop(j))
            
    
    a = l1 if len(l1)>0 else l2
    res += a
    return res

l1 = [1,3,5,7,9]
l2 = [2,4,6,8,9]
print(merge_sort(l1, l2))
        
        