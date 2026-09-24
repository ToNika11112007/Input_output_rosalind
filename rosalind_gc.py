sequences = {}
current_seq_name = ""

with open("rosalind_gc", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
    
        if line.startswith(">"):
            current_seq_name = line[1:]  
            sequences[current_seq_name] = ""
        else: 
            if current_seq_name:
                sequences[current_seq_name] += line
percent_max = -1.0
best_name = ""

for name, dna_string in sequences.items():
    gc_count = dna_string.count("G") + dna_string.count("C")
    percent = (gc_count / len(dna_string)) * 100
    
    if percent > percent_max:
        percent_max = percent
        best_name = name

print(best_name)
print(f"{percent_max:.6f}")