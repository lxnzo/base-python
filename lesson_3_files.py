#Чтение файла
# !!! Можно открыть только существующий файл !!!
from os import write

myfile = open("myfile.txt", "r", encoding="utf-8")
text = myfile.read()
myfile.close()

print(text)
print(len(text))
print(text.splitlines())
print(len(text.splitlines()))


new_file = open("new_file.txt", "w", encoding="utf-8")
text = "I Love Python!"
new_file.write(text)
new_file.write("Python Forever!!!\n")

names = ["Masha", "Sasha", "Ivan"]
for word in names:
    new_file.write(word+'\n')

names_string = "\n".join(names)
new_file,write(names_string+'\n')

new_file.close()

new_file = open("new_file.txt", "a", encoding="utf-8")
new_file.write("\nNEW TEXT")
new_file.close()

