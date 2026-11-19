# products = {"book", "pen", "eraser", "sharpner",
#  "paper"}
# products = ["Sculpture", "Painting", "Sculpture", "Figurine", "Painting"]
# print(set(products))
# fruits={"apple","orange","banana"}
# fruits.add("berry")
# fruits.update(["mango","strawberry","guava"])
# print(fruits)
# languages = {"Python", "Java", "JavaScript", "C++", "Ruby"}
# languages.discard("Java")
# print(languages)
# languages.discard("Ruby")
# print(languages)
# removes=languages.pop()
# print(removes)
# languages.clear()
# print(languages)
# products = {"Sculpture", "Painting", "Figurine", "Vase", "Statue"}
# for product in products:
#     print(product)
# six={ product for product in products if len(product)>6 }
# print(six)
# print(len(products))
# seven={ product for product in products if len(product)<7 }
# print(seven)
# print(products,six,seven)
# frontend = {"HTML", "CSS", "JavaScript", "React", "Bootstrap"}

# backend = {"Python", "JavaScript", "Node.js", "React", "Django"}
# print(frontend|backend)
# print (frontend.intersection(backend))
# print(frontend-backend)
# print(backend-frontend)
# print(frontend^backend)
# print(frontend,backend)
# python_students = {"Shifa", "Amina", "Sara", "Hana"}

# web_students = {"Shifa", "Sara"}

# data_students = {"Amina", "Hana"}

# print(web_students.issubset(python_students))
# print(web_students.issuperset(python_students))
# print(web_students&data_students)
# print(web_students.isdisjoint(data_students))
# copies=python_students.copy()
# copies.add("zara")
# print(copies,python_students)
# morning_batch = {"Shifa", "Amina", "Sara", "Hana", "Zara"}

# evening_batch = {"Sara", "Hana", "Ali", "John", "Zara"}

# cancelled_students = {"John", "Amina"}
# registerd=evening_batch.union(morning_batch)
# active=registerd-cancelled_students
# print(morning_batch^evening_batch)
# print(morning_batch&evening_batch)
# print(morning_batch-evening_batch)
# print(evening_batch-morning_batch)
# print(active)
# print( "Shifa" in registerd )
# print("John"  in  active)
# print(len(active))
# numbers = [10, 15, 20, 25, 30, 15, 40, 20, 50, 10, 60]
# unique=set(numbers)
# even={nums for nums in numbers if nums%2==0}
# square={sq**2 for sq in unique}
# greater={num for num in numbers if num>25}
# print(unique)
# print(even)
# print(greater)
# print(square)
# print(len(unique))
# employees = ["Shifa", "Amina", "Sara", "Hana", "Shifa", "Ali", "John", "Sara"]

# developers = {"Shifa", "Sara", "Ali", "John"}

# designers = {"Amina", "Hana", "Sara"}

# managers = {"John", "Amina"}
# dd=developers|designers
# unique=set(employees)
# print(unique)
# print(developers&designers)
# print(developers-managers)
# print(designers-developers)
# print(unique-dd)
# print(unique-managers)
# print("Shifa" in developers)
# print(designers.issubset(unique))
# print(len(unique))
# students = ["Shifa", "Amina", "Sara", "Hana"]
# removed=students.pop(3)
# students.append("Ali")
# print(students)
# students.insert(1,"John")
# print(students)
# students.extend(["Zara","Maryam"])
# print(students)
# students.remove("Sara")
# print(students)
# print(removed)
# print(len(students))
# for stu in students:
#     print(stu)
# languages = ("Python", "Java", "JavaScript", "Python", "React")
# hello=list(languages)
# print(languages[1])
# print(languages[3:])
# print(languages.count("Python"))
# print(languages.index("JavaScript"))
# print(hello)
# hello.append("django")
# print(hello)
# print(tuple(hello))
# hello=set()
# print(type(hello))
# student = {
#     "name": "Shifa",
#     "age": 18
# }
# student.update({"age":30,
# "course":"fullstack"})
# print(student["name"])
# # print(student)
# language = "JAVASCRIPT"
# print(language[4],language[-1],language[1:5])
# first_name = "Shifa"
# course = "Python"
# sent=first_name+" is learning "+course
# print(sent)
# print(sent*3)
# project = "SIVK SCULPT"
# print("SIVK" in project)
# print("sculpt" in project)
# print("MEMORA" not in project)
# print("V" not in project)
# sentence = "I love Python"

# words = sentence.split()
# print(words)

