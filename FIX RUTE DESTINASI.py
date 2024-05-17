import pandas as pd

# Baca data dari file CSV (ganti dengan nama file yang sesuai)
data_route = pd.read_csv('Data_Route(AutoRecovered).csv')

# Fungsi untuk menampilkan daftar destinasi dan harga tiket
def tampilkan_destinasi():
    print("Daftar Destinasi Wisata:")
    for index, row in data_route.iterrows():
        print(f"{index + 1}. {row['id']} - nama_armada: {row['nama_armada']} - source_code: {row['source_code']} - destination_code: {row['destination_code']} - start_date: {row['start_date']} - end_date: {row['end_date']}")

# Fungsi untuk membeli tiket
def pilih_destinasi():
    tampilkan_destinasi()
    try:
        pilihan = int(input("Pilih nomor destinasi yang ingin Anda tuju: "))
        if 1 <= pilihan <= len(data_route):
            destinasi = data_route.loc[pilihan - 1, 'destination_code']
            keberangkatan = data_route.loc[pilihan - 1, 'source_code']
            jadwal = data_route.loc[pilihan - 1, 'start_date']
            print(f"pilihan rute destinasi tiket dari {keberangkatan} ke {destinasi} dengan jadwal keberangkatan {jadwal}")
        else:
            print("Nomor destinasi tidak valid. Silakan pilih nomor yang benar.")
    except ValueError:
        print("Masukkan angka yang valid.")

# Fungsi utama
def main():
    print("Selamat datang di layanan pembelian tiket destinasi wisata!")
    while True:
        print("\nMenu:")
        print("1. Tampilkan daftar destinasi")
        print("2. Pilih Destinasi")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            tampilkan_destinasi()
        elif pilihan == "2":
            pilih_destinasi()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()


