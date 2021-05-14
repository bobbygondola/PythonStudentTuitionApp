
# BEGINNING OF MAIN() FN. Hold outer functions, hides functionality.
def main():
    enrolledCourses = [["", "", ""], ["", "", ""],
                       ["", "", ""], ["", "", ""], ["", "", ""]]
    tuitionBill = [0, 0, 0, 0, 0]
    PER_CREDIT_TUITION = 75
    PER_CREDIT_LAB_FEES = 15
    enrollCount = 0
    exitAnswer = 1
    welcomeSymbol = input(
        "Enter a special symbol or character to personalize your experience: ")

    welcomeBanner(welcomeSymbol)
    mainMenu(welcomeSymbol)

    while exitAnswer >= 0:
        choice = getChoice(welcomeSymbol)

        if choice == "E":
            if enrollCount < 5:
                x = enrollInCourse(enrollCount, enrolledCourses, welcomeSymbol)
            else:
                print(
                    "You have already enrolled in the maximum of 5 courses. You cannot register anymore courses this semester")
                x = input("Press any key to continue: ")
                if (x):
                    welcomeBanner(welcomeSymbol)

        elif choice == "T":
            calculateTuitionBill(enrolledCourses, tuitionBill,
                                 enrollCount, welcomeSymbol)

        elif choice == "X":
            exitProgram(welcomeBanner)
        else:
            print("Invalid Choice")
            mainMenu(welcomeSymbol)

    closingBanner(welcomeSymbol)

# BEGINING OF WELCOMEBANNER() FN. Displays important project information.


def welcomeBanner(symbol):
    topBorder = ""

    for i in range(80):
        topBorder += symbol
    bottomBorder = topBorder

    print(topBorder)
    print(symbol + "                             Student Tuition App                              " + symbol)
    print(symbol + "                        Written by: Robert Gondola                            " + symbol)
    print(symbol + "                                Spring 2021                                   " + symbol)
    print(symbol + "                          Date created: 05/08/2021                            " + symbol)
    print(bottomBorder)
    print("")
    print("")

# BEGINING OF MAINMENU() FN. Displays options to the user.


def mainMenu(symbol):
    topBorder = ""

    for i in range(80):
        topBorder += symbol
    bottomBorder = topBorder

    print(topBorder)
    print("Student Tuition App: " + symbol + " Main Menu " + symbol)
    print("----------------------------------")
    print(symbol + "                                " + symbol)
    print(symbol + " E. Enroll in a Course          " + symbol)
    print(symbol + " T. Calculate Tuition Bill      " + symbol)
    print(symbol + " X. Exit the Program            " + symbol)
    print(symbol + "                                " + symbol)
    print(bottomBorder)
    print("")

# BEGINING OF GETCHOICE() FN. Returns the mainMenu() option chosen to main().


def getChoice(symbol):
    line = ""
    choice = input("MAIN MENU - Make a Selection Now >>> ")

    for i in range(80):
        line += symbol
    print(line)
    print("")
    print("")
    return choice

# BEGINING OF CALCULATETUITIONBILL() FN. Takes in data, calls the displayTuitionBill(), passes in calculated data.


def calculateTuitionBill(enrolledCourses, tuitionBill, another, symbol):
    tuitionFeePerCredit = 75
    labFeePerCredit = 15
    courseCode = ""
    borderLine = ""
    enrollCount = 5

    for i in range(enrollCount):
        courseCode = enrolledCourses[i][0][0]
        print(courseCode)
    print(enrollCount)
    for i in range(80):
        borderLine += "-"
    for i in range(50):
        print("")
    print(borderLine)

    for i in range(enrollCount):
        courseCode = enrolledCourses[i][0]
        if (courseCode[0] == "P" and courseCode[1] == "H" and courseCode[2] == "Y"):
            tuitionBill[1] += 4
            tuitionBill[0] += 4
        elif (courseCode[0] == "S" and courseCode[1] == "C" and courseCode[2] == "I"):
            tuitionBill[1] += 4
            tuitionBill[0] += 4
        elif (courseCode[0] == "B" and courseCode[1] == "I" and courseCode[2] == "O"):
            tuitionBill[1] += 4
            tuitionBill[0] += 4
        elif (courseCode[0] == "C" and courseCode[1] == "M" and courseCode[2] == "P"):
            tuitionBill[1] += 4
            tuitionBill[0] += 4
        else:
            tuitionBill[1] += 0
            tuitionBill[1] += 4

    tuitionBill[2] = (tuitionBill[0] * tuitionFeePerCredit)  # tuitionSubtotal
    tuitionBill[3] = (tuitionBill[1] * labFeePerCredit)     # labFeesSubtotal
    tuitionBill[4] = (tuitionBill[2] + tuitionBill[3])      # tuitionGrandTotal

    # print("TOTAL CREDITS", tuitionBill[0])
    # print("Tuition Subtotal", tuitionBill[2])
    # print("labFeesSubtotal", tuitionBill[3])
    # print("TOTAL CREDITS", tuitionBill[4])

    # CALL TO DISPLAYTUITIONBILL() FN.
    displayTuitionBill(enrolledCourses, tuitionBill, enrollCount,
                       symbol, tuitionFeePerCredit, labFeePerCredit)

