#spiski
names = []

#dobavlenie elementa v konec spiska
names.append(2)
names.append("Alex")
my_name = "Elena"
names.append(my_name)

#poluchit element spiska (s udaleniem ego iz spiska)
last_name = names.pop(0)
print(last_name)
print(names)

#pochet kol-va elementa v spiske
print(names.count("Alex"))

names.append("Alex")
print(names)
ind = names.index("Alex")
print(ind)

#dobavlenie elementa d proizovol mesto spiska
names.insert(0, "Masha")
print(names)

#udalenie elementa iz spiska
names.remove("Alex")
print(names)

#kol-vo elementov v spiska
print(len(names))

#poluchenie elementov spiska\
print(names[0])
print(names[-1]) #posledniy
print(names[-2]) #predoposledniy

#srezi spiska
names.extend(["Dima", "Vova", "Sergey"])

print(names[0:2]) # ot 0 do 2 (kraynyaya granica ne vivoditsya

print(names[0:]) # ot 0 do konca

print(names[0:1:4])

#cikl For
#prohod po elementam kolekcii
for i in names:
    print(i)

#range(6) = (0, 1, 2, 3, 4, 5)
#range(1,5) = (1, 2, 3, 4)
for i in range(6):
    print(i)

for i in range(len(names)):
    print(names[i])

    for i in range(len(names)):
        print(f"{i+1}.{names[i]}")

a = 10

while a > 0:
    print("Hello")
    a -= 4
    if a == 4:
        break

print("Выберите действие: ")
print("1. Добавить книгу")
print("2. Удалить книгу")
print("Введите 0 для выхода из меню")

action = inpuy (">>> ")
if action == "1":
    print("Книга добавлена")
if action == "2":
    print("Книга удаленна")
if action == "0"
    print("До свидания")
    break

print(names)
names += ["Nastya"]
print(names)

#for i in range (1, 10):
#   print(i)

#kortej
#tuple

numbers = (1,2,3,4)
status = (
    ("in_process", "В работе"),
    ("success", "Выполено")
)

#slovar'
print("Hello")
person = {}
info = {"name": "Dima", "age": 26}

#poluchenie elementa slovarya
name = info("name")
print(info["name"])

print(info)



#razmerslovorya

print(len(info))
info["lang"] = ["russian", "english"]
print(info)
info["edu"] = {"hight": "MGU", "medium": "ITMO"}
print(info)

#ключом словаря может быть только неизменяемый тип данных(строка, число, кортеж)
cars = {("bmw", "audi"): "germany"}

age = info.pop("age")
print(age)
print(info)

#print(info["age"])
print(info.get("edu", "err").get("hight2",{}))

print(info)

info_copy