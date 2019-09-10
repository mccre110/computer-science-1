#piglatin
#Word to Pig Function
def wordToPig(word):
    word = word.lower()
    add =''
    if word[0] in "aeiouAEIOU":
        word = word[0].upper()+word[1::]+"yay"
    else:
        for x in range(len(word)):
            if word[x].lower() in ('a','e','i','o','u'):
                break
            else:
                add += word[x].lower()
        word = word[len(add)].upper() + word[len(add)+1::] + add +'ay'
    return word                

#Name to Pig Function            
def nameToPig(first,last):
    first = wordToPig(first)
    last = wordToPig(last)
    return first +" "+ last

#Main Program
while True:
    try:
        finput = open(input("Enter file name: "), "r")
        break
    except FileNotFoundError:
        print ("File Not Found")
    
outputlatin = open("results_latin.txt", "w")
for line in finput:
    first,last = line.split()
    print (nameToPig(first,last), file= outputlatin)
finput.close()
outputlatin.close()
print ("Done!")
