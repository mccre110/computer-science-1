number = int(input("Enter a number to classify: "))
divisor=1
sum_of_div=0
for test in range(2,1,number+1):
    
    if number%divisor ==0:
        sum_of_div +=divisor
        divisor+=1

if sum_of_div==number:
    print(number,"is perfect")
else:
    print(number,"is not perfect")
