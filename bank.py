# 16 student class
# class Student:
#     def __init__(self,name="",marks=0):
#         self.Name=name
#         self.Marks=marks

#     def passm(self):
#         if self.Marks>=40:
#             print("Student is passed")
#         else:
#             print("Student is failed")
#         print("student name",self.Name)
        
# mrk=int(input("Enter student marks"))
# name=input("Enter student's name")
# s=Student(name,mrk)
# s.passm()



# 17 bank account
# class Account:
#     def __init__(self,acc_h,bal):
#         self.acc_holder=acc_h
#         self.balance=bal

#     def deposit(self,money):
#         self.balance+=money
#         print("your balance after depositing money",self.balance)

#     def witdraw(self,money):
#         self.balance-=money
#         print("your balance after witdrawing money",self.balance)
        
# holder=input("Enter accounter holder name")
# bal=int(input("Enter account balance"))
# a=Account(holder,bal)
# a.deposit(30000)
# a.witdraw(30000)


# 20 shape class and derived circle class
# class Shape:
       
#     def area(self):
#         return (2*3.14*self.radius)

# class Circle:
#     def __init__(self,rad):
#          self.radius=rad   

#     def area(self):
#         return (2*3.14*self.radius)  

# cir=Circle(5)
# print("Radious of the circle is ",cir.area())



# 21 movie class
# class Movie:
#     def __init__(self,tt="",gen="",rat=0):
#         self.title=tt
#         self.genre=gen
#         self.rating=rat
#     def display(self):
#         print("The title of the movie is ",self.title)
#         print("The genre of the movie is ",self.genre)
#         print("The rating of the movie is ",self.rating)
  
# tt=input("Enter the title of the movie")
# gen=input("Enter the genre of the movie")
# rt=int(input("Enter the rating of the movie"))
# m=Movie(tt,gen,rt)
# m.display()



class Person:
    def __init__(self,name="",age=0):
        self.name=name
        self.age=age

    def display(self):
         print(f"name{self.name}, age: {self.age}")

class Student(Person):
        def __init__(self, name="", age=0,grade=0):
             super().__init__(name, age)
             self.grade=grade
            
        def display(self):
             print(f"name{self.name}, age: {self.age},Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def display_info(self):
        return f"{super().display_info()}, Subject: {self.subject}"

s1=Student('Digvijay',20,'A')
t1=Teacher("dsfgsfg",40,"maths")
print(s1.display())
print(t1.display())