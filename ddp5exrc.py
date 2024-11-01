kontak = {'safira' : '08624257' , 'ibu_safira' : '00826544'}
kontak['safira'] = '098765432'
print(kontak['safira'])

#menambah elemen ke dalam dictionary
kontak['Safira'] ='07892345'
print(kontak)

#exercise1
kendaraan =['alphard', 'mobil', 1000, 'hitam', 4 ]
print(kendaraan)
kendaraan.append('500jt')
kendaraan.append('matic')
print(kendaraan)
kendaraan.insert(1, 'toyota')
print(kendaraan)
print(type(kendaraan))
print(type(kendaraan[0]))
print(type(kendaraan[1]))
print(type(kendaraan[2]))
print(type(kendaraan[3]))
print(type(kendaraan[4]))
print(type(kendaraan[5]))
print(type(kendaraan[6]))
print(type(kendaraan[7]))

#luas persegi
hitung_luas = int(input("""pilih salah satu:
1. hitung luas persegi          
2. hitung luas lingkaran                  
3. hitung luas segitiga                    
 """))
match hitung_luas :
    case 1:
        print('menghitung luas persegi')
        sisi = int(input('masukan nilai sisi'))
        hitung_luas_persegi = sisi **2 
        print(f'jadi luas persegi dengan sisi {sisi} cm, adalah {hitung_luas_persegi} cm^2') 
    
    case 2:
        print('menghitung luas lingkaran')
        r= int(input('masukan nilai jari_jari'))
        phi= 22/7
        hitung_luas_lingkaran = phi*r**2
        print(f'jadi luas lingkaran dengan phi {r} cm, adalah {hitung_luas_lingkaran} cm^2')
        
    case 3:
         print('menghitung luas segitiga')
         a= int(input('masukan nilai sisi'))
         t= int(input('masukan nilai tinggi'))
         hitung_luas_segitiga = 0.5*a**2*t
         print(f'jadi luas segitiga dengan tinggi {t} cm, adalah {hitung_luas_segitiga} cm^2')

    case _:
        print('pilihan tidak valid')
                     