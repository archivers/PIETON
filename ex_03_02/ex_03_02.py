fhours = -1
frate = -1

while (fhours == -1):
    print("Please enter an number for hours worked")
    hours = input("Enter Hours: ")
    try:
        fhours = float(hours)
    except:
        fhours = -1

while (frate == -1):
    print("Please enter an number for the hourly rate")
    rate = input("Enter Rate: ")
    try:
        frate = float(rate)
    except:
        frate = -1

pay = fhours * frate
if fhours > 40:
    pay += (fhours - 40) * (frate * 0.5)
print("Pay:",pay)