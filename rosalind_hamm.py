lines = []
with open("rosalind_hamm", "r", encoding="utf-8") as file:
    for line in file: 
        line = line.strip()
        if line: 
            lines.append(line)
    s=lines[0]
    t=lines[1]
    mutations = 0
    for i in range(len(s)):
        if s[i] != t[i]: 
            mutations += 1
print (mutations)