#task 3............accept
import random
import string

pass_len = int(input("enter length of your Password : "))
charValues = string.ascii_letters + string.digits + string.punctuation 

password = ""

#list comprehension Method
password = "".join(random.choice(charValues) for i in range(pass_len))
print("Your Strongest Password is  =", password)