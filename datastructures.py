#LIST#

#INDEX
friuts=['apple','orange','mango','watermelon','grapes']
print(friuts)
print(friuts.index('mango'))
#count
fruits=['apple','orange','mango','watermelon','grapes']
print(fruits)
print(friuts.count('mango'))
#extend
fruits=['apple','orange','mango','watermelon','grapes']
fruits1=['jackfruit','strawberry']
fruits.extend(fruits1)
print(fruits)
#append
fruits=['apple','orange','mango','watermelon','grapes']
fruits1=['jackfruit','strawberry']
fruits.append(fruits1)
print(fruits)
#reverse
fruits=['apple','orange','mango','watermelon','grapes']
fruits.reverse('orange')
print(fruits)
#remove
fruits=['apple','orange','mango','watermelon','grapes']
fruits.remove('orange')
#insert
fruits=['apple','orange','mango','watermelon','grapes']
fruits.insert(2,strawberry)
#pop
fruits=['apple','orange','mango','watermelon','grapes']
fruits.pop(2)

##TUPLES##

#create Tuple
a=(11,14,24,76,'abc',2.3)
print(a)
print(type(a))
#update
a=('aaaa','bbbb','cccc','dddd')
b=(1,2,3,4)
c=a+b
print(c)
#delete tuple
a=('aaaa','bbbb','cccc','dddd','1,2,3,4')
delete
print(a)
#slicing tuple
mobiles=('sony','oppo','vivo','samsumg','pocp')
print(mobiles[1:2])
print(moiles[3:])
print(mobiles[:1])
print(mobiles[:])
#nested tuple
a=(1,2,3,4)
b=(6,4,7,8)
c=(a,b)
print(c)
#SET

#add
subjects= {'english'}
print(subjects)
subjects.add('maths')
subjects.add('science')
subjects.add('hindi')
print(subjects)
#update
fruits={'apple','orange','grapes','mango'}
fruits={'cherry','strawberry'}
fruits.update(fruits1)
print(fruits)
#remove
fruits={'apple','orange','grapes','mango','cherry','strawberry'}
fruits.remove('orange')
print(fruits)
#discard
fruits={'apple','orange','grapes','mango'}
fruits=discard('orange')or('orange')
print(fruits)
#pop
fruits={'apple','orange','grapes','mango'}
print(fruits)
fruits.pop()
print(fruits)
fruits.pop()
print(fruits)
#clear
fruits={'apple','orange','grapes','mango'}
fruits.clear()
print(fruits)
#len
fruits={'apple','orange','grapes','mango'}
print(len(fruits))
#sum
numbers={4,2,3,5,7,9,0}
print(sum(numbers))
print(min(numbers))
print(max(numbers))
#additional operations

#issubset
androidnew={'pie','oreo','nouget','marshmallow'}
androidold={'lollipop','kitkat','jallybeen'}

print(androidnew.issubset(androidold))
print(androidnew<androidold)
#issuperset
print(androidnew.issuperset((androidold)))
print(androidnew>androidold)
#union
print((androidnew.union(androidold))
print(androidnew|androidold)
#intersection
print(androidnew.intersection(androidold))
print(androidnew&androidold)
#difference
print(androidnew.difference(androidold))
print(androidnew-androidold)
#symmetric-difference
print(androidnew.symmetric_difference(androidold))
print(androidnew^androidold)








