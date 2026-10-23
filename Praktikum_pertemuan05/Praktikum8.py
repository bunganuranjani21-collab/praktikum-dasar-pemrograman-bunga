def faktorial(n):
    # Kondisi dasar (Base Case): berhenti ketika n bernilai 0 atau 1
    if n == 0 or n == 1:
        return 1
    
    # Pemanggilan rekursif (Recursive Case): n dikalikan dengan faktorial(n - 1)
    else:
        return n * faktorial(n - 1)

# Mencetak hasil faktorial dari 5
print(faktorial(5))