# result = "-".join(words)
# print(result)
# print("Shifa123".isalpha())
# print("2026".isdigit())
# print("Python123".isalnum())
# print("Python 123".isalnum())
# print("   ".isspace())
# print("Hello World".istitle())

#DAY THREE:-

# students={"name":"shifa","age":18,"course":"bca","university":"jain university"}
# student=students.copy()
# print(student["name"])
# print(student["age"])
# aged=student["age"]=19
# print(aged)
# city=student["city"]="kozhikkode"
# print(city)
# lang=student["skills"]="python","js","node"
# print(lang)
# print(student.keys())
# print(student.values())
# print(student)

# inventory = {
#     "laptop": 10,
#     "mouse": 25,
#     "keyboard": 15,
#     "monitor": 8
# }
# print(inventory["laptop"])
# mouse=inventory["mouse"]=30
# head=inventory["headphones"]=12
# inventory.pop("monitor")
# key=inventory.keys()
# value=inventory.values()
# print(key)
# print(value)
# for key,value in inventory.items():
#     print(key,":",value)
# print()
# print(len(inventory))
# print("keyboard" in inventory)
# students = {
#     "student1": {"name": "Shifa", "marks": 85},
#     "student2": {"name": "Amina", "marks": 92},
#     "student3": {"name": "Sara", "marks": 76},
#     "student4": {"name": "Hana", "marks": 95},
#     "student5": {"name": "Ali", "marks": 60}
# }
# print(students["student1"]["name"])
# print(students["student2"]["marks"])
# sara=students["student3"]["marks"]=80
# john=students.update({"student6":{"name": "john", "marks": 88}})
# for key, value in students.items():
#     print("Name:", value["name"])
#     print("Marks:", value["marks"])
# eighty={key:value for key,value in students.items() if value["marks"]>=80}
# print(eighty)
# beloweigty={key:value for key,value in students.items() if value["marks"]<80}
# print(beloweigty)
# print(len(students))
# high=max(value["marks"] for value in students.values())
# print(high)
# name = "SIVK SCULPT"
# one=name[:4:]
# two=name[5::]
# print(name[0])
# print(name[-1])
# print(one)
# print(two)
# print(name[::-1])
# equal=one+" "+two
# print(equal)
# print(equal * 3)
# print("SIVK" in name)
# print("MEMORA" not in name)
# description = "   sivk sculpt creates beautiful miniature sculptures   "
# space=description.strip()
# print(space)
# print(description.lower())
# print(description.upper())
# print(description.capitalize())
# print(description.title())
# print(description.replace("beautiful","elegant"))
# sliced=description.split()
# print(sliced)
# print("-".join(sliced))
# print(description.count("sculpt"))
# print(space.startswith("sivk"))
# print(space.endswith("sculptures"))
# review = "Python is easy to learn. Python is powerful and Python is popular."
# print(review.count("Python"))
# print(review.find("powerful"))
# print(review.find("easy"))
# print(review.startswith("Python"))
# print(review.endswith("p  opular"))
# print("Java" in review )
# print(review.index("Java"))
# print(len(review))
# print(review.upper())
# print(review.lower())
# def calculate_area():
#     length=10
#     width=5
#     return length*width


# total=calculate_area()
# print(total)
# def check_age():
#     age = 18
#     if age>=18:
#         print("Eligible to vote")
#     else:
#         print("Not eligible to vote")

# check_age()        
# def welcome_user(name):
#     return "welcome "+ name 

# print(welcome_user("shifa"))
# print(welcome_user("sivk"))
# print(welcome_user("chippa"))
# def calculate_discount(price,discount_percentage):
#     discount=price*discount_percentage/100
#     final=price-discount
#     return final
# run=calculate_discount(2000,10)
# print(run)
# def student_details():
#     print("Name: Shifa")
#     print("Age: 18")
#     print("Course: BCA")
#     print("University: Jain University")

# student_details()
# student_details()

# def student(**name):
    
#         print(name)
# student(    name="Shifa",
#     age=18,
#     course="BCA",
#     city="Kozhikode")
# def student_details(name,age,course="bca"):
#     print("name : ",name)
#     print("age : ",age)
#     print("course : ",course)
# student_details("shifa",18)
# student_details(age=18,name="shifa")
# student_details("amina",20)
# def calculate_total(*prices):
#     total=0
#     for price in prices:
#         total+=price
#     return total
# result=calculate_total(250,450,300,500)
# # print(result)
# def employee_details(**details):
#     for key,value in details.items():
#         print(key ," : ",value)
        
