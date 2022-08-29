##Function//

#Lambda

value=lambda a:a*2
print(value(10))

#ex:2
def value(a,b):
    return a+b
    print(value(10,20))
#ex:3
def value(a,b=20):
    return  a+b
print(value(10))
value=lambda a,b=20:a+b
print(value(10))
#ex:4
def values(args)
    print(sum(args))
    values(10,20,30,40,50)
    value=lambda *args:sum(args)
    print(value(10,20,30,40,50))
#map
m=map(lambda a:a**2[1,2,3,4,5])
print((list(m)))
#exp:2
name='jeeva'
m=lambda a:a.upper()
m=map(m,name)
print(list(m))
#exp:3
value='programing'.split()
m=lambda a:a.upper
m=map(m,value)
print(list(m))
#filter
value=[1,2,3,4,5,6,7]
print(list(filter(lambda a:a%2=0,value)))
#exp:4
l=lambda  a:a**2
x=map(1,range(10))
y=filter(lambda x:x>5andx<5ax)
print(list(y))
#reduce
value=[1,2,3,4,5]
print(reduce(lambda a:a,b:a+b,value))
#exp:2
value=[10,20,30,70,50]
print(reduce(lambda a,b:a if a>b else b,value))
#list comprehension
separated_letter = []
for letter in 'engineering':
    separated_letter.append(letter)
print(separated_letters)

print([letter for letters in 'engineering'])
#exp:2
value=[]
for i in range(1,11):
    vlaue.append(i)
print(values)

print([i for i in range(1,11)])
#exp:3
vowls =[]
for i in 'this is a pan':
    if i in 'aeiou':
        vowls.append(i)
print(vowls)

print([i for in 'this is a pen' if i in 'aeiou'])
exp:4
fruits = ['apple','berry','plum']
fruits1 = ['pineapple','strawberry','crange','dryplum']
vlues = []
for i in fruits:
    for j in fruits1:
        if i in j:
            value.append(j)
print(values)

print([j for i in fruits for j in fruits1 if i in j])
#exp:5
numbers = []
for i in range(1,11):
    if i%2 == 0:
        numbers.append(str(i)+" :even")
    else:
        numbers.append(str(i)+" :odd")
print(numbers)

print([str(i)+' : even' if i%2 == 0else str(i)+' :odd' for i in range(1,11])













