sub1 = float(input("Enter marks for sub 1(out of 100): "))
sub2 = float(input("Enter marks for sub 2(out of 100): "))
sub3 = float(input("Enter marks for sub 3(out of 100): "))
sub4 = float(input("Enter marks for sub 4(out of 100): "))
sub5 = float(input("Enter marks for sub 5(out of 100): "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) * 100

if percentage >= 60:
    print("First Division")
elif percentage >= 50:
    print("Second Division")
elif percentage >= 40:
    print("Third Division")
else:
    print("Fail")