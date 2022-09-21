import random, string

def generate(lenth_of_password):
    
    password_string = string.ascii_letters + string.digits + string.punctuation


    return ''.join(random.sample(password_string, k=lenth_of_password))

lenth_of_password = int(input())
generate(lenth_of_password)