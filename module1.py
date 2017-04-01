def createtextfile():
    fyl=open("content.txt","w")
    for i in range(input("Enter number of lines in the new fle")):
        l=raw_input("Enter a line")
        fyl.write(l)
        fyl.write("\n")
    return fyl
def countall(myfile):
    s=myfile.read()
    vowel=0
    digit=0
    spaces=0
    for char in s:
        if char in ["0","1","2","3","4","5","6","7","8","9"]:
            digit+=1
        elif char in ["a","e","i","o","u"]:
            vowel+=1
        elif char==" ":
            spaces+=1
    s=s.split()
    words=len(s)
    myfile.seek(0)
    l=myfile.readlines()
    lines=len(l)
    print "Lines=",lines
    print "Vowels=",vowel
    print"Digits=",digit
    print "Spaces=",spaces
    print "Words=",words
def replacespace(myfile):
    newfile=open("Wspace.txt","w")
    myfile.seek(0)
    s=myfile.read()
    for char in s:
        if char==" ":
            newfile.write("#")
        else:
            newfile.write(char)
while True:
    i=raw_input("Choose 1 to create a file, 2 to count characters in the file, 3 to replace the spaces with #, 4 to exit")
    if i=="1":
        f=createtextfile()
        print "File created"
    elif i=="2":
        fle=raw_input("Enter the file name")
        try:
            f=open(fle,"r")
        except IOError:
            print "File not found"
        else:
            countall(f)
            f.close()
    elif i=="3":
        fle=raw_input("Enter the file name")
        try:
            f=open(fle,"r")
        except IOError:
            print "File not found"
        else:
            replacespace(f)
            print "Spaces replaced"
            f.close()
    else:
        print "Exit"
        break
