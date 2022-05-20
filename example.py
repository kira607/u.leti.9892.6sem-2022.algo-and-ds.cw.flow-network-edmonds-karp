from flow_network.io import load_flow_network, export_flow_network


def run_example(i: int) -> None:
    name = f'example_{i}'
    graph = load_flow_network(f'data/{name}.txt')
    print()
    print(f'Пример {i}:')
    print(f'{graph.max_flow=}')
    print('=' * 50)
    export_flow_network(graph, 'data', name)


def main():
    for i in range(1, 5):
        run_example(i)


if __name__ == '__main__':
    main()
