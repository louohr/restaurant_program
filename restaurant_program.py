# Assignment A_7 Restaurant program made in the Test Automation course at Frans Schartaus Business Institute
# This is a restaurant program where the user can book a table, see the food menu, leave a review and show the booking
# I added some more code to make changes to the booking like change time, number of people and cancel booking
# Date: 2022-02 updated: 2023-01-29/30

# the lists that will be used
booking_list: list = []
review_list: list = []


# defining all the menu options that you can choose
def menu_options():
    option = input("Welcome to the best restaurant in the world! "
                   "\nWhat would you like to do? \n1. Book a table \n2. Show menu \n3. Leave review \n4. Show booking "
                   "\n5. Exit")
    if option == "1":
        book_table()
    if option == "2":
        show_food_menu()
    if option == "3":
        leave_review()
    if option == "4":
        show_booking_list()
    if option == "5":
        print("Please come back again!")
        quit()

    menu_options()


# asking the user to book a table
def book_table():
    quantity = input("How many people will you be?")
    booking_list.append(quantity)
    time = input("What time will you be here?")
    booking_list.append(time)
    comment = input("Any extra comment?")
    booking_list.append(comment)
    if len(comment) > 0:
        print(f"Your reservation is confirmed for {quantity} people with arrival time at {time}. "
              f"Additional information: {comment}")
    options = input(f"Would you like to see the menu options again?")
    if options == "yes":
        menu_options()
    else:
        print("Thank you. Please come by again!")
        quit()


# show booking to make changes
def show_booking_list():
    print(booking_list)
    option = input("What would you like to do? \n1. Change the reservation \n2. Cancel your reservation \n3. Go back "
                   "to menu options")
    if option == "1":
        change_reservation()
    if option == "2":
        cancel_reservation()
    if option == "3":
        menu_options()


# change reservation, time, number of people, comment
def change_reservation():
    option = input(
        "What do you want to change? \n1. Time \n2. Number of people \n3. Comment \n4. Go back to menu options")
    if option == "1":
        change_time()
    if option == "2":
        change_number_of_people()
    if option == "3":
        change_comment()
    if option == "4":
        menu_options()


# change arrival time
def change_time():
    time = input("What time will you be here?")
    booking_list.append(time)
    print(f"Your change is confirmed for {time}.")
    options = input(f"Would you like to see the menu options again?")
    if options == "yes":
        menu_options()
    else:
        print("Thank you. Please come by again!")
        quit()


# change how many you will be
def change_number_of_people():
    quantity = input("How many people will you be?")
    booking_list.append(quantity)
    print(f"Your change is confirmed for {quantity}")
    options = input(f"Would you like to see the menu options again?")
    if options == "yes":
        menu_options()
    else:
        print("Thank you. Please come by again!")
        quit()


# change additional information
def change_comment():
    comment = input("What information do you want to add?")
    booking_list.append(comment)
    print(f"Your change is confirmed for {comment}")
    options = input(f"Would you like to see the menu options again?")
    if options == "yes":
        menu_options()
    else:
        print("Thank you. Please come by again!")
        quit()


# cancelling reservation
def cancel_reservation():
    print("The reservation is cancelled")
    booking_list.clear()


# food menu
def show_food_menu():
    print("Starter: Fish soup")
    print("Main course: Beef tenderloin with fried potatoes")
    print("Dessert: Icecream")
    options = input(f"Would you like to see the menu options again?")
    if options == "yes":
        menu_options()
    else:
        print("Thank you. Please come by again!")
        quit()


# writing a review
def leave_review():
    review = input("What is your name and what would you like to write?")
    print(f"{review}")
    print(f"Thank you for the review!")
    options = input(f"Would you like to see the menu options again?")
    if options == "yes":
        menu_options()
    else:
        print("Thank you. Please come by again!")
        quit()


menu_options()
