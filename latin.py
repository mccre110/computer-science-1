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
        print(add)
    return word                

#Name to Pig Function            
def nameToPig(first,last):
    first = wordToPig(first)
    last = wordToPig(last)
    return first +" "+ last


#Main Program
uinput = input("Enter Your Name :")
first,last = uinput.split()
print (nameToPig(first,last))


    

