def calculate_sum(a, b):
    return a + b

def concat_strings(str):
    index = 0
    while index < 10:
        str += index.__str__() + " "
        index += 1
    return str

print(calculate_sum(3, 5))
print(concat_strings(""))