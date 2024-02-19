import re

def replace_digits(text):
    pattern = r'\b\d{7,}\b'
    result = re.sub(pattern, lambda x: x.group()[:-3] + '*' * 3, text)
    return result

text = input("text : ")

hasil = replace_digits(text)
print("hasil : " + hasil)