from collections import Counter

#counting the frequency of words
#needs improvement for handling/counting punctuation

fname = input('Enter File: ')
if len(fname) < 1: fname = 'clown.txt'

try:
    handle = open(fname)
except:
    print('File does not exist')
    exit()

di = dict()
punctuation = ['?','(',')','.','\,',';',':','!','-','/']

for line in handle:
    line = line.rstrip()

    '''
    thanks to breceluu
    put line in lower case since we are not
    differentiating based on capitalization
    '''
    words = line.lower().split()
    for word in words:
        for punk in punctuation:
            if punk in word:
                word = word.replace(punk,'')  
        di[word] = di.get(word, 0) + 1

largest = -1
the_word = None
for key,value in di.items():
    if value > largest:
        largest = value
        the_word = key

#gets a dictionary of the top five most frequent words
#top_five = dict(Counter(di).most_common(5))

#sorting top 5 using a different method than exercise 9
top_five = list()
for k,v in di.items():
    top_five.append( (v,k) )

print("")
print("The most frequent word is","\'",the_word,"\'","with",  largest, "occurences.")
print('')
print("TOP 5 Frequent Words")
print("=====================")

'''
counter = 1;
for key in top_five:
    print(counter,":",key,top_five[key])
    counter = counter+1

using a new method to print the top 5 than exercise 9
'''
top_five = sorted(top_five, reverse=True)

for v,k in top_five[:5]:
    print(k,v)