# employee_details(name="shifa",age=18,department="development",role="python developer",company="sivk technologies")
# def order_details(name,*price):
#     print("name : ",name)
#     print("price :",price )
# order_details("shifa",10,20,30)
# def employee_details(name, *skills, **details):
#     print("Name:", name)

#     print("Skills:")
#     for skill in skills:
#         print(skill)

#     print("Additional details:")
#     for key, value in details.items():
#         print(key, ":", value)


# employee_details(
#     "Shifa",
#     "Python",
#     "JavaScript",
#     "React",
#     age=18,
#     department="Development",
#     company="SIVK Technologies"
# )
# def register_employee(name,*skills,**details):
#     print("name : ",name)
#     for skill in skills:
#         print(skill)
#     for key,value in details.items():
#         print(key,value)
# register_employee("shifa","python","javascript","react","node.js",age=18,department="DEVElopment",role="fullstack",company="sivk technologies")
# def register_student(name,age,*hobbies,course="BCA",**info):
#     print(name,'\n',age)
#     print(course)
#     for hobbie in hobbies:
#         print(hobbie)
#     for key,value in info.items():
#         print(key,value)
# register_student("shifa",18,"drawing","sketching","coloring",city="kannur",university="jain university",country="india")
# register_student("amina",18,"drawing","sketching","coloring",course="bca", city="kannur",university="jain university",country="india")
# def calculate_sum(num):
#     if num==0:
#         return 0
#     return num+calculate_sum(num-1)   
# result=calculate_sum(5)
# print(result)
# def reverse_string(name):
#     if name=="":
#         return""
#     return reverse_string(name[1:])+name[0]
# print(reverse_string("python"))

# def factorial(num):
#     if num<0:
#         return "negative are not allowed"
#     if num==0:
#         return 1
#     return num*factorial(num-1)
# print(factorial(5))
# def fibonacci(n):
#     if n<0:
#         return("nega tive are not allowed")
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(5))
# def number(n):
#     if n==0:
#         return n
#     return n+number(n-1)
# print(number(5))
# cube=lambda n:n**3
# print(cube(5))
# multiply=lambda n,m:n*m
# print(multiply(5,3))
# is_positive = lambda n: True if n > 0 else False

# print(is_positive(-1))
# numbers = [2, 4, 6, 8, 10]
# five=map(lambda n:n*5,numbers)
# print(list(five))
# numbers = [10, 15, 20, 25, 30, 35, 40]
# twenty5=filter(lambda x: x>25,numbers)
# print(list(twenty5))
# employees = [
#     {"name": "Shifa", "salary": 25000},
#     {"name": "Amina", "salary": 40000},
#     {"name": "Sara", "salary": 30000}
# ]
# sorting=sorted(employees,key=lambda employee:employee["salary"],reverse=True)
# print(sorting)
# import math,random
# num=int(input("enter a number: "))
# print(math.sqrt(num))
# print(random.randint(1,100))
# print(math.factorial(num))
# import student
# print(student.student_name())
# print(student.student_age())
# print(student.student_course())

# try: 
#     num=int(input("enter a number: "))
#     nums=int(input("enter a number: "))
#     result=num/nums
    
# except ZeroDivisionError:
#     print("cannot divided by zero")
# except ValueError:
#     print("enter an intiger")
# else:
#      print("Result:", result)
# finally:
#     print("Program completed")
#day 55555555

# class vehicle:
#     def start(self):
#         print("vehicle started")
#     def stop(self):
#         print("vehicle stopped")
# class car(vehicle):
#     def drive(self):
#         print("car is driving")
# car1=car()
# car1.start()
# car1.stop()
# car1.drive()
#
#-----------------------------------------------------------------------------
# class employee():                                                           |
#     def __init__(self,name,salary):                                         |
#         self.name=name                                                      |
#         self.salary=salary                                                  |
#     def dispaly(self):                                                      |
#         print(self.name, "here you go")                                     |
#         print(self.salary, " got it")                                       |
# class Manager(employee):                                                    |
#     def __init__(self, name, salary,department):                            |
#         self.department=department                                          |
#         super().__init__(name, salary)                                      |
#     def started(self):                                                      |
#         print("name :", self.name)                                          |
#         print("salary :",self.salary )                                      |
#         print("department :",self.department)                               |
# manger1=Manager("SIVK",1000000000000,"CEO")                                 |
# manger1.started()                                                           |
# manger1.dispaly()                                                           |
#-----------------------------------------------------------------------------
# class father():
#     def height(self):
#         print("Father has good height")
# class mother():
#     def intelligence(self):
#         print("Mother is intelligent")
# class student(father,mother):
#     def study(self):
#         print("Student is studying")
# child1=student()
# child1.height()
# child1.intelligence()
# child1.study()
# class Grandfather:
#     def house(self):
#         print("Grandfather owns a house")

