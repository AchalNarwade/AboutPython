# https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

def is_leap(year):
    leap = False
    if year%400==0:
        leap=True
    elif year%100==0 and year%400!=0:
        leap=False
    elif year%4==0:
        leap=True
    else:
        leap=False
        
    # Write your logic here
    
    
    return leap