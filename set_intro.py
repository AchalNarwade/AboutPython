# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

def average(array):
    # your code goes here
    remove_duplicates=set(array)
    return round(sum(remove_duplicates)/len(remove_duplicates), 3)  #return f"{average:.3f}""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)