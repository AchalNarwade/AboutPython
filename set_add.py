# https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

def sorted_countries():
    n=int(input())
    countries=set()
    
    for _ in range(n):
        country=input().strip()
        countries.add(country)
        
    print(len(countries))
    
if __name__== '__main__':
    sorted_countries()