# class Father(Grandfather):
#     def car(self):
#         print("Father owns a car")

# class Child(Father):
#     def bike(self):
#         print("Child owns a bike")


# child1 = Child()

# child1.house()
# child1.car()
# child1.bike()
# class Employee:
#     compony="google"
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def display(self):
#         print("name :",self.name)
#         print("salary :",self.salary)
# employee1=Employee("sivk",18)
# employee2=Employee("pp",20)
# employee1.display()
# employee2.display()
# print(employee1.compony)
# print(employee2.compony)
# class Student:
#     def display(self):
#         message = "Hello, Student!"
#         print(message)

# student1 = Student()
# student1.display()
# class Employee:
#     compony="google"
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def display(self):
#         print("name :",self.name)
#         print("salary :",self.salary)
#         message = "Employee Details"
#         print(message)
# employee1=Employee("sivk",18)
# employee2=Employee("pp",20)
# employee1.display()
# employee2.display()
# print(employee1.compony)
# print(employee2.compony)
# class mobile:
#     def __init__(self,brand,price):
#         self.price=price
#         self.brand=brand
#     def display_details(self):
#         print("brand : ",self.brand)
#         print("price : ",self.price)
# mobile1=mobile("sivk",10000000000000)
# mobile2=mobile("iphone",1000)
# mobile1.display_details()
# mobile2.display_details() 
# class here:
#     compony="google"
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print("name : ",self.name)
#     @classmethod
#     def change_company(cls,comppany):
#         cls.compony=comppany
# here1=here("sivk")
# here2=here("pp")
# here.change_company("microsoft")
# here1.display()
# here2.display()
# print(here1.compony)
# print(here2.compony)
# class calculator:
#     @staticmethod
#     def add(a,b):
#         print(a+b)                                               
#     @staticmethod
#     def multiply(a,b):
#         print(a*b)
# calculator1=calculator()
# calculator1.add(5,5)
# calculator1.multiply(5,5) 
# class school:
#     def introduce(self):
#         print("i am a school student")
# class collagestudent(school):
#     def introduce(self):
#         print("i am a collage student")
# collagestudent1=collagestudent()
# collagestudent1.introduce()
# class Parent:
#     def display(self):
#         print("Parent method")

# class Child(Parent):
#     def display(self):
#         print("Child method")
#         # What should we write here to call the parent method?
#         super().display()

# obj = Child()
# obj.display()
# class car:
#     def start(self):
#         print("Car engine started")
# class bike:
#     def start(self):
#             print("bike engine started")
# car1=car()
# bike1=bike()
# car1.start()
# bike1.start()
# print(5 * "SIVK")
# print("Python " * 2 + "Developer")
# class calculator():
#    def multiply(self,a,b,c=1):
#         print((a*b)*c)
# calculator1=calculator()
# calculator1.multiply(5,10)
# calculator1.multiply(5,10,5)
# class student:
#     def total_marks(self,*marks):
#         print(sum(marks))
# student1=student()
# student1.total_marks(80,90)
# student1.total_marks(80, 90, 85)
# student1.total_marks(80, 90, 85, 95)
# from abc import ABC,abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#     def company(self):
#         print("Working at Google")
# class Developer(Employee):
#     def work(self):
#         print("Developer is writing code")
# class Manager(Employee):
#     def work(self):
#         print("Manager is managing the team")
# developer1=Developer()
# manager1=Manager()
# developer1.work()
# developer1.company()
# manager1.work()
# manager1.company()
# class Employee:

#     def __init__(self):
#         self.__salary = 50000

#     def display(self):
#         print(self.__salary)


# emp1 = Employee()

# print(emp1._Employee__salary)  # Outside the class
# def set_balance(self, amount):
#     self.__balance = amount
# class BankAccount:
#     def __init__(self):
#         self.__balance=10000
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,amount):
#         self.__balance=amount
# account1=BankAccount()
# account1.set_balance(15000)
# print(account1.get_balance())
# class BankAccount():
#     def __init__(self):
#         self.__balance=10000
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,amount):
#         self.__balance=amount
# account1=BankAccount()
# account1.set_balance(15000)
# print(account1.get_balance())
# class Employee:
#     def __init__(self):
#         self._salary = 50000


