# products = {"book", "pen", "eraser", "sharpner",
#  "paper"}
# products = ["Sculpture", "Painting", "Sculpture", "Figurine", "Painting"]
# print(set(products))
# fruits={"apple","orange","banana"}
# fruits.add("berry")
# fruits.update(["mango","strawberry","guava"])
# print(fruits)
languages = {"Python", "Java", "JavaScript", "C++", "Ruby"}
languages.discard("Java")
print(languages)
languages.discard("Ruby")
print(languages)
removes=languages.pop()
print(removes)
languages.clear()
print(languages)