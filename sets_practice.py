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
student = {
    "name": "Shifa",
    "age": 18
}
student.update({"age":30,
"course":"fullstack"})
print(student["name"])
print(student)