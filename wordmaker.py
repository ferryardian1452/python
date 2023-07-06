one=(open('givennames.txt', 'r')).readlines()
two=(open('surnames.txt', 'r')).readlines()
wordlist=[]
for word1 in one:
    for word2 in two:
            new1=word1+word2

            wordlist.append(new1)
wordlist = [item.replace('\r', '').replace('\n', '') for item in wordlist]
WordList='\n'.join(wordlist)
Wlist=open('wordlist.txt','w')
Wlist.write(WordList)
