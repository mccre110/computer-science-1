

sec_int = int(input("Seconds?(1 to 86,400) : "))


minutes_int = sec_int//60

hours_int = minutes_int//60

realmin_int = minutes_int%60

seconds_int = sec_int%60

print(hours_int , "Hours" , realmin_int , "Minutes" , seconds_int , "Seconds")
