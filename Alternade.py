#Alternades

print ("Would you like to Construct or Destruct?")
choice = input("c/d : ")

#loop end
pt = True

while choice == "d" and pt == True:
    string = input("Enter an Alternade: ")
    if string.isalpha():
        one = ''
        two = ''
        firstword = 0
        secondword = 1
        while firstword < len(string):
            one += string[firstword]
            firstword += 2
        while secondword < len(string):
            two += string[secondword]
            secondword += 2
        print(one,two)
        pt = False
            
    else:
        print("Try Again")

while choice == "c" and pt == True:
    string = input("Enter Two Words : ")
    one,two = string.split()
    one = one.upper()
    newword = ''
    var = 0
    if one.isalpha() and two.isalpha() and len(one)>=len(two):
        while var < len(one) and var < len(two):
            newword += one[var]
            newword += two[var]
            var += 1
        print (newword)
        pt = False
    else:
        print ("Try Again")

