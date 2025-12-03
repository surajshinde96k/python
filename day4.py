# dictionary={
#     "cat" : "a small domesticated carnivorous mammal",
#     "table" : ["a wood", "a plastic"]
# }

# print(dictionary)

# ....................................................................................................

# set = { "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
# print(len(set))
# print(set)


# ....................................................................................................

marks = {}
x = int(input("enter phy: "))
marks.update({"phy" : x})

x = int(input("enter math : "))
marks.update({"math": x})

x = int(input("enter chem: "))
marks.update({"chem" : x})

print(marks)