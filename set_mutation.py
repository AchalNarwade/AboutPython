# https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true

def mutation_of_set():
    n=int(input())
    setA=set(map(int,input().split()))

    for _ in range(int(input())):
        operation_name , size=input().split()
        other_set=set(map(int,input().split()))
        #setA.operation_name(other_set){ wrong _ Python looks for a method literally called operation_name; correct_ A.intersection_update(other_set) if op_name =intersection_update}
        getattr(setA,operation_name)(other_set)
        
    print(sum(setA))
        
if __name__=='__main__':
    mutation_of_set()