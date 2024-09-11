import datetime as dt
from LibRizz import main

class Runner:
    def __init__(self):
        self.datetime = dt.datetime.now()
        self.duration = 1
        self.groupName = ""
        self.users = []

        self.start_time = None
        self.stop_time = None

    def calculate_times(self):
        if self.datetime and self.duration:
            self.start_time = self.datetime.time()
            self.stop_time = (self.datetime + dt.timedelta(hours=self.duration)).time()

    def print_main_menu(self):
        print("Welcome to LibRizz 2.0")
        print("----------------------")
        print('1. Set booking date and time')
        print('2. Set Group Name')
        print('3. Manage all Users')
        print('4. Book rooms')
        print('5. Exit')
        print()

    def run_main_menu(self):
        self.print_main_menu()
        choice = input("Please select what you would like to do:")

        if int(choice) == 1:
            print("Current Booking Time: {} and duration is {} hours".format(self.datetime, self.duration))
            print("1. Change Booking Time")
            print("2. Change Duration")
            print("3. Go Back")
            choiceSub = input("Please select what you would like to do:")
            if int(choiceSub) == 1:
                newDate = input("Please enter the new booking date and time: (YYYY-MM-DD HH:MM:SS)")
                self.datetime = dt.datetime.strptime(newDate, '%Y-%m-%d %H:%M:%S')
                return
            elif int(choiceSub) == 2:
                newDuration = input("Please enter the new duration in hours:")
                self.duration = int(newDuration)
                return
            elif int(choiceSub) == 3:
                return

        elif int(choice) == 2:
            print("Current Group '{}'".format(self.groupName))
            print("1. Change Name")
            print("2. Go Back")
            choiceSub = input("Please select what you would like to do:")
            if int(choiceSub) == 1:
                newName = input("Please enter the new name:")
                self.groupName = newName
                return
            elif int(choiceSub) == 2:
                return
        elif int(choice) == 3:
            print("There are {} users.".format(len(self.users)))
            print("1. Add User")
            print("2. Go Back")
            choiceSub = input("Please select what you would like to do:")
            if int(choiceSub) == 1:
                newUser = {}
                newUser["NID"] = input("Please enter the user's NID:")
                newUser["Password"] = input("Please enter the user's password:")
                newUser["Last Name"] = input("Please enter the user's Last name:")
                newUser["Student ID"] = input("Please enter the user's Student ID:")
                self.users.append(newUser)
                return
            elif int(choiceSub) == 2:
                return

        elif int(choice) == 4:
            print("Book rooms")
            main(self.start_time, self.users[0]['NID'], self.users[0]['Password'], self.users[0]['Student ID'], self.groupName, self.users[0]['Last Name'])
            return

        elif int(choice) == 5:
            print("Exiting...")
            exit()

    def run(self):
        while True:
            self.run_main_menu()

myrunner = Runner()
myrunner.run()