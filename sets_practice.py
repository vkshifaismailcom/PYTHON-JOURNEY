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
def calculate_area():
    length=10
    width=5
    return length*width


total=calculate_area()
print(total)