#encrypt/decrypt
def en(file,cmap): 
    foutput = open("encrypted.txt","w")
    #make dictionary based on txt input
    dic = {}   
    for line in cmap:
        a,b = line.split()
        dic[a]=b
    #line by line print new string to txt
    for line in file:
        ustr = ''
        line = line.strip()
        for x in line:
            if x in dic:
                ustr += dic[x]
            else:
                ustr += x
        print(ustr, file= foutput)
    foutput.close()

def dn(file,cmap):
    foutput = open("unencrypted.txt","w")
    #make dictionary based on txt input
    dic = {}   
    for line in cmap:
        a,b = line.split()
        dic[b]=a
    #line by line print new string to txt
    for line in file:
        ustr = ''
        line = line.strip()
        for x in line:
            if x in dic:
                ustr += dic[x]
            else:
                ustr += x
        print(ustr, file= foutput)
    foutput.close()

#Main Program
while True:
    try:
        finput = open(input("Enter input file name: "), "r")
        break
    except FileNotFoundError:
        print ("File Not Found")

while True:
    try:
        umap = input("Enter character map file name: ")
        cmap = open(umap, "r")
        break
    except FileNotFoundError:
        print ("File Not Found")

#Function call and reopen of cmap for second dic creation
user = en(finput,cmap)
cmap.close()
encrypted = open("encrypted.txt","r")
cmap = open(umap, "r")
test = dn(encrypted,cmap)
print("Done")

#Close open files
encrypted.close()
cmap.close()
finput.close()

