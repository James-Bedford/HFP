
wordlist = ['a','e','i','o','u']

word = 'scratches'

for i in word:
    if i in wordlist:
        print(i)
    else:
        wordlist.append(i)
print(wordlist)