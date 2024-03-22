#Atur caa mengira luas permukaan dan isi padu silinder
#Isytihar pemalar
pi=3.142

#Kod input
jejari=float(input("Masukka jejari:"))
tinggi=float(input("Masukkan tinggi"))

#Kod proses
luaspermukaan=(2*pi*jejari*jejari)+(2*pi*jejari*tinggi)
isipadu=pi*(jejari*jejari)*tinggi

#Kod output
print("Luas permukaan silinder ialah",round(luaspermukaan,2),"dan isipadunya ialah",round(isipadu,2),".")
