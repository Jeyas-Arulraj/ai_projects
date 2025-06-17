class multi_fun():
    # Define the function to display subfields
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")

    
    # Define the function to display subfields
    def OddEven():
        num =int(input("Enter the number:"))
        if((num%2) == 0):
            print("It is a even number")
            message=f"{num} is Even number"
        else:
            print("It is a odd number")
            message=f"{num} is Odd number"
        return message


    # Define the function
    def Elegible():
        gender = input("Your Gender (Male/Female): ").strip().capitalize()
        age = int(input("Your Age: "))
    
        if gender == "Male":
            if age >= 21:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif gender == "Female":
            if age >= 18:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            print("Invalid gender input. Please enter 'Male' or 'Female'.")


    def percentage():
        # Marks for each subject
        subject1 = 98
        subject2 = 87
        subject3 = 95
        subject4 = 95
        subject5 = 93
    
        # Calculate total
        total = subject1 + subject2 + subject3 + subject4 + subject5
    
        # Calculate percentage
        percentage = (total / 500) * 100  # assuming each subject is out of 100
    
        # Print the results
        print("Subject1 =", subject1)
        print("Subject2 =", subject2)
        print("Subject3 =", subject3)
        print("Subject4 =", subject4)
        print("Subject5 =", subject5)
        print("Total :", total)
        print("Percentage :", percentage)


    def triangle():
        # Area calculation
        height = 32
        breadth = 34
        area = (height * breadth) / 2
        print("Height:", height)
        print("Breadth:", breadth)
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", area)
    
        # Perimeter calculation
        height1 = 2
        height2 = 4
        breadth = 4
        perimeter = height1 + height2 + breadth
        print("Height1:", height1)
        print("Height2:", height2)
        print("Breadth:", breadth)
        print("Perimeter formula: Height1 + Height2 + Breadth")
        print("Perimeter of Triangle:", perimeter)

