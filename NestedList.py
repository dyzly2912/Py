if __name__ == '__main__':
    StudentList = []
    for _ in range(int(input())):
        name = input().strip()
        score = float(input().strip())
        StudentList.append([name, score])

    unique_scores = sorted({score for _, score in StudentList})
    second_lowest = unique_scores[1]

    result = [name for name, score in StudentList if score == second_lowest]
    for name in sorted(result):
        print(name)
