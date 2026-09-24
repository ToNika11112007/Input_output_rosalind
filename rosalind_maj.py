result = []
with open("rosalind_maj", "r", encoding="utf-8") as file:
    first_line = file.readline().strip()
    k, n = map(int, first_line.split())
    
    for line in file:
        line = line.strip()
        if not line:
            continue
        numbers = list(map(int, line.split()))
        
        numbers.sort()
        candidate = numbers[n // 2]
        
        if numbers.count(candidate) > n / 2:
            result.append(str(candidate))
        else:
            result.append("-1")

print(" ".join(result))