myfile=open(r"security.txt","a+")
while True:
    myfile.seek(0)
    id=raw_input("Enter id")
    avail=1
    while True:
        l=myfile.readline()
        if not l:
            break
        else:
            l=l.split()
            if l[0]==id:
                avail=0
                break
            else:
                avail=1
    if avail==0:
        print "ID not available"
    else:
        print "ID is saved"
        break
while True:
    passwrd=raw_input("Enter password")
    if len(passwrd)<8:
        avail=0
    elif len(passwrd)>=8:
        for char in passwrd:
            if char not in["@","$","%"]:
                 avail=0
            else:
                avail=1
    if avail==1:
        print "Password saved"
        break
    else:
        print "Invalid"
myfile.close()
myfile=open("security.txt","a")
info=id+" "+passwrd
myfile.write(info)
myfile.write("\n")
myfile.flush()
myfile.close()