users = [
    {"name": "Ali", "age": 20},
    {"name": "Veli", "age": 25},
    {"name": "Aytac", "age": 21}
]

search_name = input("Enter name: ")
found=False

for u in users:
    if search_name == u["name"]:
        print(u)
        found=True
        break
    

if found == False:
    print("User not found")
