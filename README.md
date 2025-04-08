# DNA Consensus and Profile Matrix Generator

This Python script reads a collection of DNA sequences in FASTA format, builds a **profile matrix**, and generates a **consensus string** based on the most common nucleotides at each position.

---

## 📌 Problem Description

Given a set of DNA strings of equal length, the script:

- Constructs a **profile matrix** showing the frequency of A, C, G, and T at each position.
- Generates a **consensus string** by selecting the most frequent base at each position.

This is based on a classic problem from Rosalind, a platform for bioinformatics challenges.

---

## 🧪 Example Input

`dna_sequences.txt` (FASTA format):

```
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
```

---

## 📾 Sample Output

```
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
```

---

## 🚀 How to Run

1. Create or edit your input file `dna_sequences.txt` (in FASTA format).

2. Run the Python script:

```bash
python consensus_profile.py
```

---

## 📁 Files

- `consensus_profile.py` — Main script to generate consensus and profile
- `dna_sequences.txt` — Input file with DNA strings in FASTA format
- `README.md` — Documentation

---

## 🧬 Dependencies

- Python 3.x  
- No external libraries required (uses only the Python standard library)

---
