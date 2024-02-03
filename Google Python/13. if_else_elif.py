# Video 27

def hint_username(name):
    if len(name)<3:
        print("Invelid username. Username should be at least 3 characters")
    elif len(name)>15:
        print("Username should not exceed 15 characters")
    else:
        print("Valid username entered.")

hint_username("Marion")