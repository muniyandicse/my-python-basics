#INHERITANCE

#single
class brands:
    brandname1 = 'facebook'
    brandname2 = 'you tube'
    brandname3 = 'Amazon'

class products(brands):
    products1 = 'social media'
    products2 = 'video Blog'
    products3 = 'online shopping'

uses = products()
print(uses,brandname1,'is a',uses.products1)
print(uses.brandname2,'is a',uses.products2)
print(uses.brandname3,'is a',uses.products3)

#multiple
class phone:
    def call(self):
        print('make call')
    def sms(self):
        print('send message')
class computer:
    def filestorage(self):
        print('store files')
    def internet(self):
        print('Browse')

class android(phone,computer):
    def tracking(self):
        print('GPS tracking')

obj = android()
obj.call()
obj.sms()
obj.filestorage()
obj.internet()
obj1.tracking()

#mutilevel
class personal:
    def getpersonaldetails(self):
        self.name = input('Enter Name        :')
        self.age = int(input('Enter Age       :'))
        self.mall - input('Enter MailId        :')

class educational(personal):
    def getpersonaldetails(self):
        self.collegname = input('Enter college name  :')
        self.department - input('Enter Depertment   :')
class professional(educational):
    def getprofessionaldeteils(self):
        self.companyname = input('Enter Company name  :')
        self.designation = input('Enter Designation  :')

class details(professional):
    def displaydetails(self):
        print('name               :',self.name)
        print('age              :', self.age)
        print('Mail iD               :', self.mail)
        print('College Name               :', self.collegname)
        print('Department             :', self.department)
        print('Company Name               :', self.companyname  )
        print('Designation               :', self.designation)

obj = details()
obj.getpersonaldetails()
obj.geteducationaldetails()
obj.getprofessionaldeteils()
obj.displaydetails()

#hierarchial
class area:
    print('welcome')

class triangle(area):
    def findarea(self,h,b):
        print('Area of triangle :',0.5*h*b)

class square(area):
    def findarae(self,s):
        print('Area of Square  :',S*S)

sq = square()
sq.findarea(10,20)

#HYBRID
class university:
    def display(self):
        print('The university name is ABC university')
class branch(university):
    def display(self):
        print('the branch name is date science')
class course(university):
    def disolay(self):
        print('the course name is IT')
class student(branch,course):
    def display(self):
        branch.display(self)
        course.disolay(select)
        university.display(self)
obj = student()
obj.display()

#ENCAPSULATION
class customer:
    def phoneno(self):
        print('phone no : 12372123')
    def domain(self):
        print('operator    : Airtel')
    def address(self):
        print('place      :chennai')
ob  = customer()
ob.phoneno()
ob.domain()
#abstraction
from  abc import  ABC
class user(ABC):
    def __init__(self,name,numofnonths):
        self.name - name
        self.numofmonths = numofmonths
    def process_feel(self):
        pass
class platinumuser(user):
    platinumuser = 2200
    def process_fee(self):
        return self.numofmonths * platinumuser.platinumpackage
class golduser(user):
    goldpackage = 1800
    def process_fee(self):
        return self.numofmonths * golduser.goldpackage

ob1 = platinumuser('Arun',7)
ob1.display_user()
fee = ob1.process_fee()
print('fee is',fee)

ob2 = golduser('ajay',4)
ob2.display_user()
fee = ob2.process_fee()
print('fee is ',fee)
#polymorphism
value1 = 1
value2 = 3
print('addition of numbers :',value1+value2)

stringvalue1 = 'good'
stringvalue2 = 'morning'
print('concatenation of strings :',stringvalue1 + stringvalue2)

value1 = 1
value2 = 3
print('Multiplication of numbers :',value1*value2)

stringvalue1 = 'good'
stringvalue2 = 3
print('replication of  strings :',stringvalue1 * value)

stringvalue = 'welcome'
print('Length of string :',len(stringvalue))

dictvalue = {'aa':1,'bb':2,'cc':3}
print(('Length of dictioary : ',len(dictvalue))

class employee:
    def details(self):
        name = 'Arun'
        dept = 'IT'
        print(name,'from',dept)

class admin:
    def details(self):
        name = 'Ajay'
        dept = 'CSE'
        print(name,'from',dept)

ob1 = employee()
ob.details()

ob = admin()
ob.details()




