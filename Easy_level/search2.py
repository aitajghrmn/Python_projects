users = [
    {"name": "Ali", "age": 20},
    {"name": "Veli", "age": 25},
    {"name": "Aytac", "age": 21},
    {"name": "Murad", "age": 30}
]

agely=int(input("Enter age: "))
found= False

for u in users:
    if u["age"] == agely :
        print(u["name"])
        found=True

if not found :
    print("User not found")
