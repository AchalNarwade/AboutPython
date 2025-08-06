# https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_strict_superset():
    setA=set(map(int,input().split()))
    
    n=int(input())
    for _ in range(n):
        setx=set(map(int,input().split()))
        if not (setA>setx): #not a strict superset
            print("False")
            return # exit early if any check fails
    print("True") # all checks passed
            
            
if __name__=='__main__':
    is_strict_superset()
