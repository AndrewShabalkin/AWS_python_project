
# Conversion Celsius to Fahrenheit
#C=float(input('Please enter temperature in celsius  '))
#F=((C * 1.8)+32)
#print('Temp in Fahrenheit',F)

#hrs = float(input("Enter Hours: "))
#rate = float(input("Enter rate: "))
#pay = (hrs * rate)
#print("Pay: ", pay)

stdhrs = input("Enter Hours: ")
stdrate = input("Enter Rate: ")
fhrs = float(stdhrs)
frate = float(stdrate)
#print(fhrs,frate)
if fhrs > 40:
    print("Overtime")
    regular = frate * fhrs
    otp = (fhrs - 40.0) * (frate * 0.5)
    print(regular,otp)
    xp = regular + otp
else:
    print("Regular")
    xp = fhrs * frate
print("Pay", xp)


