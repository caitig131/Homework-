list= [0,1,2,3,4,5,6,7,8,9,10] 
def count_odd(list):
    count = 0
    for i in list:
        if i %2 !=0:
            count+= 1
    return count
print(count_odd(list))






def add_even(list):
    count = 0
    for i in list:
        if i %2 == 0:
            count+= 1
    return sum(count)
print(add_even(list))
