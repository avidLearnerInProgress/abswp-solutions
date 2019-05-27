table_data = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David', ],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):
    col_width = [0] * len(table)
    for i in range(len(table[0])):
        for j in range(len(table)):
            if len(table[j][i]) > col_width[j]:
                col_width[j] = len(table[j][i])
    for z in range(len(table[0])):
        for x in range(len(table)):
            print(table[x][z].rjust(col_width[x] + 1), end="")
        print()

if __name__ == "__main__":
    print_table(table_data)