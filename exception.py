# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
def error_handling():
    t=int(input())
    
    for _ in range(t):
        try:
            a,b=map(int,input().split())
            print(a//b) #instead of converting direct int , // will give the exact value error that is the expected outcome
        except ZeroDivisionError as e:
            print("Error Code:",e)
        except ValueError as e :
            print("Error Code:",e)

if __name__=="__main__":
    error_handling()
    
    
