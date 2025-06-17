class multipleFunction():
    def oddEven():
        #odd or even calculation
        num =int(input("Enter the number:"))
        if((num%2) == 0):
            print("It is a even number")
            message="Even number"
        else:
            print("It is a odd number")
            message="Odd number"
        return message
        
    def BMI():
        bmi=int(input("Enter the BMI Index:"))
        if(bmi < 16):
            print("Severely Underweight")
            message="Severely Underweight"
        elif(bmi < 18.5):    
            print ("Underweight")
            message="Underweight"
        elif(bmi < 25) :
            print("Normal")
            message="Normal"
        elif(bmi < 30):
            print("Overweight")
            message="Overweight"
        elif(bmi < 35):
            print("very Overweight")
            message="very Overweight"
        elif(bmi < 40):
            print("Severely Obese")
            message="Severely Obese"
        else:
            print("Morbidly Obese")
            message="Morbidly Obese"
        return message    