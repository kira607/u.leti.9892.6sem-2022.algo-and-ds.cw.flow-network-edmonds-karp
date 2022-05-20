import helpers
import latex


def get_complexity_table():
    methods = [
        'vertex',
        'edge',
        'vertices',
        'edges',
        'add_vertex',
        'add_edge',
        '_get_max_flow',
        '_get_augmenting_path',
        '_get_residual_capacity',
    ]
    table = latex.LatexTable(
        2, 'l', 
        caption='Оценка временной сложности методов класса FlowNetwork',
        caption_pos = 'bottom',
        label='complexity'
    )
    table.set_header('Метод', 'Оценка временной сложности')
    for method in methods:
        table.add_row(f'\\verb|{method}|', '$ O(?) $')
    return table.render()


def wrap_data(data):
    return '\n'.join(' '.join(str(i) for i in row) for row in data)


def make_example(i, data, expected_max_flow):
    s = f'\\subsection*{{Пример {i}}}\n\n'

    s += 'Исходные данные:\n\n\\begin{lstlisting}\n'
    s += wrap_data(data)
    s += '\n\\end{lstlisting}\n\n'

    pic_result = latex.LatexPicture(
        f'example_{i}',
        f'Результ выполнения примера {i}',
        width='\\linewidth',
    )

    s += (
        f'Результат выполнения программы представлен '
        f'на рис. \\ref{{{pic_result.label}}}.\n\n'
        f'{pic_result.render()}\n\n'
    )

    s += f'Итоговый максимальный поток: {expected_max_flow}\n\n'

    pic_result_graph = latex.LatexPicture(
        f'example_graph_{i}',
        f'Результирующий граф для примера {i}',
        width='\\linewidth',
    )

    s += (
        f'Результирующий граф представлен '
        f'на рис. \\ref{{{pic_result_graph.label}}}.\n\n'
        f'{pic_result_graph.render()}\n\n'
    )

    return s

def make_examples():
    examples = [
        (
            (
                ('S', 'O', 3),
                ('S', 'P', 3),
                ('O', 'Q', 3),
                ('O', 'P', 2),
                ('P', 'R', 2),
                ('Q', 'R', 4),
                ('Q', 'T', 2),
                ('R', 'T', 3),
            ),
            5,
        ),
        (
            (
                ('S', 'A', 8),
                ('S', 'B', 5),
                ('S', 'C', 3),
                ('A', 'B', 6),
                ('A', 'C', 4),
                ('A', 'D', 5),
                ('B', 'C', 5),
                ('B', 'E', 3),
                ('B', 'F', 5),
                ('C', 'D', 5),
                ('C', 'E', 4),
                ('D', 'E', 5),
                ('D', 'T', 3),
                ('E', 'T', 8),
                ('F', 'E', 3),
                ('F', 'T', 9),
            ),
            16,
        ),
        (
            (
                ('S', 'A', 5),
                ('S', 'D', 10),
                ('S', 'G', 5),
                ('A', 'B', 10),
                ('B', 'C', 10),
                ('B', 'E', 25),
                ('C', 'T', 5),
                ('D', 'A', 15),
                ('D', 'E', 20),
                ('E', 'G', 5),
                ('E', 'F', 30),
                ('F', 'B', 15),
                ('F', 'T', 15),
                ('F', 'I', 5),
                ('G', 'H', 5),
                ('H', 'I', 5),
                ('H', 'F', 5),
                ('I', 'T', 5),
            ),
            20,
        ),
        (
            (
                ('S', 'A', 8),
                ('S', 'B', 12),
                ('S', 'C', 26),
                ('S', 'D', 9),
                ('A', 'E', 3),
                ('B', 'E', 4),
                ('B', 'F', 6),
                ('C', 'G', 11),
                ('D', 'G', 2),
                ('D', 'H', 3),
                ('E', 'I', 9),
                ('E', 'J', 5),
                ('F', 'J', 7),
                ('G', 'J', 9),
                ('G', 'K', 2),
                ('H', 'K', 12),
                ('I', 'T', 8),
                ('J', 'I', 11),
                ('J', 'K', 20),
                ('K', 'T', 16),
            ),
            24,
        ),
    ]
    s = '\\section{Примеры работы}\n\n'
    for i, example in enumerate(examples, start=1):
        s += make_example(i, *example)
    return s


def main():
    eg = make_examples()
    with open('modules/chapters/example.tex', 'w') as f:
        f.write(eg)


if __name__ == '__main__':
    main()