# BEGINING OF DISPLAYTUITIONBILL() FN.


def displayTuitionBill(enrolledCourses, tuitionBill, enrollCount, symbol, tuitionFeePerCredit, labFeePerCredit):
    borderLine = ""
    dash = ""

    for i in range(80):
        borderLine += "-"
    for i in range(50):
        print("")
    print(borderLine)

    print(symbol + " Department of Information Technologies at County College of Morris " + symbol)
    print(symbol + " Tuition Bill for Information Technology and Computer Science Degrees " + symbol)

    for i in range(78):
        dash += "-"
    print(dash)

    index = 1
    for record in enrolledCourses:
        theOutput = (str(index) + ". ")
        index += 1

        for field in range(3):
            if field < 2:
                theOutput += record[field] + " | "
            else:
                theOutput += record[field] + "."
        print(theOutput)
    print(borderLine)
    print("")
    print("")
    print("The tuition rate per credit is $" + str(tuitionFeePerCredit))
    print("The lab fee per credit is $" + str(labFeePerCredit))
    print(" Total enrolled credits:" +
          str(tuitionBill[0]) + " Tuition Subtotal: $" + str(tuitionBill[2]))
    print(" Total lab credits:" +
          str(tuitionBill[1]) + "Lab Fee Subtotal: $" + str(tuitionBill[3]))
    print(" Tuition Grand Total: $" + str(tuitionBill[4]))
    print("")
    print("")
    print(borderLine)
    print(symbol + "Your Tuition Bill Is Due At This Time!" + symbol)
    print(symbol + "Please Make Payment within 14 days to avoid being dropped from your classes." + symbol)
    print(borderLine)
    print("")
    print("")

# BEGINING OF ENROLLINCOURSE() FN. Takes in data outside of main, prompts user and adds chosen courses to the nested enrolledCourses list.


