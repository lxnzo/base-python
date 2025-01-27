# mnojestva  - set() - {}

# sozdanie mnojestva pri pomoshi literalov
set_of_numbers = {1,2,2,2,3,4}
print(type(set_of_numbers))
print(set_of_numbers)

names = ['Ivan', 'Maria', 'Ivan']
print(set(names))

#sozdanie mnojestva pri pomoshi function set
set_of_names = set(['Ivan', 'Maria', 'Ivan'])
print(set_of_names)

print(len(set_of_names))

#dobavlenie elementa vo mnojestvo
set_of_names.add('Dima')
print(set_of_names)

#udalenie elemeta
# in - operator, kotoriy proveryaet vhojdenie elementa v collection
if "Dima2" in set_of_names
    set_of_names.remove("Dima")
else:
    print("Takogo elementa net")

set_of_names.discard("Dima2")
print(set_of_names)
