# Kelsey Li
# BME547
# BMI Calculator


# main function that calls all other functions
def main():
    units = BMI_units()
    
    BMI = BMI_calc(units)
    
    BMI_status(BMI)
    
# first allow user to choose their unit system
def BMI_units():
    units = input("Would you like to use imperial or metric units? Enter either imperial or metric: ")
    return units #saves units as the results of this function

def BMI_calc(units):
    if units == "imperial":
        height_str = input("Enter height in inches: ")
        weight_str = input("Enter weight in pounds: ")
        
        # float converts the string inputs to floats for calculation
        height = float(height_str)
        weight = float(weight_str)
        
        #BMI calculation with conversion factor for imperial units
        BMI = (weight/height**2)*703
     
    if units == "metric":
        height_str = input("Enter height in meters: ")
        weight_str = input("Enter weight in kilograms: ")
        
        # float converts the string inputs to floats for calculation
        height = float(height_str)
        weight = float(weight_str)
        
        # BMI calculation for metric units
        BMI = weight/height**2
    
    print("The corresponding BMI is {}.".format(BMI))  
   
    # saves BMI as output of BMI calculation
    return BMI

#if statement depending on BMI value to determine BMI status
def BMI_status(BMI):
    if BMI<18.5:
        status = 'underweight'
    elif BMI>=18.5 and BMI<=24.9:
        status = 'normal weight'
    elif BMI>=25 and BMI<=29.9:
        status = 'overweight'
    else:
        status = 'obese'
    print("This BME is categorized as {}.".format(status))
    
if __name__ == "__main__": 
# double underscore means it's an internal Python variable
    main()
