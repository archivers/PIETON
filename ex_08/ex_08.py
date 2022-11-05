try:
    han = open('mbox-short.txt')
except:
    print("File could not be opened")
    exit()

for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])