# class Manager(Employee):
#     def show_salary(self):
#         print(self._salary)


# manager1 = Manager()
# manager1.show_salary()
# class Vehicle:
#     def  __init__(self):
#         self._speed=120
# class Car(Vehicle):
#     def show_speed(self):
#         print(self._speed)
# car=Car()
# car.show_speed()
# class Employee:
#     def __init__(self):
#         self.name="shifa"
#         self._department="Development"
#         self.__salary=50000
#     def show_name(self):
#         print(self.name)
#     def show_department(self):
#         print(self._department)
#     def get_salary(self):
#         return self.__salary
# emp1=Employee()
# emp1.show_name()
# emp1.show_department()
# print(emp1._Employee__salary)
# class MyNumbers:
#     def __iter__(self):
#         return iter([10, 20, 30])

# numbers = MyNumbers()

# my_iterator = iter(numbers)

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# my_iterator = iter(numbers)
# print(next(my_iterator))
# print(next(my_iterator))
# class number:
#     def __iter__(self):
#         return iter([10,20,30])
# nuber1=number()
# myiter=iter(nuber1)
# print(next(myiter))
# print(next(myiter))   
# myiter=iter(nuber1)
# print(next(myiter))
# class number:
#     def __init__(self):
#         self.value=10
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.value<=30:
#             current=self.value
#             self.value+=10
#             return current
#         else:
#             raise StopIteration
# number1=number()
# myiter=iter(number1)
# print(next(myiter))
# print(next(myiter))


# myiter=iter(number1)

# print(next(myiter))
# print(next(myiter))
# class RollNumbers:
#     def __init__(self):
#         self.value=10
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.value<=50:
#             current=self.value
#             self.value+=10
#             return current
#         else:
#             raise StopIteration
# number1=RollNumbers()
# myiter=iter(number1)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# def numbers():
#     yield 10
#     yield 20
#     yield 30

# for num in numbers():
#     print(num * 2)
# def even_numbers():
#     for num in range(2,11,2):
#         yield num
# for nu in even_numbers():
#     print(nu)
# def even_numbers():
#     for num in range(2,11,2):
#         yield num
# for nu in even_numbers():
#     print(nu)
# file = open("students.txt", "r")


# print(file.read())

# file.close()
# file = open("students.txt", "w")
# file.write("Rahul")
# file.close()
# file=open("students.txt","r")
# print(file.read())
# file.close()
# file = open("students.txt", "r")
# print(file.readlines())
# file.close()
# file = open("students.txt", "w")

# file.write("Shifa\n")
# file.write("Amina")
# file.write("Sara")

# file.close()
# file = open("students.txt", "r")
# print(file.readline())
# print(file.readline())
# print(file.readline())




# with open("students.txt","w") as file:
#     file.write("shifa\namina\nsara\n")
# with open("students.txt","r") as file:
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())
# file=open("students.txt","w")
# file.write("shifa\namina\nsara\n")
# file.close()
# file=open("students.txt","r")
# print(file.read())
# file.close()
# file=open("students.txt","a")
# file.write("rahul")
# file.close()
# file=open ("students.txt","r")
# print(file.read())
# file.close()
# numbers = [2, 4, 6, 8, 10]
# def square(num):
#     return num*num
# result=map(square,numbers)
# print(list(result))
# ages = [12, 18, 25, 15, 30, 16]
# def is_adult(num):
#     return num>=18
# result=filter(is_adult,ages)
# print(list(result))
# from functools import reduce
# numbers = [2, 3, 4, 5]
# def mul(a,b):
#     return a*b
# result=reduce(mul,numbers)
# print(result)
# add=lambda a,b:a+b
# print(add(20,10))
# products = ["Laptop", "Mobile", "Tablet"]
# prices = [50000, 20000, 15000]
# print(list(zip(products,prices)))
# def outer():
#     name = "Shifa"

#     def inner():
#         print(name)

#     return inner

# outer()()
# def my_decorator(func):
#     def wrapper():
#         print("Before function execution")

#         func()

#         print("After function execution")
        
#     return wrapper


# # @my_decorator
# def greet():
#     print("Hello, Shifa!")

