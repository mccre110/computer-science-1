#DNA ATGC
#Complemetary Sequence Function
def complement(seq):
    seq = seq.upper()
    newseq = ""
    for i in range(len(seq)):
        if seq[i] == "A":
            newseq += "T"
        if seq[i] == "T":
            newseq += "A"
        if seq[i] == "G":
            newseq += "C"
        if seq[i] == "C":
            newseq += "G"
    return newseq

#Reverse Complementary Function
def revComplement(seq):
    seq = seq[::-1]
    seq = complement(seq)
    return seq

#User Input Check Loop
uinput=''
while uinput =='' or uinput =='bad':
    uinput=''
    seq = input("Enter a Sequence: (A T C G) :")
    seq = seq.lower()
    for i in range(len(seq)):
        if seq[i] not in ('a','t','g','c'):
            uinput = 'bad'
    if uinput == 'bad':
        print ("Try Again")
    else:
        uinput = 'good'
    
    
#Print and Function Call
print ("Complemetary Sequence: ",complement(seq))
print ("Reverse Complementary Sequence: ",revComplement(seq))
        
        
        
                   
    
    
