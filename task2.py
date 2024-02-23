import json


def sol(matrix):
    new_matrix = []
    new_columns = []
    for col in range(len(matrix[0])):
        column = []
        for row in matrix:
            column.append(row[col])
        if column not in new_columns:
            new_columns.append(column)

    for i in range(len(new_columns[0])):
        new_row = []
        for j in range(len(new_columns)):
            new_row.append(new_columns[j][i])
        new_matrix.append(new_row)

    return new_matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def main():
    with open('test_task_2.json', 'r') as file:
        matrix = json.load(file)

    print_matrix(matrix)
    print()
    print_matrix(sol(matrix))

    with open('answer_task_2.json', 'w') as file:
        json.dump(sol(matrix), file)


if __name__ == "__main__":
    main()
