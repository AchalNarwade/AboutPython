# https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
def difference_oper():
    a=int(input())
    eng_news=set(map(int,input().split()))
    
    b=int(input())
    french_news=set(map(int,input().split()))
    
    only_eng=((eng_news|french_news)-(french_news)-(eng_news&french_news))
    # eng_news-french_news=diffrence(only english)
    print(len(only_eng))
    
if __name__=='__main__':
    difference_oper()