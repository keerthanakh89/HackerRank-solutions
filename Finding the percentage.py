if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *scores = input().split()
        scores = list(map(float, scores))
        student_marks[name] = scores

    query_name = input()
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)

    print(f"{average:.2f}")
