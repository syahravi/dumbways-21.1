def string(word,words): #Fungsi Penghitung
    d = 0
    for c in words:
        if c is word:
            d +=1
        else:
            pass

    print ("Original String: ", words)
    print('----------------------------->')
    print (f"Hasil Hitung huruf {word} muncul sebanyak {d} kali") 

# Eksekusi Program!
string('a','saya mau makan sate bersama teman saya setelah lulus dari sekolah dasar')


'''
Sederhana banget wkwk
,harusnya bisa lebih dikit dari ini baris codenya ;>
'''