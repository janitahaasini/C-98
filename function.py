def countWords():
    fileName=input("ENTER THE NAME OF THE FILE")
    file=open(fileName,'r')
    noofwords=0
    for line in file :
        words=line.split()
        noofwords=noofwords+len(words)
    print("NUMBER OF WORDS=")
    print(noofwords)



countWords()