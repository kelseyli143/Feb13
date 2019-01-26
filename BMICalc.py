#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Receives input from the user from the console

#Console input can be received with code such as follows:
#x = input("Enter number: ")
#Note that x will be a string and needs to be converted to a float.
#Weight input must be in pounds
#Height input must be in inches
# BMI	Weight Status
# Below 18.5	Underweight
# 18.5 – 24.9	Normal
# 25.0 – 29.9	Overweight
# 30.0 and Above	Obese
# BMI = (Weight in Pounds / (Height in inches) x (Height in inches)) x 703
#Program must output to the console the calculated BMI.

#Console output can be achieved by code such as: print("The number entered was {}".format(x))
#Program must output whether the calculated BMI represents underweight, normal weight, overweight, or obese.

#Extra credit: give the user the option to enter weight in kilograms and height in meters.


# In[3]:


height_str = input("Enter height in inches:")
weight_str = input("Enter weight in pounds:")
height = float(height_str)
weight = float(weight_str)
# %whos


# In[4]:


BMI = (weight/height**2)*703
print("The corresponding BMI is",BMI)


# In[5]:


if BMI<18.5:
    status = 'underweight'
elif BMI>=18.5 and BMI<=24.9:
    status = 'normal weight'
elif BMI>=25 and BMI<=29.9:
    status = 'overweight'
else:
    status = 'obese'
print("This BME is categorized as",status)


# In[ ]:




