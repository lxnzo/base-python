a = 5
b = 6
# a = 24
# fbfbgff

print(a)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a**b)
print(a%2)
print("Hello")
print('Hi')
print(f"Hello. a = {a}")
print(f"Hello. a+b = {a+b}")


c = 5.7
c = 7.0
print(type(a))
print(type(c))
print(type(a+c))
#boolean
print(7>10)
print(7<10)
print(7>=10)
print(7<=10)
print(7==10)
print(7!=10)
#string
last_name = ("Ivanov"
             "dsfsdfsf"
             "dfewfdf")
text = """
sdffsdfd
fdsfsdsd
fsdfsdfs
"""
city = "Moscow\ncity"
print(city)
#list
numbers = []
new_numbers = [1,2,3]
elements = [1, '2', 'name', True, [1,2,3]]
print(elements)
#кортеж
colors = tuple()
new_colors = ("red", "blue", "green")
#словарь
car = {}
my_car = dict()

#ключ   значение   ключ   значение
info = {"name": "Misha",
        "age": 26,
        "city": "Moscow",
        25: 46,
        ("1", 2, 3): 24
        }
print(info)


#set
set_of_names = {"Masha", "Sasha", "Dima", "Masha"}
print(type(set_of_names))
print(set_of_names)

cars = ['bmw', 'audi', 'bmw', 'bmw']
# list -> set
print(list(set(cars)))
txt = "Hello"
print(set(txt))

#if - elif - else
age = 0
if (age < 11 and age !=0):
    print("error")
elif age == 0:
    print("age == 0")
else:
    print("ok")

in_name = input("Введите ваше имя: ")
in_age = input("Введите ваш возраст: ")

print(f"Ваше имя - {in_name}")
print(f"Ваше возраст - {in_age}")
print(type(in_age))

print(12 == int(in_age))