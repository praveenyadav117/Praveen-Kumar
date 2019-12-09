#!/usr/bin/env python
# coding: utf-8

# In[1]:


#task 1 problem 1,2
c = 2000
while c<=3200 :
    if c%7==0 and c%5!=0 :
        print(c)
        print(',')
    c += 1

    


# In[ ]:


#task 1 problem 3
first_name = input('Enter your first name  ')
print('your first name is',first_name)

last_name = input('Enter your last name  ')
print('your last name is',last_name)

f = first_name[::-1]
l = last_name[::-1]


print(f,' ',l)


# In[ ]:


#task 1 problem 4
r = 2
pi=3.14
volume = 4/3*pi*r*r
print(volume)


# In[ ]:


#TAsk 2 problem 1
numbers = list(input('enters the numbers how amny you want' ))

type(numbers)
numbers


# In[ ]:


#task 2 problem 2
forloop = "*****"
x = 0
for j in forloop:
    x = x +1
    print(forloop[0:x])

for j in forloop:
    x = x - 1
    print(forloop[0:x])


# In[ ]:


#task 2 problem 3
word = input('Enter your word')
print(word[::-1])


# In[ ]:


# task 2 problem 4
my_string = input('Enter your string ')
my_string
print('WE, THE PEOPLE OF INDIA,\n having solemnly resolved to constitute India into a SOVEREIGN,!\n SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n and to secure to all its citizens')

