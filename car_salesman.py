base = float(input("Please input the base price of your car:\n"))
year = int(input("Please input the year of your car:\n"))
if year <= 2004:
    unifee = 10.00
elif year <= 2007:
    unifee = 50.00
elif year <= 2010:
    unifee = 80.00
elif year <= 2013:
    unifee = 100.00
else:
    unifee = 150.00
regifee = 43.00
tax = base * 0.066
title = 50.00
tcost = base + unifee + regifee + tax + title
print("\nYour cost of buying this car would be:\n")
print("\tBase cost: ", base)
print("\tUniform fee: ",unifee)
print("\tRegistration fee: ",regifee)
print("\tTax: ",tax)
print("\tTitle fee: ",title,"\n")
print("Total Cost", tcost)
