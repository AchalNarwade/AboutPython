# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
def symmetric_diff():
    
    M=int(input())
    set1=set(map(int,input().split()))
    
    N=int(input())
    set2=set(map(int,input().split()))
    
    result=sorted(set1^set2)
    
    for num in result: # to print numbers on diffrent lines
        print(num)
    
    
if __name__=='__main__':
    symmetric_diff()