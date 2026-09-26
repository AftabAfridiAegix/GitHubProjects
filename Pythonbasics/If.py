# if = do some code only if some cndition is true 
# Else do something else

age= int(input("Enter your age :"))
if age >=18:
    print("you are now signed up! ")
elif age<0:
    print("you havenot born yet")
else:
    print("you must be 18+ to sign up")

response = input("would you like food? (y/n):")

if response  == "y":
    print("have some food")
else:
    print("no food for you")