# greets=my_decorator(greet)
# greets()
# def my_decorator(func):
#     def wrapper():
#         print("Start")
#         # func()
#         print("End")
#     return wrapper

# @my_decorator
# def welcome():
#     print("Welcome!")

# welcome()
# def test(*args, **kwargs):
#     print(args)
#     print(kwargs)

# test("Shifa", 18, city="Kozhikode")
# def welcome_decorator(fun):
#     def wrapper():
#         print("Welcome to Python!")
#         fun()
#         print("Enjoy learning!")
#     return wrapper()
# # @welcome_decorator
# def start_learning():
#     print("Let's learn decorators!")
# hello=welcome_decorator(start_learning)
# hello()
# def get_number():
#     return 100

# result = get_number()
# print(result)
# def calculte_discount(price,discount):
#     num=price*discount/100
#     final=price-num
#     return final
# result=calculte_discount(1000,10)
# print(result) 
# class Phone:
#     def call(self):
#         print("Making a normal call")

# def video_call(self):
#     print("Making a video call")
# Phone.call=video_call

# phone = Phone()
# phone.call()
# class Student:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return self.name

# student1 = Student("Shifa")

# print(student1)
# class product():
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def __str__(self):
#         return f"product:{self.name}|price:{self.price}"
# product1=product("laptop",30000)
# print(product1)
# import copy

# original = [[10, 20], [30, 40]]

# new = copy.deepcopy(original)
# new[0].append(999)

# print(original)
# print(new)
# x=[]
# print(type(x))
# hello="heeey"
# print(hello)

# hello = "Shifa"
# hello = 100
# print(hello)
# numbers = [10, 20, 30]
# numbers[0] = 100

# print(numbers)
# prices=1250
# Quantity = 4
# Discount = 15
# Deliverycharge = 100
# price=prices*Quantity
# print(price)
# dis=prices*Discount/100
# print(dis*4)
# print(price-dis*4)
# print()
# fin=price+Deliverycharge-dis*4
# print(fin)
# print(fin%500)
# print(fin**2)
# balance = 5000
# print(balance)
# balance+=1500
# print(balance)
# balance-=750
# print(balance)
# balance*=2
# print(balance)
# balance/=2
# print(balance)
# balance%=1000
# print(balance)
# student1 = 85
# student2 = 92
# print(student1>student2)
# print(student1<student2)
# print(student1==student2)
# print(student1!=student2)
# print(student1>=85)
# print(student2<=900)
# age = 20
# qualification = "BCA"
# training_completed = True
# ag=age>=18
# quali=qualification=="BCA" or qualification== "BSc"
# print(ag and quali and training_completed)
# print(ag or quali or training_completed)
# print(not(ag and quali and training_completed))
# skills = ["Python", "JavaScript", "React", "HTML", "CSS"]
# print("Python" in skills)
# print("Java" in skills)
# print("React" not in skills )
# print("CSS" in skills)
# a = [10, 20, 30]
# b = a
# c = [10, 20, 30]
# print(a is b)
# print(a is c)
# print(a==c)
# print(b is not c)
# num=int(input("enter a number : "))
# if num>100 or num<0:
#     print("not valid")
# elif num>=90:
#     print("A+")
# elif num>=80:
#     print("A")
# elif num>=70:
#     print("B")
# elif num>=60:
#     print("C")
# elif num>=50:
#     print("D")
# else:
#     print("FAIL")
# for i in range(1,11):
#     print(i)
# numbers = [1, 2, 3, 4]

# for num in numbers:
#     if num == 2:
#         numbers.remove(num)

# print(numbers)
# for i in range(5):
#     print(i)     # 0, 1, 2, 3, 4
# for a in range(1, 5):
#     print(a)  # 1, 2, 3, 4
# for i in range(10, 0, -2):
#     print(i)
# for i in []:
#     print(i)
# for num in [10, 20, 30]:
#     print(num)
# for i in range(1, 11):
#     print(i)
# for i in range(10, 0, -1):
#     print(i)
# for i in range(1,11):
#     print(f"7 *{i}={7*i}")
# total=0
# for i in range(1,11):
#     total+=i
# print(total)
# total=0
# i=1
# while i<=10:
#     total+=i
#     i+=1
# print(total)
# total=sum(range(1,11))
# print(total)
# numbers=[]
# for i in range(1,11):
#     numbers.append(i)
# print(sum(numbers))
# for i in range(2,21,2):
#     print(i)
count=0
# for i in range(2,21):
#     if i%2==0:
#         print(i)
#         count+=1
# print("total length =",count)
# total=1
# for i in range(6,0,-1):
#     total*=i
# print(f"factorial of 5 is {total}")
# text = "SHIFA"
# length=0
# for let in text:
#     length+=1

