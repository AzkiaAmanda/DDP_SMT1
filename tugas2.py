#Data Pegawai
p1 = {"nama": "Budi", "jabatan": "Manager", "agama": "Islam", "status": "Menikah"}
p2 = {"nama": "Siti", "jabatan": "Asisten Manager", "agama": "Islam", "status": "Menikah"}
p3 = {"nama": "I Gede", "jabatan": "Supervisor", "agama": "Hindu", "status": "Menikah"}
p4 = {"nama": "Joko", "jabatan": "Staff", "agama": "Islam", "status": "Belum Menikah"}
p5 = {"nama": "Alex", "jabatan": "Staff", "agama": "Kristen Protestan", "status": "Belum Menikah"}

#List Pegawai
ar_pegawai= [p1, p2, p3, p4, p5]

#gaji pokok
for pegawai in ar_pegawai:
    if pegawai ['jabatan'] == "Manager":
        pegawai ['gaji_pokok'] = 15000000 #15jt
    elif pegawai ['jabatan'] == "Asisten Manager":
        pegawai ['gaji_pokok'] = 10000000 #10jt
    elif pegawai ['jabatan'] == "Supervisor":
        pegawai ['gaji_pokok'] = 7000000 #7jt
    elif pegawai ['jabatan'] == "Staff":
        pegawai ['gaji_pokok'] = 4000000 #4jt
    else:
        pegawai ['gaji_pokok'] = 0

    #tunjangan jabatan
    pegawai ['tunjab'] =  pegawai ['gaji_pokok'] * 30/100

    #BPJS
    pegawai['bpjs'] =  pegawai ['gaji_pokok'] * 10/100

    #tunjangan keluarga (tuple & list)
    pegawai['tukel'] = (0, pegawai['gaji_pokok'] * 0.1)[pegawai['status'] == 'Menikah']

    #gaji kotor
    pegawai ['gaji_kotor'] = pegawai ['gaji_pokok'] + pegawai ['tunjab'] + pegawai ['bpjs'] + pegawai ['tukel']

    #zakat profesi
    pegawai['zapro'] = (0, pegawai['gaji_kotor'] * 2.5/100)[pegawai['agama'] == 'Islam' and pegawai['gaji_kotor'] >= 7000000]

    #gaji bersih
    pegawai ['gaji_bersih'] = pegawai ['gaji_kotor'] - pegawai ['zapro']

    #cetak slip gaji
    print('-----Cetak Slip Gaji Pegawai-----')
    print(f"Nama \t\t\t: {pegawai['nama']} "
        f"\nJabatan \t\t: {pegawai['jabatan']}"
        f"\nAgama \t\t\t: {pegawai['agama']}"
        f"\nStatus \t\t\t: {pegawai['status']}"
        f"\nGaji Pokok \t\t: {pegawai['gaji_pokok']}"
        f"\nTunjangan Jabatan \t: {pegawai['tunjab']}"
        f"\nBPJS \t\t\t: {pegawai['bpjs']}"
        f"\nTunjangan Keluarga \t: {pegawai['tukel']}"
        f"\nGaji Kotor \t\t: {pegawai['gaji_kotor']}"
        f"\nZakat Profesi \t\t: {pegawai['zapro']}"
        f"\nGaji Bersih \t\t: {pegawai['gaji_bersih']}"
        )
    print('---------------------------------')
    print('')