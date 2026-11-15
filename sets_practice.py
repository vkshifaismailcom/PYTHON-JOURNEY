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
employees = [
    {"name": "Shifa", "salary": 25000},
    {"name": "Amina", "salary": 40000},
    {"name": "Sara", "salary": 30000}
]
sorting=sorted(employees,key=lambda employee:employee["salary"],reverse=True)
print(sorting)