def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

#contoh
n = int(input("Silahkan input angka: "))
hasil = faktorial(n)
print(f"faktorial dari {n}! adalah {hasil}")