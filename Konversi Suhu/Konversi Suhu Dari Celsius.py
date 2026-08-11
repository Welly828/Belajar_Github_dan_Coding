#Konversi Suhu dari Celsius ke Satuan Lainnya.

celsius = float(input("Masukan Suhu Dalam Celsius:"))
print("--------------------------------------")
print("Suhu Adalah:", celsius, "Celsius")

reamur = (4/5) * celsius
print("Suhu dalam Reamur Adalah:", reamur, "Reamur")

fahrenheit = (9/5 * celsius) + 32
print("Suhu dalam Fahrenheit:", fahrenheit, "Fahrenheit")

kelvin = celsius + 273
print("Suhu dalam Kelvin", kelvin, "Kelvin")

print("--------------------------------------")
