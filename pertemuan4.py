# dict = {'mangga':'5 kg', 'jeruk':'10 kg', 'mangga2':'rp 10.000', 'jeruk2':'rp 1.000'}

# print ("andi beli mangga:",dict['mangga'],",jeruk :",dict['jeruk'])
# print ("Harga Mangga:",dict['mangga2'])
# print ("Harga Jeruk:",dict['jeruk2'])

# def salam():
#     print ("Hello")

# salam()

# def hitung(alas, tinggi):
#     luas = (alas * tinggi) / 2
#     print ('Luas Segitiga =%f'%luas)

# hitung(4,6)

# def persegi(x):
#     return x * x

    
# print ('Luas Persegi =',persegi(4))

# def luas_segitiga (a, b):
#     return (a*b)/2


# print ('Luas Segitiga =%d'%luas_segitiga(8,6))

#Global
nama = "Salsa"
versi = "1.0.0"

def help():

    #Lokal
    nama = "Programku"
    versi = "1.0.2"

    print ("Nama: %s"% nama)
    print ("Versi: %s"% versi)

print ("Nama: %s"% nama)
print ("Versi: %s"% versi)

help()