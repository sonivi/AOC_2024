from collections import defaultdict, deque

def parse_input(input_data):
    sections = input_data.strip().split("\n\n")
    rules = [tuple(map(int, line.split("|"))) for line in sections[0].splitlines()]
    updates = [list(map(int, line.split(","))) for line in sections[1].splitlines()]
    return rules, updates

def is_correct_order(update, rules):
    positions = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in positions and y in positions:
            if positions[x] > positions[y]:  # x must appear before y
                return False
    return True

def topological_sort(rules, pages):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    # Build the graph and indegree counts for the given pages
    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            indegree[y] += 1

    for page in pages:
        if page not in indegree:
            indegree[page] = 0

    # Topological sort using Kahn's algorithm
    queue = deque([node for node in pages if indegree[node] == 0])
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

def reorder_and_calculate(rules, updates):
    total = 0

    for update in updates:
        if not is_correct_order(update, rules):
            sorted_update = topological_sort(rules, update)
            middle_index = len(sorted_update) // 2
            total += sorted_update[middle_index]

    return total

def main():
    with open("inp.txt", "r") as f:
        input_data = f.read()

    rules, updates = parse_input(input_data)
    result = reorder_and_calculate(rules, updates)
    print(f"Sum of middle page numbers after reordering: {result}")

if __name__ == "__main__":
    main()