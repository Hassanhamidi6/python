def reverse(l:list):
    r_list=[]
    for i in l:
        pop_item=l.pop()
        r_list.append(pop_item)
    return r_list

print(reverse([1,2,3]))