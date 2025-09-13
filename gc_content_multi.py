# gc_content.py
# برنامج بسيط لحساب نسبة GC من تسلسل DNA

def clean_sequence(seq):
    return ''.join([ch.upper() for ch in seq if ch.upper() in "ATGC"])

def gc_content(sequence):
    seq = clean_sequence(sequence)
    if len(seq) == 0:
        return 0.0
    g = seq.count('G')
    c = seq.count('C')
    return (g + c) / len(seq) * 100

def main():
    seq = input("أدخل تسلسل DNA: ").strip()
    print(f"GC content: {gc_content(seq):.2f}%")

if __name__ == "__main__":
    main()
