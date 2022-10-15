def computePay(hours, rate) :
    pay = hours * rate
    if hours > 40:
        pay += (hours - 40) * (rate * 0.5)
    return pay

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
fhours = float(hours)
frate = float(rate)

print("Pay:",computePay(fhours, frate))