#program that creates a random password of 18 characters with a mix of upper and lower case letters, numbers and symbols
import random
import string

def random_password():
    password = ''
    for i in range(18):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password

print(random_password())