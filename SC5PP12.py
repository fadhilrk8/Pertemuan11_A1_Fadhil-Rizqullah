def hitung_vol_kerucut(jari_jari,tinggi):
    pi = 3.14159
    volume = (1/3) * pi * (jari_jari ** 2) * tinggi
    return volume

#contoh
jari_jari_alas = int(input("Silahkan masukkan jari-jari: "))
tinggi_kerucut = int(input("Silahkan masukkan tinggi kerucut: "))
vol_kerucut = hitung_vol_kerucut(jari_jari_alas, tinggi_kerucut)
print(f"Volume kerucut ddengan jari-jari {jari_jari_alas}, dan tinggi {tinggi_kerucut}, adalah {vol_kerucut}")
