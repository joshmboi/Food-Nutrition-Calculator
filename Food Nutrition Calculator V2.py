import time
import numpy as np

#calories, carbs, protein, total_fat, sat_fat, trans_fat, sodium, sugar, fiber
meal_stats = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0]).astype(float)
#above is a global list that still has all of the same stats, ill be using this array to add with the arrays you created down below
#the reason i create a global variable is so that it does not reset in each function i use it in
#before the overall nutritional facts changes with each burger or fries i ordered

def print_message(string):  # Delays each print statement by .7 seconds.
    # Parameter is any string.
    print(string)
    time.sleep(.7)


def intro():
    restaurant = input('\nOut of ChickfilA, Chipotle, FiveGuys, and Fuddruckers, where are you eating today?:\n')
    if 'five' in restaurant:
        print_message("\nFiveGuys, that's tuff.")
        fiveguys()
    elif 'chick' in restaurant:
        print_message("\nChick-Fil-A, that's tuff.")
    elif 'chipotle' in restaurant:
        print_message("\nChipotle, that's tuff.")
    elif 'fud' in restaurant:
        print_message("\nFuddruckers, that's tuff.")
    else:
        print_message("Learn to spell, holy shit. Try again.")
        intro()

def repeat():  #How can I generalize this function so it can repeat for any restaurant?
    while True:
        more_food = input('\nAre you eating more food?  Please type yes or no: \n').lower()
        if more_food == 'yes':
            print_message("Christ you fatass, alright.")
            fiveguys()
        elif more_food == 'no':
            print_message("\nThank god, go exercise.")
            break
        else:
            print_message("\nDidn't get that, try again.")

def fiveguys():
    #burger: hamburger, cheeseburger, baconburger, baconcheeseburger - fries: small, medium, large
    fiveguys_menu = np.array([[(700, 39, 39, 43, 19.5, 2, 430, 8, 2), (770, 39, 43, 49, 23.5, 2.2, 790, 8, 2), (780, 39, 43, 50, 22, 2, 690, 8, 2), (850, 39, 47, 56, 26.5, 2.2, 1050, 8, 2)], [(526, 72, 8, 23, 4, .5, 531, 2, 8), (953, 131, 15, 41, 7, 1, 962, 4, 15), (1314, 181, 20, 57, 10, 1, 1327, 6, 20)]])
    #above i looked up how to create a 3d array in numpy, since that was the array you were using, i just followed the guide they had
    fiveguys_dict = {'burger': 0, 'hamburger': 0, 'cheeseburger': 1, 'baconburger': 2, 'baconcheeseburger': 3, 'fries': 1, 'Small': 0, 'Medium': 1, 'Large': 2}
    #above is a dictionary, i can assign values of any type to keys, i use this to bypass the use of numbers down below when adding to meal_stats
    fries_dict = {'small': 'Small', 'medium': 'Medium', 'large': 'Large', 'smallfries': 'Small', 'mediumfries': 'Medium', 'largefries': 'Large'}
    #above is another dictionary, it converts the two ways one would type fries_type into a uniform string, this is useful for condensing a lot of possible answers
    while True:
        global meal_stats
        #above i am referencing the meal_stats global variable to be able to make edits to it
        food = input("\nWhat're you tryna eat?  Please state whether you want a burger or fries, f a t t y:\n").lower().replace(" ", "")
        if 'burger' in food:
            while True:
                burger_type = input('\nOut of a hamburger, cheeseburger, baconburger, and bacon cheeseburger, which one do you want?:\n').lower().replace(" ", "")
                if burger_type in ['hamburger', 'cheeseburger', 'baconburger', 'baconcheeseburger']:
                    #above, instead of having an if statement for each burger, i created one if statement to detect any burger, due to code below, i get this flexibility
                    print_message("\nMhm, delicious.")
                    meal_stats += fiveguys_menu[fiveguys_dict[food]][fiveguys_dict[burger_type]]
                    #above is the statement that allows a lot of condensing, since i can add arrays using numpy, it condenses adding each element of each array
                    break
                else:
                    print_message('Didn\'t understand, try again.')
                    continue
        elif 'fries' in food:
            while True:
                fries_type = input('\nOut of small, regular, and large, what size fries do you want?:\n').lower().replace(" ", "")
                if fries_type in ['small', 'medium', 'large', 'smallfries', 'mediumfries', 'largefries']:
                    #above is the same as before
                    meal_stats += fiveguys_menu[fiveguys_dict[food]][fiveguys_dict[fries_dict[fries_type]]]
                    #above is the same as before
                    print_message(f"\n{fries_dict[fries_type]} fries coming up.\n")
                    #above, because i created the fries_dict dictionary, i can use that dictionary to enter the type of fries into the fstring
                    break
                else:
                    print_message('Didn\'t understand, try again.')
                    continue
        else:
            print_message("Try again.")
            fiveguys()
        toppings(food)
        #i generalize the toppings statement, this allows me to move the toppings outside of either burger or fries
        print_message("Calculating nutritional info...\n\n")
        print_message("So ...\n\n")
        print_message("Much ...\n\n")
        print_message("Obesity!!!!!\n\n ")
        print_message(f"\n\nYour meal contains:\n{meal_stats[0]} calories \n{meal_stats[1]} grams of carbs \n{meal_stats[2]} grams of protein \n{meal_stats[3]} grams of total fat \n{meal_stats[4]} grams of saturated fat \n{meal_stats[5]} grams of trans fat \n{meal_stats[6]} milligrams of sodium \n{meal_stats[7]} grams of sugar \n{meal_stats[8]} grams of fiber\n")
        print_message("Whew! That's a lot of calories.")
        #remove this from function, add it after intro at the bottom
        break

