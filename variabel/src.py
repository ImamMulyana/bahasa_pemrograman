
print ("===variabel dan definisi===")
#variabel dan definisi
a = "Imam Mulyana\n"
def func():
    a = "any"
    print ("selamat " + a,"\n")
func()
print(a)

def tambah ():
    a = 5
    b = 3
    c = a+b
    print (c)
tambah()

print ("===definisi parameter===")
#definisi parameter
def data (nama, nim):
    print ("Nama saya",nama," dan NIM saya",nim)
data ("Imam", "20210801234\n")

#contoh
def total (sisi):
    return sisi*sisi
print(total(5))
def segitiga (alas, tinggi):
    return 0.5*alas*tinggi
print (segitiga(5, 20))