# print(f"total charector is: {length}")
# text = "PYTHON"
# rev=""
# for i in text:
#     rev=i+rev
# print(rev)
# numbers = [12, 45, 7, 89, 23, 56]
# lar=numbers[0]
# for num in numbers:
#     if num>lar:
#         lar=num
# print(f"the largest number is {lar}")
# numbers = [12, 45, 7, 89, 23, 56]
# lar=numbers[0]
# for num in numbers:
#     if num>lar:
#         lar=num
# print(f"largest number: {lar}")
# text = "programming"
# vovel=0
# texs="aeiou"
# for tex in text:
#     if tex in texs:
#         vovel+=1
# print(vovel)
# for i in range(1,6):
#     for a in range(i):
#         print("*",end="")
#     print()
# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()
# num=int(input("enter the number : "))
# prime=True
# if num<2:
#     prime=False
# for i in range(2,num):
#     if num%i==0:
#         prime=False
#         break
# if prime:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")
# num=int(input(" enter a number : "))
# prime=True
# if num<2:
#     prime=False
# for i in range(2,num):
#     if num%i==0:
#         prime=False
#         break
# if prime:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")
# for i in range(2, 11, 2):
#     print(i)
num = 5

# while num > 0:
#     print(num)
#     num -= 2
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)
# for i in range(1, 6):
#     if i == 4:
#         break
#     print(i)
# else:
#     print("Loop completed")
# for i in range(3):
#     for j in range(2):
#         print(i, j)
# for i in range(1, 6):
#     print(i)
# num = 1

# while num <= 5:
#     print(num)
#     num+=1
# for i in range(1, 6):
#     if i == 3:
#         print("Found")
# text = "SHIFA"
# hello=len(text)
# print(f"total charector: {hello}")
# text = "Hello Python"
# print(text.upper())
# print(text.lower())
# text = "welcome to python programming"
# print(text.capitalize())
# 
# print("Hi".center(8, "-"))
# print(	"Hi".ljust(5, "-"))
# product_name = "   miniature silver BUDDHA statue   "
# category = "SCULPTURES"
# description = "beautiful silver miniature statue for home decoration"
# product_code = "sculpt123"
# price = "2500"
# sentence = "python is powerful and python is easy"
# email = "admin@sivksculpt.com"
# filename = "SIVK_SCULPT_PRODUCT.txt"
# print(product_name.strip())
# print(product_name.lstrip())
# print(product_name.rstrip())
# print(product_name.upper())
# print(product_name.lower())
# print(product_name.capitalize())
# print(product_name.title())
# print(product_name.swapcase())
# print(description.replace("silver","premium silver"))
# print(sentence.index("python"))
# print(sentence.index("powerful"))
# print(description.count("python"))
# print(description.startswith("python"))
# print(description.endswith("easy"))
# print("silver" in description)
# print("gold" not in description)
# product_code = "sculpt123"
# price = "2500"
# category = "SCULPTURES"
# product_name = "   miniature silver BUDDHA statue   "
# hello="   "
# print(product_code.isalpha())
# print(price.isdigit())
# print(product_code.isalnum())
# print(category.isupper())
# print(product_name.istitle())
# print(hello.isspace())
# description = "beautiful silver miniature statue for home decoration"

# sentence = "python is powerful and python is easy"

# words1 = ["SIVK", "SCULPT", "PREMIUM"]

# words2 = ["Python", "String", "Methods"]
# print(description.split(" "))
# print(sentence.split("and"))
# print("-".join(words1))
# print(" ".join(words2))
# price = "2500"
# name = "SIVK"
# language = "PYTHON"
# print(price.zfill(8))
# print(name.center(20,"*"))
# print(language.ljust(15,"-"))
# print(language.rjust(15,'-'))
# filename = "SIVK_SCULPT_PRODUCT.txt"
# print(filename.removeprefix("SIVK_"))
# print(filename.removesuffix(".txt"))
# customer_name = "   sHiFa IsMaIl   "
# email = "SHIFA@SIVKSCULPT.COM"
# product = "silver miniature buddha statue"
# product_id = "sculpt2026"
# price = "4500"
# lowers=customer_name.lower()
# print(customer_name.strip())
# print(customer_name.capitalize())
# print(email.lower())
# print(email.endswith(".COM"))
# print("silver" in product)
# print(product.replace("silver","premium silver"))
# print(lowers.count("i"))
# print(product_id.isalnum())
# print(price.isdigit())
# words=product.split(" ")
# print(words)
# print("_".join(words))
# print(price.zfill(10))
    # a = [10, 20, 30, 20, 40]
