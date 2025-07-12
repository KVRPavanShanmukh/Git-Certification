print("Subject Marks Grading System" + "\n" + "=" * 30)


grade = int(input())
if grade <= 100:
    if grade>90 :
        print("Grade A")
    elif grade>80 and grade <90:
        print("Grade B")
    elif grade>70 and grade<80:
        print("Grade C")
    elif grade>50 and grade<70:
        print("Grade D")
    else:
        print("Bayataki po ra sannasi")