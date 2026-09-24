with open("rosalind_iprb", "r", encoding="utf-8") as file:
    line = file.read().strip()
    k, m, n = map(int, line.split())
    total = k+m+n
    total_pairs = total * (total - 1)
    aa_aa = (n*(n-1))/total_pairs
    Aa_Aa = (m*(m-1))/total_pairs*0.25
    Aa_aa = (2*m*n)/total_pairs*0.5
    prob_rec = aa_aa+Aa_Aa+Aa_aa
    proob_dom = 1 - prob_rec
    print(proob_dom)