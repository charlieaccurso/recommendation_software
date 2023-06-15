from restaurantData import types, restaurant_data

def welcome():
    print("Welcome to Restaurant Navigator!")

def get_user_input():
    user_input= input("Please type the first few letters of the type of food you're interested in:\n> ")
    return user_input

def match_type(user_input):
    matches = []

    for type in types:
        if type.startswith(user_input):
            matches.append(type)

    return matches

def verify_match(matches):
    if len(matches) > 1:
        print(f"We found the following matches: {matches}")
        user_input= input("Please type the one you want:\n>")
        if user_input in matches:
            return user_input
        else:
            return verify_match(matches)
        
    return matches[0]

def show_restaurants(match):
    for restaurant in restaurant_data:
        if restaurant[0] == match:
            print("================================")
            print(f"Type: {restaurant[0]}")
            print(f"Name: {restaurant[1]}")
            print(f"Average rating: {(float(restaurant[2]) + float(restaurant[3])) / 2}")
            print(f"Address: {restaurant[4]}")
            print("================================")
    
    user_input= again()
    if user_input == 'y':
        get_user_input()
    else:
        goodbye()

def again():
    print("Would you like to search for a different type of restaurant?")
    user_input= input("Enter y/n:\n> ")
    return user_input

def goodbye():
    print("Thank you for using Restaurant Navigator!")

def main():
    welcome()
    user_input= get_user_input()
    matches= match_type(user_input)
    match= verify_match(matches)
    show_restaurants(match)
