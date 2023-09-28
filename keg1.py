# kegiatan 1

def tambah(pertama, kedua):
    return pertama+kedua

# fungsi Pengurangan


def minus(pertama, kedua):
    return pertama-kedua

# fungsi Perkalian


def mult(pertama, kedua):
    return pertama*kedua

# fungsi Pembagian


def div(pertama, kedua):
    if kedua == 0:
        raise ValueError("Tidak dapat melakukan Pembagian Dengan nol")
    return pertama/kedua


def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '+':
            return tambah(tree(left_operand), tree(right_operand))
        elif operator == '-':
            return minus(tree(left_operand), tree(right_operand))
        elif operator == '*':
            return mult(tree(left_operand), tree(right_operand))
        elif operator == '/':
            return div(tree(left_operand), tree(right_operand))
    else:
        raise ValueError("Invalid expression tree node")


expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))
result = tree(expression_tree)
print("Hasil Evaluasi Pohon Ekspresi:", result)
