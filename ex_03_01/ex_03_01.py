hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
fhours = float(hours)
frate = float(rate)
pay = fhours * frate
if fhours > 40:
    pay += (fhours - 40) * (frate * 0.5)
print("Pay:",pay)