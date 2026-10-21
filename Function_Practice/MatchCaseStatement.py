# Match case statement (switch):
# An alternate to use many elif use case 
# benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
       case 1:
            return "It is sunday"
       case 2:
            return "It is monday"      
       case 3:
            return "It is tuesday" 
       case 4:
            return "It is wednesday" 
       case 5:
            return "It is thursday" 
       case 6:
            return "It is friday" 
       case 7:
            return "it is saturaday"
       case _:
            return "Not a valid day"
         
print(day_of_week(8))





         
         
         
         