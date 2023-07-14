sampah_organik = ['daun', 
           'kulit buah', 
           'sisa makanan',
           'buah dan sayur busuk',
           'kotoran hewan',
           'ranting',
           'bangkai hewan']

sampah_anorganik = ['Botol sampah',
                    'kaca',
                    'plastik belanja',
                    'buku',
                    'kertas ujian yang nilainya E',
                    'kotak makanan kertas']

with open('organik.txt', 'w',encoding='UTF-8') as f:
    for i in sampah_organik:
        f.write(i + '\n')
    f.close()
   
with open('anorganik.txt', 'w',encoding='UTF-8') as f:
    for i in sampah_anorganik:
        f.write(i + '\n')
    f.close()

