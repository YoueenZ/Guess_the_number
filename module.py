import random
def seperate_int(number):   
    x = [int(a) for a in str(number)]
    return x
def return_element(a):
    x = a[0]
    return x
def create_random_num(a,b):
    x = int(random.randrange(a, b))
    return x
