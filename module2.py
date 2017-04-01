def create():
    myfile=open("msg.txt","w")
    l=raw_input("Enter message")
    myfile.write(l)
    myfile.close()
def encrypt():
    myfile=open(r"msg.txt","r")
    newfile=open("encrypt.txt","w")
    l=myfile.read()
    for char in l:
        if char in "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM":
            a=ord(char)
            a=str(a)+' '
            newfile.write(a)
        else:
            newfile.write(char)
    myfile.close()
    newfile.close()
def decrypt():
    myfile=open(r"encrypt.txt","r")
    newfile=open("decrypt.txt",'w')
    l=myfile.readlines()
    for num in l:
        a=chr((num))
        a=str(a)
        newfile.write(a)
    else:
        newfile.write(str(num))
    myfile.close()
    newfile.close()
create()
encrypt()
decrypt()