#Input data
print("Data Pegawai PT. XYZ")
nama = input("Masukan Nama: ")
agama = input("Masukan Agama: ")
divisi = input("Masukan Divisi: ")
jabatan = input("Masukan Jabatan: ")

#Menentukan gaji pokok sesuai jabatan
if jabatan == "Staff" or jabatan == "staff":
   gapok = 4000000
elif jabatan == "Kabag" or jabatan == "kabag":
   gapok = 7000000
elif jabatan == "Manajer" or jabatan == "manajer":
   gapok = 10000000
else:
   gapok = 0

#Hitung tunjangan jabatan
tunjab = 0.2 * gapok

#Hitung gaji kotor
gator = gapok + tunjab

#Hitung pengeluaran zakat
zapro = (0.025 * gator) if (agama.lower() == "islam" and gator >= 7000000 ) else 0

#hitung gaji bersih
gasih = (gapok + tunjab) - zapro

#Cetak
print("\nHasil Sistem Penggajian PT. XYZ")
print(f"Nama               : {nama}")
print(f"Agama              : {agama}")
print(f"Divisi             : {divisi}")
print(f"Jabatan            : {jabatan}")
print(f"Gaji Pokok         : Rp {gapok:,.2f}")
print(f"Tunjangan Jabatan  : Rp {tunjab:,.2f}")
print(f"Gaji Kotor         : Rp {gator:,.2f}")
print(f"Zakat Profesi      : Rp {zapro:,.2f}")
print(f"Gaji Bersih        : {gasih:,.2f}")
