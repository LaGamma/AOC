from collections import defaultdict, deque
import re

with open("day7.txt") as f:
    lines = [x.strip() for x in f.readlines()]


class Child:
    def __init__(self, color, count):
        self.color = color
        self.count = count


contained_in = defaultdict(list)
contains = defaultdict(list)

for line in lines:
    children = re.findall(r"(\d) (\w+ \w+)", line)
    parent = " ".join(line.split()[:2])
    for count, color in children:
        contained_in[color].append(parent)
        contains[parent].append(Child(color, int(count)))


def bfs(color):
    color_contains = set()
    q = deque([color])
    while q:
        u = q.popleft()
        for v in contained_in[u]:
            if v not in color_contains:
                color_contains.add(v)
                q.append(v)
    return color_contains


def get_weight(color):
    w = 0
    for child in contains[color]:
        w += child.count * (1 + get_weight(child.color))
    return w


print("Part 1:", len(bfs("shiny gold")))
print("Part 2:", get_weight("shiny gold"))