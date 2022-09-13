#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# print(len(letters))
my_string = []
my_strin = []
my = []
for number in range(1,nr_letters + 1):
   x = letters[random.randint(0,51)]
   my_string += x
# print(my_string)
for integer in range(1,nr_symbols + 1):
  y = numbers[random.randint(0,9)]
  my_strin += y
for symbol in range(1,nr_numbers + 1):
  z = symbols[random.randint(0,8)]
  my += z
 
shuffle_me = my_string + my_strin + my
print(shuffle_me)
random.shuffle(shuffle_me)
print(shuffle_me)
password = ""
for char in shuffle_me:
  password += char
print(f"Your password is {password}")