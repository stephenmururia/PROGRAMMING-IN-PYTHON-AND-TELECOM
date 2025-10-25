#Simple Voter Eligibility Checker

country = input("Enter your country of citizenship: ").strip().lower()

if country in ['kenya', 'uganda', 'tanzania']:
    age = int(input("Enter your age: "))
    
    if age >= 18:
        passport = input("Enter your passport number (8 digits): ").strip()
        
        if passport.isdigit() and len(passport) == 8:
            print("You are eligible to vote.")
        else:
            print("Invalid passport number. It must be exactly 8 digits.")
    else:
        print("You must be at least 18 years old to vote.")
else:
    print("Only citizens of East Africa can vote.")
