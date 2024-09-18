def letter_grade():
    grade = int(input("What's your current grade?"))
    if grade >= 95:
        print("A+")
    if grade < 95 and grade >= 92:
        print("A")
    if grade >= 85:
        print("B+")
    if grade < 85 and grade >= 82:
        print("B")



if __name__ == "__main__":
    letter_grade()
 