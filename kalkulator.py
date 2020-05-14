import time

def tambah(x, y):
	return(x + y)
	
def kurang(x, y):
	return(x - y)

def kali(x, y):
	return(x * y)
	
def bagi(x, y):
	return(x / y)
	
print("Kalkulator")
time.sleep(0.5)
print("Sederhana")
time.sleep(0.5)
print("Menu: ")
time.sleep(0.5)
print("1.Tambah	3.Kali")
print("2.kurang	4.bagi")
men = input('pilih mana? ')
num1 = int(input('Nilai A: '))
num2 = int(input('Nilai B: '))
if men == '1':
	print("hasil: ", num1, "+", num2, "=", tambah(num1,num2))
	