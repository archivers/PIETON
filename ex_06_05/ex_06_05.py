str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
piece = str[ipos+1:].strip()
value = float(piece)
print(value)
