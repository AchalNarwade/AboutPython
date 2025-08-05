# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
def symmetric_difference_oper():
    a=int(input())
    eng_news=set(map(int,input().split()))
    
    b=int(input())
    french_news=set(map(int,input().split()))
    
    either_but_not_both=((len(eng_news)+len(french_news))-2*len(eng_news&french_news))
    #eng_news^french_news
    print(either_but_not_both)
    
if __name__=='__main__':
    symmetric_difference_oper()