# variables for settings mainly
import time

projectVersion = 1.0
adminCode = ""
adminLoggedin = False


def adminLogin():
    if adminCode == "":
        print("First time setup!\n"
              "You must enter a admin password or passcode.")
        time.sleep(2)
        adminCode == input("Enter new Admin code: ")
        print(adminCode)
    else:
        if input("Enter Admin code: ") == adminCode:
            print("Logging in")
            adminLoggedin == True
            main(adminLoggedin)
        else:
            print("Wrong passcode!")
            adminLogin()


def main(adminLoggedin):
    if adminLoggedin == False:
        print("Not logged in as admin")
        time.sleep(1)
        adminLogin()
    else:
        while True:
            time.sleep(2.5)
            #Main menu loop
            mainMenu_Input = input(f"Choose and option: "
                                   f"\n\t1. Generate a password"
                                   f"\n\t2. View passwords"
                                   f"\n\t3. View accounts"
                                   f"\n\t4. Add account"
                                   f"\n\t5. Delete account"
                                   f"\n\t6. Show help "
                                   f"\n\t7. Options"
                                   f"\n\t8. Exit"
                                   f"\n\nEnter input: ")


main(adminLoggedin)