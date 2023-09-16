# task 1
def get_odd(x,y):
    odd_list = [i for i in range(x,y) if i %2 !=0]
    return odd_list
print(get_odd(2,20))

# task 2 
def divided(x, y):
    numbers = [i for i in range(100) if i%x == 0 or i%y == 0]
    return numbers
print(divided(4, 8))

# task 3
