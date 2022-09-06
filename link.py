sent = 'It is a dark night'
# splitting the sentence into words
sent_split = sent.split()
# extract each word with a loop
for i in sent_split:
    print(i, end = ' / ')