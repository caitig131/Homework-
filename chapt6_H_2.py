def is_divisible(x,y):
    """ Test if x is exactly divisible by y """
    return x % y == 0

num1 = 3
num2 = 12

if is_divisible(num1,num2):
    print("yes")
else:
    print("no")