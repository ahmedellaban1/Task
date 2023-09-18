Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

# task 1
def normal_list(items):
    blank_list = []
    for i in items:
        blank_list.append(i.upper())
    return blank_list
print(normal_list(Names))

def list_comprehension(items):
    return [i.upper() for i in items]
print(list_comprehension(Names))

functional_programming = list(map(str.upper, Names))
print(functional_programming)

# task 2
def contains_a(items):
    blank_list = []
    for i in items:
        if 'a' in i:
            blank_list.append(i)
    return blank_list
print(contains_a(Names))


def list_comprehension_2(items):
    return [i for i in items if 'a' in i]
print(list_comprehension_2(Names))

def check_contains_a(word):
    if 'a' in word:
        return word

functional_programming_2 = list(filter(check_contains_a, Names))
print(functional_programming_2)

# task 3
def start_t(items):
    blank_list = []
    for i in items:
        if i[0] == 't':
            blank_list.append(i)
        continue
    return blank_list
print(start_t(Names))


def list_comprehension_3(items):
    return [i for i in items if i[0] == 't']
print(list_comprehension_3(Names))

def check_start_t(word):
    if word[0] == 't':
        return word

functional_programming_3 = list(filter(check_start_t, Names))
print(functional_programming_3)

# task 4
def contains_2a(items):
    blank_list = []
    for i in items:
        if i.count('a') >= 2:
            blank_list.append(i)
    return blank_list
print(contains_2a(Names))


def list_comprehension_4(items):
    return [i for i in items if i.count('a') >= 2]
print(list_comprehension_4(Names))

def check_contains_2a(word):
    if word.count('a') >= 2:
        return word

functional_programming_4 = list(filter(check_contains_2a, Names))
print(functional_programming_4)

# task 5
def task_5(items):
    len_list = []
    for i in items:
        len_list.append(len(i))
    return len_list
print(task_5(Names))


def list_comprehension_5(items):
    return [len(i) for i in items]
print(list_comprehension_5(Names))

functional_programming_5 = list(map(len, Names)) 
print(functional_programming_5)

# task 6
# print(Names.clear()) 

# task 7
a, *b = Names
print(f"""
a = {a}
b = {b}
""")

# task 8
a, *_, b= Names
print(f"""
a = Names[0] = {a}
b = Names[-1] = {b}
""")

# task 9
a, b ,*_= Names
print(f"""
a = Names[0] = {a}
b = Names[1] = {b}
""")
