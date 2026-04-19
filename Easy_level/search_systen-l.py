users = [
    {"name": "Ali", "age": 20},
    {"name": "Veli", "age": 25},
    {"name": "Aytac", "age": 21},
    {"name": "Murad", "age": 30}
]

namely = input("Enter your name: ")
agely = int(input("Enter your age: "))
found = False

for u in users:
    if u["name"] == namely and u["age"] >= agely:
        print(u["name"], u["age"])
        found = True

if not found:
    print("The User not found")
