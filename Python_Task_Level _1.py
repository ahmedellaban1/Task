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
def task_3(x, y):
    for i in range(x, y+1):
        print(f"---------- Multiplication table of {i} ------------")
        for n in range(1,13):
            print(f"{n}\t* {i} = \t{n*i}")
task_3(1, 12)

# task 4
def task_4(sentence):
    blank_list = []
    for i in sentence.split(' '):
        if i not in blank_list:
            blank_list.append(i)
        else : continue
    return blank_list
print(task_4("i'm i'm ahmed ahmed ellaban"))

# task 5
def task_5(sentence):
    return len(sentence) - sentence.count(' ')
print(task_5('ahmed ellaban '))

# task 6
def task_6(sentence, word):
    sentence_list = sentence.split()
    for i in sentence_list:
        if word == i :
            sentence_list.remove(i)
    return sentence_list
print(task_6('ahmed ellaban ahmed', 'ahmed'))

# task 7
def task_7(sentence, word):
    return sentence.count(word)
print(task_7('ahmed ellaban ahmed', 'ahmed'))

# task 8
def task_8(x, y):
    return [i for i in range(x, 100) if i % y == 0]
print(task_8(8, 8))

