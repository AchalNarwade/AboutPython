# https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
def is_subset():
    n=int(input())
    
    for _ in range(n):
        a=int(input())
        setA=set(map(int,input().split()))
    
        b=int(input())
        setB=set(map(int,input().split()))
    
    
        if(setA.issubset(setB)):
            print("True")
        else:
            print("False")
        
if __name__=='__main__':
    is_subset()
        