def toppings(food):
    #i condensed both fb_toppings and ff_toppings
    #A1 Sauce, barbeque, green peppers, grilled mushrooms, hot sauce, jalapenos, ketchup, lettuce, mayo, mustard, onions, pickles, relish, tomatoes
    fiveguys_toppings = np.array([(15, 3, 0, 0, 0,0, 280, 2, 0), (60, 15, 0, 0, 0, 0, 400, 10, 0), (5, 1, 0, 0, 0, 0, 1, 0, 0), (5, 1, 0, 0, 0, 0, 55, 1, 0), (0, 0, 0, 0, 0, 0, 200, 0, 0), (3, 0, 0, 0, 0, 0, 0, 0, 0), (20, 5, 0, 0, 0, 0, 160, 4, 0), (4, 1, 0, 0, 0, 0, 3, 0, 0), (100, 0, 0, 11, 2, 0, 75, 0, 0), (0, 0, 0, 0, 0, 0, 55, 0, 0), (10, 2, 0, 0, 0, 0, 1, 1, 0), (3, 1, 0, 0, 0, 0, 0, 0, 0), (10 , 3, 0, 0, 0, 0, 105, 3, 0), (9, 2, 0, 0, 0, 0, 3, 1, 0)])
    #above i moved the fiveguys_toppings into here because this is the only place it is useful, therefore i dont have to pass it as an arg
    toppings_list = ['A1 Sauce', 'barbeque', 'green pepper', 'grilled mushrooms', 'hot sauce', 'jalapenos', 'ketchup', 'lettuce', 'mayo', 'mustard', 'onions', 'pickles', 'relish', 'tomatoes']
    ff_list = ['barbeque', 'hot sauce', 'ketchup', 'mayo', 'mustard']
    your_fb_toppings = []
    your_ff_toppings = []
    global meal_stats
    toppings_dict = {'A1 Sauce': 0, 'barbeque': 1, 'green peppers': 2, 'grilled mushrooms': 3, 'hot sauce': 4, 'jalapenos': 5, 'ketchup': 6, 'lettuce': 7, 'mayo': 8, 'mustard': 9, 'onions': 10, 'pickles': 11, 'relish': 12, 'tomatoes': 13}
    #above is the dictionary i use to map the toppings to numbers for the arrays
    if 'burger' in food:
        while True:
            burger_toppings = input(f"\nThe toppings available are:\n\n{toppings_list}\n\nWhat toppings do you want? Please be specific to the spelling listed. \nIf you don't want toppings or are finished, leave the response blank and presss enter:\n\n")
            if not burger_toppings:
                return
            elif burger_toppings not in toppings_list and (burger_toppings in fiveguys_toppings):
                print_message('\nYou already added that topping in your burger.')
                continue
            elif burger_toppings not in toppings_list:
                print_message(f"\n{burger_toppings.capitalize()} is not one of the options!")
                continue
            meal_stats += fiveguys_toppings[toppings_dict[burger_toppings]]
            #above is the same as before
            toppings_list.remove(burger_toppings)
            your_fb_toppings.append(burger_toppings)
            print_message(f'\nIn your burger, you have {your_fb_toppings}.')
    elif 'fries' in food:
        while True:
            fries_sauce = input(f"\nThe toppings available are:\n\n{ff_list}\n\nWhat sauces do you want? Please be specific to the spelling listed. \nIf you don't want sauces or are finished, leave the response blank and press enter: \n\n")
            if not fries_sauce:
                return
            elif fries_sauce in fiveguys_toppings and fries_sauce not in ff_list:
                print_message('\nYou already added that topping in your burger.')
                continue
            elif fries_sauce not in ff_list:
                print(f"\n{fries_sauce.capitalize()} is not one of the options!")
                continue
            meal_stats += fiveguys_toppings[toppings_dict[fries_sauce]]
            #above is the same as before
            ff_list.remove(fries_sauce)
            your_ff_toppings.append(fries_sauce)
            print_message(f'\nFor your fries, you have {your_ff_toppings}')

print_message("\nWhat's up fatass!")
print_message("\nYou ready to grub you pig?!")
intro()
repeat()
