import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
def listtostring(output):
    storage = " "
    return storage.join(output)

password_lenght = int(input(f'Your Password length: '))
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
output = random.sample(s,password_lenght)

print(listtostring(output))
