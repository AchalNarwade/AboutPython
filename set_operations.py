# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

def operations_on_set():
    n=int(input())
    setS=set(map(int,input().split()))
    No_of_commands=int(input())
    
    for _ in range(No_of_commands):
        command=input().split() 
        operation=command[0]
       
        if operation=="pop":
            setS.remove(min(setS))
        elif operation=="discard":
            setS.discard(int(command[1]))
        elif operation=="remove":
            value=int(command[1])
            if value in setS:
                setS.remove(value)
            
    print(sum(setS))
    
if __name__=='__main__':
    operations_on_set()