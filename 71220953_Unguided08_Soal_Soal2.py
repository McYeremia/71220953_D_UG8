a= int(input('Masukkan tinggi Diamond: '))
if a%2 == 0:
    print("angka harus ganjil")
else:
    with open('diamond.txt','w') as tulis:
        for i in range(a-2):
            tulis.write(" " * (a-i-1))
            tulis.write("*" * (2*i+1) + '\n')
        for j in range(a-4, -1, -1):
            tulis.write(" " * (a-j-1))
            tulis.write("*" * (2*j+1) + '\n')