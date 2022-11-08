
def sdvig(n):
    a =int(input())
    print(n)
    return n[a:]+ n[:a] or n[-a:]+ n[:-a]
#print(sdvig([5,7,9,10,2]))



def country_1 (n):
    d ={'1': 'kyrgyzstan', '2': 'kazahstan'}
    if type (n) == int:
        for i in d.keys():
            if str(n)==i:
                return d.get(i)
#print(country_1(2))

#n = int(input())
#factorial = 1
#while n > 1:
#    factorial *= n
#    n -= 1
 
#print(factorial)

def length(lst):
    if not lst:
        return 0
    return 1 + length(lst[1:])
a = [1,2,3]
#print("Длина списка равна:")
#print(length(a))




'''
l = []

def qwerty(b):
    if (b == 0):
        return l
    dig = b % 2
    l.append(dig)
    qwerty(b // 2)
a = int(input("Введите число: "))
qwerty(a)
l.reverse()
print("Двоичная форма числа:")
for i in l:
    print(i)
'''



def findmin(ls):
    max_num = max(ls)
    for i in ls:
        max_num = max_num - 1
        if max_num in ls:
            return max_num + 2
        else:
            continue 
print(findmin([1, 2, 3, 4, 5, 6]))