try:
    marks = float(input("Enter your marks: "))
    if 0 <= marks < 40:
        print("FAIL")
        print("You have to work harder.")
    elif marks > 100:
        print("Enter a valid mark between 0-100.")
    else:
        print("PASS")
        print("Well done!")
except ValueError:
    print("Enter a valid mark.")
print("Thank you!")
