# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    remove_duplicate=set(arr)
    
    sorted_arr=sorted(remove_duplicate)
    
    second_highest = sorted_arr[-2]
    print(second_highest)