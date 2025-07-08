# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = sorted(set([score for name, score in students]))
    
    if len(scores) >= 2:
        second_lowest = scores[1]

        names = [name for name, score in students if score == second_lowest]

        for name in sorted(names):
            print(name)
