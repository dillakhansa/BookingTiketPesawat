print("|===============================================|")
print("| LIST KEBERANGKATAN DASPRO LIGHT AIRBUS =======|")
print("|===============================================|")
print("| kode penerbangan | tujuan | harga tiket ======|")
print("|===============================================|")
print("| 101              | ENG/LDN    | Rp. 7.000.000 |")
print("| 102              | JPN/TKY    | Rp. 5.000.000 |")
print("| 103              | AUS/SYD    | Rp. 6.000.000 |")
print("| 104              | SGN/SING   | Rp. 2.200.000 |")
print("| 105              | THA/BGK    | Rp. 2.700.000 |")
print("| 106              | PHL/MNL    | Rp. 2.500.000 |")
print("|===============================================|")
print("")
nama = input("Nama Pembeli : ")
nomor = input("Nomor Handphone : ")
asal = input("Asal Kota : ")
jurusan = input("Kode Tujuan Penerbangan : ")
tujuan = []
harga = []
if jurusan == "101":
    tujuan.append("LONDON")
    harga = 7000000
elif jurusan == "102":
    tujuan.append("TOKYO")
    harga = 5000000
elif jurusan == "103":
    tujuan.append("SYDNEY")
    harga = 6000000
elif jurusan == "104":
    tujuan.append("SINGAPURA")
    harga = 2200000
elif jurusan == "105":
    tujuan.append("BANGKOK")
    harga = 2700000
elif jurusan == "106":
    tujuan.append("MANILA")
    harga = 2500000
else :
    tujuan.append("Kode Yang Anda Masukan Salah")

jumlah = int(input("Jumlah beli pembelian : "))
seat = input("Nomor seat: ")
print()
if jumlah ==2:
    potongan = int(jumlah*harga)*0.1
elif jumlah ==3:
    potongan = int(jumlah*harga)*0.12
elif jumlah ==4:
    potongan = int(jumlah*harga)*0.15
else:
    potongan =0

total = int(jumlah*harga-potongan)
pajak = int(total*0.11)
jumlah_bayar = total+pajak
def garis():

    print("-------------------------------------")
garis()
print("BUKTI PEMESANAN TIKET ANDA")
garis()
print("Nama Pembeli : ", nama)
print("Nomor Handphone : ", nomor)
print("Asal Negara : ", asal)
print("Kode Negara : ", jurusan)
print("Negara Tujuan : ", tujuan)
print("Jumlah Beli : ", jumlah)
print("Nomor seat: ", seat)
garis()
print("Harga tiket : Rp", harga)
print("Potongan    : Rp", potongan)
print("PPN 10%     : Rp", pajak)
garis()
print("Pelunasan pembayaran tiket")
print("Jumlah bayar : Rp", jumlah_bayar)
pembayaran = input("Metode Pembayaran: ")
uang = int(input("Masukan pembayaran : Rp."))
garis()
kembalian = uang-jumlah_bayar
print("Uang kembalian : Rp", kembalian)
garis()
print("ENJOY YOUR FLIGHT")
print("STAY SAFE")
print("PLEASE FOLLOW COVID-19 PROTOCOL")
