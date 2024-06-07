psw1 = input("Enter a new password:  ")
psw2 = input("Enter again to confirm:  ")
if psw1 == psw2:
    print("Thank you password saved")
elif psw1.lower() == psw2.lower():
    print("Correct letters but wrong case")
else:
    print("Password incorrect")
