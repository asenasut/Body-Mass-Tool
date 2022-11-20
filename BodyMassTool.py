height=float(input("Please enter your height (m):"))
weight= float(input("Please enter your weight (kg):"))
bki= weight/(height**2)
print("Your obesity according to your body mass index:")
if bki<18.50:
   print("weak")
elif bki>=18.50 and bki<25.00:
   print("regular")
elif bki>=25.00 and bki<30.00:
   print("heavy")
elif bki>=30.00 and bki<35.00:
   print("overweight")
elif bki>35.00:
   print("obese")