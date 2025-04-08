from collections import defaultdict

def read_fasta(filename):
    sequences = []
    with open(filename, 'r') as file:
        current_seq = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_seq:
                    sequences.append(current_seq)
                    current_seq = ''
            else:
                current_seq += line
        if current_seq:
            sequences.append(current_seq)
    return sequences

def build_profile_and_consensus(sequences):
    length = len(sequences[0])
    profile = {
        'A': [0] * length,
        'C': [0] * length,
        'G': [0] * length,
        'T': [0] * length,
    }

    for seq in sequences:
        for i, base in enumerate(seq):
            profile[base][i] += 1

    consensus = ''
    for i in range(length):
        max_base = max('ACGT', key=lambda base: profile[base][i])
        consensus += max_base

    return consensus, profile

def main():
    filename = 'dna_sequences.txt'  # <-- replace with your filename
    sequences = read_fasta(filename)
    consensus, profile = build_profile_and_consensus(sequences)

    print(consensus)
    for base in 'ACGT':
        print(f"{base}: {' '.join(map(str, profile[base]))}")

if __name__ == '__main__':
    main()