def enrollInCourse(enrollCount, enrolledCourses, bannerSymbol):
    topBorder = ""
    line = ""
    courseChoice = 0

    for i in range(80):
        topBorder += bannerSymbol
    print(topBorder)

    for i in range(78):
        line += "-"

    while(enrollCount < 5):
        for i in range(50):
            print("")

        print(bannerSymbol + " Department of Information Technologies at County College of Morris " + bannerSymbol)
        print(bannerSymbol + " Course Listing for Information Technology and Computer Science Degrees " + bannerSymbol)

        print(line)

        courseListing = [["CMP120", "Foundations of Info. Security", "No Lab Fees"],
                         ["CMP124", "Network Security", "No Lab Fees"],
                         ["CMP125", "Info Security Management", "No Lab Fees"],
                         ["CMP128", "Computer Science I", "No Lab Fees"],
                         ["CMP129", "Computer Science II", "No Lab Fees"],
                         ["CMP130", "Introduction to Information Technology",
                             "No Lab Fees"],
                         ["CMP131",
                          "Fundamentals of Programming (Python)", "No Lab Fees"],
                         ["CMP200", "Operating Systems and Utilities", "No Lab Fees"],
                         ["CMP230", "Computer Architecture & Assembly Language",
                          "No Lab Fees"],
                         ["CMP233", "Data Structures & Algorithms", "No Lab Fees"],
                         ["CMP239", "The Internet and Web Page Design", "No Lab Fees"],
                         ["CMP241",
                             "Database Programming (SQL)", "No Lab Fees"],
                         ["CMP243", "Ethical Hacking & Systems Defense", "No Lab Fees"],
                         ["CMP244", "Web Design II", "No Lab Fees"],
                         ["CMP246", "Operating Systems", "No Lab Fees"],
                         ["CMP249", "Advanced Web Programming", "No Lab Fees"],
                         ["CMP255", "Linux", "No Lab Fees"],
                         ["CMP262", "Data Science Programming", "No Lab Fees"],
                         ["CMP263", "Web Development Workflow", "No Lab Fees"],
                         ["CMP264", "Machine Learning", "No Lab Fees"],
                         ["CMP280", "Software Engineering", "No Lab Fees"],
                         ["CHM117/118", "Introductory Chemistry Lecture/Lab",
                          "(Lab Fee Applies)"],
                         ["CHM125/126", "General Chemistry I Lecture/Lab",
                          "(Lab Fee Applies)"],
                         ["CHM127/128", "General Chemistry II Lecture/Lab",
                          "(Lab Fee Applies)"],
                         ["PHY125/126", "Physics I Lecture/Lab",
                          "(Lab Fee Applies)"],
                         ["PHY127/128", "Physics II Lecture/Lab",
                          "(Lab Fee Applies)"],
                         ["PHY130", "Engineering Physics I",
                             "(Lab Fee Applies)"],
                         ["PHY133/134", "Engineering Physics II Lecture/Lab",
                          "(Lab Fee Applies)"],
                         ["BIO101", "Anatomy and Physiology I",
                          "(Lab Fee Applies)"],
                         ["BIO102", "Anatomy and Physiology II",
                          "(Lab Fee Applies)"],
                         ["BIO 121", "General Biology I", "(Lab Fee Applies)"],
                         ["BIO 122", "General Biology II",
                             "(Lab Fee Applies)"],
                         ["SCI 118", "General Astronomy", "(Lab Fee Applies)"],
                         ["PHY103", "Concepts of Physics",
                             "(Lab Fee Applies)"],
                         ["PHY 118", "Meteorology", "(Lab Fee Applies)"],
                         ["ENG111", "English Composition I", "No Lab Fees"],
                         ["ENG112", "English Composition II", "No Lab Fees"],
                         ["MAT110", "College Algebra", "No Lab Fees"],
                         ["MAT123", "Precalculus", "No Lab Fees"],
                         ["MAT130", "Probability and Statistics", "No Lab Fees"],
                         ["MAT131", "Calculus I", "No Lab Fees"],
                         ["MAT132", "Calculus II", "No Lab Fees"]]

        index = 1
        for record in courseListing:
            theOutput = (str(index) + ". ")
            index += 1

            for field in range(3):
                if field < 2:
                    theOutput += record[field] + " | "
                else:
                    theOutput += record[field] + "."
            print(theOutput)

        print(line)

        print(bannerSymbol +
              " Enter Only the List Item Number corresponding to the Course Code you want to register for [Example: 1] " + bannerSymbol)
        print("")

        courseChoice = input("Make a Selection Now >>>")
        print("")

        x = int(courseChoice)

        if (x > 0 & x < 42):
            theChosenCourse = "You have just registered for,"
            print("")
            print(theChosenCourse + " " + courseListing[x-1][0])
            print("")
            print("")

        else:
            print("Error: Invalid Input! No Such Course Code Found. Please Try Again.")

        for field in range(3):
            enrolledCourses[enrollCount][field] = courseListing[x-1][field]
        enrollCount += 1

        classIndex = 1
        for i in enrolledCourses:
            print("Enrolled in:", str(classIndex) + ".", i)
            classIndex += 1
        print("")
        print("")
    mainMenu(bannerSymbol)
    return enrollCount

# BEGINING OF CLOSINGBANNER() FN. Displays exit banner to the user.


def closingBanner(symbol):
    topBorder = ""

    for i in range(80):
        topBorder += symbol
    bottomBorder = topBorder

    print("")
    print("")
    print(topBorder)
    print("Thank you for using the Tuition Bill Calculator App v. 1.0!")
    print("This program will now terminate…")
    print(bottomBorder)
    print("")
    print("")

# BEGINING OF EXITPROGRAM() FN. Exits or returns to mainMenu.


def exitProgram(symbol):
    answer = 0
    print()
    print()

    print("You have entered the Exit Program command!  If this was a mistaken entry, you can return to the main menu now by entering ANY positive number OR 0.  If you meant to exit this program, then please enter ANY negative number now to confirm the program termination.")
    answer = input("   Make a Selection Now >>> ")
    p = int(answer)
    ik = input("\n\nYour answer has been recorded.  Press Enter to Continue...")
    if p > 0:
        mainMenu(symbol)
    else:
        quit()


main()
