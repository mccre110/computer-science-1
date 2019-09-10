#DNA ATGC
#Complemetary Sequence Function
def complement(seq):
    seq = seq.upper()
    newseq = ""
    for i in range(len(seq)):
        if seq[i] == "A":
            newseq += "T"
        elif seq[i] == "T":
            newseq += "A"
        elif seq[i] == "G":
            newseq += "C"
        elif seq[i] == "C":
            newseq += "G"
        else:
            print("Invalid Input")
            break
    return newseq

#Reverse Complementary Function
def revComplement(seq):
    seq = seq[::-1]
    seq = complement(seq)
    return seq

#Main Program
while True:
    try:
        finput = open(input("Enter file name: "), "r")
        break
    except FileNotFoundError:
        print ("File Not Found")

outputcomp = open("results_complement.txt", "w")
for line in finput:
    line = line.strip()
    print ("Complemetary Sequence: ",complement(line)," - Reverse Complementary Sequence: ",revComplement(line),file = outputcomp)
finput.close()
outputcomp.close()
print ("Done!")

