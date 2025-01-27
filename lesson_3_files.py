#Чтение файла
# !!! Можно открыть только существующий файл !!!

myfile = open("myfile.txt", "r", encoding="utf-8")
text = myfile.read()
myfile.close()

print(text)
print(len(text))
print(text.splitlines())
print(len(text.splitlines()))