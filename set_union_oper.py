# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true

def union_operation():
    a=int(input())
    set1=set(map(int,input().split()))
    
    b=int(input())
    set2=set(map(int,input().split()))
    
    union_of_set=len(set1&set2)
    result=((len(set1)+len(set2))-union_of_set)
    print(result)
    
if __name__=='__main__':
    union_operation()
    