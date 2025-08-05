# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
def intersection_oper():
    a=int(input())
    eng_news=set(map(int,input().split()))
    
    b=int(input())
    french_news=set(map(int,input().split()))
    
    both_news=eng_news.intersection(french_news) # (eng_news&french_news)
    print(len(both_news))
    
if __name__=='__main__':
    intersection_oper()