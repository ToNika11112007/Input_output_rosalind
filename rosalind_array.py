with open("rosalind_array", "r", encoding="utf-8") as f:
    first_line = f.readline().strip().split()
    n = int(first_line[0])
    m = int(first_line[1])

    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, f.readline().strip().split())
        adj[u].append(v)
        adj[v].append(u)

degrees = []
for i in range(n + 1):
    degrees.append(len(adj[i]))

result = []
for i in range(1, n + 1):
    sum_deg = 0
    for neighbor in adj[i]:
        sum_deg += degrees[neighbor]
    result.append(sum_deg)

print(" ".join(map(str, result)))