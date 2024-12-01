def calculate_age():
    import datetime
    current_year = datetime.datetime.now().year

    try:
        birth_year = int(input("Please enter your birth year: "))
        age = current_year - birth_year
        
        if age < 0:
            print("The age entered is wrong.")
        else:
            print(f"You are {age} years old.")
    except ValueError:
        print("The age entered is wrong.")

calculate_age()
