# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

def No_Idea():
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    setA=set(map(int,input().split()))
    setB=set(map(int,input().split()))
    happiness=0
    for num in arr:
        if num in setA:
            happiness+=1
        if num in setB:
            happiness-=1
    print(happiness)
    
    
if __name__=='__main__':
    No_Idea()