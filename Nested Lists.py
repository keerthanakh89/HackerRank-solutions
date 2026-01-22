if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Get all unique scores and sort them
    scores = sorted(set([student[1] for student in students]))

    # Second lowest score
    second_lowest = scores[1]

    # Get names with second lowest score
    names = [student[0] for student in students if student[1] == second_lowest]

    # Sort names alphabetically
    names.sort()

    # Print each name
    for name in names:
        print(name)
