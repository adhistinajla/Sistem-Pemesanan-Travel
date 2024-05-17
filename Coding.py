import pandas as pd
data_route = pd.read_csv('Data_Route.csv')
print(data_route)

# Membuat Variable
id_pemesanan = [id]
nama_armada = []
code_kota = []

# Pengkondisian atau perulangan
jumlah_pesanan = int(input("Masukkan Jumlah Pesanan Tiket: "))
for i in range (jumlah_pesanan):
    print("Pesanan ke : ", i+1)