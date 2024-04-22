import random
password = "ASDFGHJKLQWERTYUIOPZXCVBNMasdfghjklqwertyuiopzxcvbnm1234567890"
length_of_password = int(input("Enter the length of the password: "))
a = "".join(random.sample(password,length_of_password))
print(f"Your password is {a}")