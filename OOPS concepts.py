# # # # # # # Class: a blueprint for creating objects
# # # # # # class Student:
# # # # # #     name = "sandy"

# # # # # # # Object (instance of Student)
# # # # # # s1 = Student()

# # # # # # #   here when we use '.' with s1 or student , in case of s1 , s1 has stored student class  and '.' means inside the function associated. 
# # # # # # #  when we use s1.name we are telling intrepreter to use name variable in class student that's why it gives the name sandy as output same with student.name
# # # # # # #since name = sandy is mentioned in class variable then it will always be the name = sandy when ever we call the variable or function related to it .
# # # # # # s2 = "sanket"   # normal string variable, NOT related to class

# # # # # # print(Student.name)  # access class variable
# # # # # # print(s1.name)       # access class variable via object
# # # # # # print(s1)            # object reference 


# # # # # # # constructor 
# # # # # # # All classes have function called __init__(), which is always called whenever a new object is created or initiated.

# # # # # class student:
# # # # #   #default parameters
# # # # #     def __init__(self):  # it is created by default whether u want it or not.
# # # # #         pass
# # # # #     def __init__(self,name,marks):
# # # # #         self.name=name
# # # # #         self.marks = marks
# # # # #         print("adding it to the data base")
# # # # # #in above code u can change self if u want but we ususally do not do that to avoid confusion . it is used refrence the object
# # # # # # __init__() is a special method that initializes object data.
# # # # # # If multiple __init__() methods are defined, the last one overrides the others.
# # # # # # The 'self' parameter refers to the current object and is used to access instance variables.


# # # # # s1=student("sanket",99)
# # # # # print(s1.name,s1.marks)

# # # # # s2=student("adii",100)
# # # # # print(s2.name,s2.marks)
        
# # # # # s3=student("adii",10)
# # # # # print(s3.name,s3.marks)
        

# # # # # #  self.name=name  # means every object named self.name  it's object can have different values
# # # # # #         self.marks = marks


# # # # # #class and instance attributes

# # # # # # instance attributes are different for every object.
# # # # #  # we ususally store common objects or other codes in class attributes.
# # # # #  # object attributes >>class attributes


# # # # # #Quick question 

# # # # # class student:
# # # # #     def __init__(self,name,math,chemistry,physics):
# # # # #         self.name = name
# # # # #         self.math=math
# # # # #         self.chemistry=chemistry
# # # # #         self.physics=physics

# # # # # s1=student("sanket",23,26,31)
# # # # # print("student name is : ",s1.name,"marks in maths is :",s1.math,"marks in chemistry",s1.chemistry,"marks in physics:",s1.physics)       

# # # # class student:
# # # #     def __init__(self,name,marks):
# # # #         self.name = name 
# # # #         self.marks = marks

# # # #     def avg_m(self):
# # # #         sum=0
# # # #         for val in self.marks:
# # # #             sum+= val
# # # #         print(self.name ,"avg score is ",sum/3)
# # # # s1= student("Sanket",[99,99,32])
# # # # s1.avg_m()

# # # # ABSTRACTION 
# # # # hiding unwanted details from user or implementation details of class
# # # # essential features to the user

# # # # class Car:
# # # #     def __init__(self):
# # # #        self.acc = False
# # # #        self.brk = False
# # # #        self.clutch=False

# # # #     def start(self):
# # # #         self.clutch= True
# # # #         self.acc =True
# # # #         print("Car started.....")

# # # # car1 =Car()
# # # # car1.start()



# # # #Wrapping data and functions into a single unit (object)

# # # class account:
# # #     def __init__(self,balance , accno):
# # #         self.balance=balance
# # #         self.accno=accno

# # # #debit method
# # #     def debit(self,amount):
# # #         self.balance -= amount
# # #         print("RS",amount,"amount was debited")
# # #         print("total balance = ",self.get_balance())

# # #     def credit(self,amount):
# # #         self.balance +=amount
# # #         print("your account havs credited by RS")
# # #         print("total balance = ",self.get_balance())

    
# # #     def get_balance(self):
# # #       return self.balance


# # # acc1 = account(10000,12345)
# # # print(acc1.balance)
# # # print(acc1.accno)
# # # acc1.debit(1000)
# # # acc1.credit(6969696)
# # # acc1.credit(90)
# # # acc1.debit(90000)
# # # acc1.balance


# # #OOPS lecture 2 on youtube [apana college]

# # # #using del keyword
# # # class student:
# # #     def __init__(self,name):
# # #         self.name = name
# # # s1 = student("sanket")
# # # print(s1)
# # # print(s1.name)

# # # del (s1.name)
# # # print(s1)


# # # class Person:
# # #     __name ="anoymous" # use double underscore to make attribute private 

# # #     def __hello(self):
# # #         print("hello person")
    
# # #     def welcome(self):
# # #         self.__hello()

# # # p1 = Person()
# # # print(p1.welcome())  


# # # inheritance  
# # #inherating the properties of one function[parent] to another[child]

# # #example

# # # class Car:
# # #     def __init__(self,type):
# # #         self.type = type

# # #     @staticmethod
# # #     def start():
# # #         print("Car starting...")
    
# # #     @staticmethod
# # #     def stop():
# # #         print("Car stopped")


# # # class ToyotaCar(Car): # here Car is a class referenced here meaning Car is the parent class .
# # # super() acts as a parent class each time it's used or referenced 
# # #     def __init__(self, name,type):
# # #         super().__init__(type)
# # #         self.name = name
# # #         super().start()


# # # car1 = ToyotaCar("Fortuner","electric")
# # # car2 = ToyotaCar("Prius")
# # # print(car1.type)

# # # print(car1.name)
# # # car1.start()
# # # print(car1.color)


# # #class method 
# # ''' a class method is boound to the class and receives the class as an implicit first argument 0
# # # NOTE: static method can't access or modify class and generally for utility 
# # class Student 
# #     @classmethod # it's a decorator 
# #     def college(cls):
# #     pass
# # '''

# # class Person:
# #     name = "anomymous"

# #     #def changeName(obj , name):
# #     # self.__class__.name = "sanket"

# #     @classmethod
# #     def changeName(cls,name):
# #         cls.name = name 

# # p1 = Person()
# # p1.changeName("Sanket")
# # print(p1.name)
# # print(Person.name)

# # property decorator
# # we use @PROPERTY DECORATOR ON ANY METHOD 
# # IN THE CLASS TO USETHE METHOD AS A PROPERTY 
# # property decorator is use ful for us to give direct 
# class Student:
#     def __init__(self,phy ,chem ,math):
#         self.phy = phy 
#         self.chem = chem 
#         self.math = math


#         @property 
#         def percentage(self):
#             return str((self.phy +self.chem+self.math)/3) + "%"
        
#         stu1 = Student(98,97,99)
#         print(stu1.percentage)

#         stu1.phy = 86
#         print(stu1.percentage)
          
        
#Polymorphism : Operator Overloading 

#when the same operator is allowed to have different meaning according to the context 

#Operators and dunder functiond
'''
operators              DUNDERS
a+b #addition         a._add__(b)
a-b #substraction     a.__sub__(b)
a*b #multiplication   a.__mul____(b)
a/b #division         a.__truediv____(b)
a%b #addition         a.__mod___(b)'''

#simple examples 
 #it ends here 
 