num = 0
tot = 0
while True:
    sval = input('Enter a number: ')

    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    
    num+= 1
    tot+= fval

if num == 0:
    print(tot,num,0)
else:
    print(tot,num,tot/num)
    