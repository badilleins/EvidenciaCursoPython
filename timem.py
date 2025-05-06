from datetime import datetime

dt = datetime(2020, 11, 4, 14, 53, 0)

print(dt.strftime("%Y/%m/%d %H:%M:%S"))                
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))              
print(dt.strftime("%a, %Y %b %d"))                    
print(dt.strftime("%A, %Y %B %d"))                     
print("Weekday:", dt.strftime("%w"))                    
print("Day of the year:", dt.strftime("%j"))
print("Week number of the year:", dt.strftime("%U"))   