# square=[]
# for i in range(1,6):
#     square.append(i*2)
# print(square)
# square=[num*2 for num in range(1,6)]
# print(square)
# numbers = [10, 20, 30, 40, 50]
# print(numbers[0])
# print(numbers[-1])
# print(numbers[::-1])
# numbers.insert(1,200)
# numbers.append(60)
# print(len(numbers))
# print(30 in numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# print(numbers)
# products = ["Buddha", "Ganesha", "Shiva"]
# products.append("krishna")
# products.extend(["lakshmi","saraswathi"])
# products.insert(1,"durga")
# products.remove("Ganesha")
# remo=products.pop()
# print(remo)
# print(products)
# print(products.index("Shiva"))
# print(products.count("Buddha"))
# products.clear()
# print(products)
# numbers = [40, 10, 30, 20, 50]
# numbers.sort()
# print(numbers)
# print(sorted(numbers,reverse=True))
# numbers.reverse()
# print(numbers)
# print(numbers.copy())
# copy=numbers[:]
# print(copy)
# a=[1,2,3]
# b=a
# b[0]=20
# print(a)
# print(b)
# c=[4,5,6]
# d=c.copy()
# d[1]=40
# print(d)
# print(c)
# numbers = [12, 45, 7, 89, 23, 56]
# max=numbers[0]
# small=numbers[0]
# sum=0
# len=0
# even=0
# odd=0
# evens=[]
# odds=[]

# for i in numbers:
#     if i>max:
#         max=i
#     elif i<small:
#         small=i
#     sum+=i
#     len+=1
#     if i%2==0:
#         even+=1
#         evens.append(i)
#     else:
#         odd+=1
#         odds.append(i)
   
# print(f"largest : {max}")
# print(f"smallest : {small}")
# print(sum)
# print(sum/len)
# print(f"even :{even}")
# print(f"odd: {odd}")
# print(evens)
# print(odds)
# numbers = [5, 10, 5, 20, 10, 5, 30, 20, 10]
# print(numbers.count(5))
# students = [
#     ["Shifa", 90],
#     ["Amina", 85],
#     ["Sara", 95]
# ]
# high=students[0][1]
# marks=[students[0][1],students[1][1],students[2][1]]
# print(students[0][1])
# print(students[2][0])
# sum=sum(student[1] for student in students)
# print(sum)
# len=len(students)
# print(sum/len)
# for student in students:
#     print(student[0],student[1])
#     if student[1]>high:
#         high=student[1]
#         print(f"{student[0]}-{student[1]}")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# squra=[number**2 for number in numbers if number%2==0]
# print(squra)
# numbers = [12, 45, 67, 23, 89, 34, 90]
# gr=[num for num in numbers if num>50]
# print(gr)
# names = ["shifa", "amina", "sara", "zoya"]
# upp=[name.upper()  for name in names]
# print(upp)
# numbers = [10, 20, 10, 30, 20, 40, 30, 50]
# nums=[]
# for i in numbers:
#     if i not in nums:
#         nums.append(i)
# print(nums)
# items = ["apple", "banana", "apple", "orange", "banana"]
# item=[]
# for i in items:
#     if i not in item:
#         item.append(i)
# print(item)
# list1 = [10, 20, 30]
# list2 = [40, 50, 60]
# # print(list1+list2)
# list1.extend(list2)
# print(list1)
# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 50, 60, 70]
# common=[num for num in list1 if num in list2]
# print(common)
# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 50, 60, 70]
# notin=[num for num in list1 if num not in list2]
# print(notin)
# nested = [[1, 2], [3, 4], [5, 6]]
# # flat=[]
# # for num in nested:
# #     for i in num:
# #         flat.append(i)
# flat=[i for num in nested for i in num]
# print(flat)
# numbers = [10, 20, 30, 40, 50]
# numbers=numbers[-1:]+numbers[0:4]
# print(numbers)
list1 = [10, 20, 20, 30, 40, 40, 50]
list2 = [20, 20, 40, 50, 60]
comn=[]
for num in list2:
    if num in list1 and num not in comn:
        comn.append(num)
print(comn)