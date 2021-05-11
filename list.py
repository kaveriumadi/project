l1 = [1,2,4,3,6,7,8,4,3]
print(l1)

l1[4]

print(l1[4])

print(len(l1))

l1.append(22)
print(l1)

l1.append(25)
print(l1)

l1.insert(2, 45)
print(l1)

l2 = [4,6,2,8]
l1.extend(l2)
print(l1)

l1[2]=20
print(l1)

l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.sort()
print(l1)

l1.pop()
print(l1)

l1.pop(1)
print(l1)

l3 = ["a", "b", "c","d", "a", "b"]    #removing the duplicate values
l3 = list(dict.fromkeys(l3))
print(l3)

text = "hello everyone"[::-1]         #reverse the string
print(text)

#x = input("enter a first number:")
#y = input("enter the second number:")

#sum = int(x) + int(y)                 #adding two numbers
#print(sum)

print(l1)

def count_3s():
    cnt = 0
    for i in l1:
        if i == 3:
            cnt=cnt+1
    return cnt
print(count_3s())