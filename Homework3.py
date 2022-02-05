import re


text = """tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
# normalizing case view
text = re.split('([.!?\t\n] *)', text)
text = ''.join([i.capitalize() for i in text])

# iz mistake solver
text = re.sub(' (iz) ', ' is ', text)
text = re.sub('(Iz) ', 'Is ', text)

# whitespace count
wsCnt = len(re.findall(r'[\s]', text))

# take last word of each sentence
lastW = ''
for i in re.split('[.?!]', text)[0:-1]:
    lastW += re.search("(\w+)$", i).group() + ' '
text += lastW

# results print
print(text)
print('Whitespaces count', wsCnt)
