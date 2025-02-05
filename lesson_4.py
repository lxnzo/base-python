def get_sum_numbers(num_1=0, num_2=0):
    return num_1 + num_2

def get_first_last_char(text):
    first = text[0]
    last = text[-1]
    second = text[1]

    return [first, last, second]

a,b,c = get_first_last_char(text="python")


def get_max_value(numbers):
    min_val = numbers[0]
    for i in numbers:
        if i > min_val:
            min_val = i
    return min_val

def get_sum_even_numbers(numbers):
    sum_ = 0
    for i in numbers:
        if i % 2 == 0:
            sum_ += i
    return sum_

def get_clean_words(text):
    text = text.replace(',', ' ').replace('-', ' ').lower().split()
    return text



text = "I,Love - Python"
new_list = get_clean_words(text)
print(new_list)

# new_list = list(map(lambda x: x.lower(), text))

def hello():
    print("hello")

def square(x):
    return x*x

def sum_sum(a, b):
    return a + b

sum_ = lambda x,y: x+y
print(sum_(2,3))

square_ = lambda x: x*x
print(square_(2))

message = lambda: print("hello")

