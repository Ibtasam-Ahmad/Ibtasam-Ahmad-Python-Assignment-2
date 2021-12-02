#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Make a calculator using python with addition, substraction,
#multipllication, division and power

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.power")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4' ,'5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "pow", num2, "=", pow(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


# In[2]:


#write a program to check if there is any numaric value
# in list using for loop

squares = {1: 1, 2: 4, 3: 9}
squares['x'] = None # Adding new key without value
print(squares)


# In[3]:


#python script to add a key to a dictionary

# Initializing list
test_list = [ 1, 6, 3, 5, 3, 4 ]
 
print("Checking if 4 exists in list ( using loop ) : ")
 
# Checking if 4 exists in list
# using loop
for i in test_list:
    if(i == 4) :
        print ("Element Exists")
 
print("Checking if 4 exists in list ( using in ) : ")
 
# Checking if 4 exists in list
# using in
if (4 in test_list):
    print ("Element Exists")


# In[12]:


#python program to sum all the numaric items in a dictionary

my_dict = {'data1':100,'data2':-50,'data3':250}
print(sum(my_dict.values()))


# In[4]:


#program to identify duplicate values from list

l=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')


# In[22]:


#python script to check if a given key already exists in a dictionary

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(1)
is_key_present(0)

