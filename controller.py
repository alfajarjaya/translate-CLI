from db import indonesia,inggris,jepang
from src import ind,eng,jpg
    
def kataIndonesia():
    
    kata = input("Masukkan kata yang akan diterjemahkan: ").lower()
    
    in_en = indonesia.indonesiaToEnglish(kata)
    in_jp = indonesia.indonesiaToJapan(kata)
    
    a = ind.indonesia(kata)

    while True:
        if kata not in a:
            print(f"kata : ( {kata} ) tidak dalam bahasa indonesia")
            return
        else:
            print("="*50)
            print(f"Kata yang dimasukkan : {kata}")
            print("="*50)
            
        
            print("""
              
            KAMUS YANG TERSEDIA :
              
            1. Bahasa Indonesia -> Bahasa Inggris
            2. Bahasa Indonesia -> Bahasa Jepang
                  """)

            pilihan = input("Translate ke bahasa mana nih ? ( pilih nomor di atas / pilih huruf 'x' untuk mengakhiri ) : ").lower()  
        
            if pilihan == "x":      
                print("")
                print("|","="*48,"|")
                print("|   Terima kasih telah menggunakan layanan kami.   |")
                print("|","="*48,"|")
                print("")
                break
            elif pilihan == "1":
                terjemahan = in_en
                print("-"*90)
                print(f"Terjemahan dari ( {kata} ) ke bahasa Inggris adalah : {terjemahan}")
                print("-"*90)
                break
            elif pilihan == "2":
                terjemahan = in_jp
                print("-"*90)
                print(f"Terjemahan dari ( {kata} ) ke bahasa Jepang adalah : {terjemahan}")
                print("-"*90)
                break
            else:
                print("pilihan tidak valid!")
                continue
            
def kataInggris():
    
    kata = input("Masukkan kata yang akan diterjemahkan: ").lower()
    
    en_in = inggris.englishToIndonesia(kata)
    en_jp = inggris.englishToJapan(kata)
    
    a = eng.english(kata)

    while True:
        if kata not in a:
            print(f"kata : ( {kata} ) tidak dalam bahasa Ingggris")
            return
        else:
            print("="*50)
            print(f"Kata yang dimasukkan : {kata}")
            print("="*50)
        
            print("""
              
                KAMUS YANG TERSEDIA :

                1. Bahasa Inggris -> Bahasa Indonesia
                2. Bahasa Inggris -> Bahasa Jepang
                  """)
        
            pilihan = input("Translate ke bahasa mana nih ? ( pilih nomor di atas / pilih huruf 'x' untuk mengakhiri ) : ").lower()
        
            if pilihan == "x":      
                print("")
                print("|","="*48,"|")
                print("|   Terima kasih telah menggunakan layanan kami.   |")
                print("|","="*48,"|")
                print("")
                break
            elif pilihan == "1":
                terjemahan = en_in
                print("-"*90)
                print(f"Terjemahan dari ( {kata} ) ke bahasa Indonesia : {terjemahan}")
                print("-"*90)
                break
            elif pilihan == "2":
                terjemahan = en_jp
                print("-"*90)
                print(f"Terjemahan dari ( {kata} ) ke bahasa Jepang : {terjemahan}")
                print("-"*90)
                break
            else:
                print("Pilihan tidak valid!")
                continue
            
def kataJepang():
    
    kata = input("Masukkan kata yang akan diterjemahkan: ").lower()
    
    jp_in = jepang.japanToIndonesia(kata)
    jp_en = jepang.japanToEnglish(kata)
    
    a = jpg.jepang(kata)
    
    while True:    
        if kata not in a:
            print(f"kata : ( {kata} ) tidak dalam bahasa Ingggris")
            return
        else:
            print("="*50)
            print(f"Kata yang dimasukkan : {kata}")
            print("="*50)
        
            print("""
              
                KAMUS YANG TERSEDIA :
            
                1. Bahasa Jepang -> Bahasa Indonesia
                2. Bahasa Jepang -> Bahasa Inggris
                  """)
        
            pilihan = input("Translate ke bahasa mana nih ? ( pilih nomor di atas / pilih huruf 'x' untuk mengakhiri ) : ").lower()
        
            if pilihan == "x":      
                print("")
                print("|","="*48,"|")
                print("|   Terima kasih telah menggunakan layanan kami.   |")
                print("|","="*48,"|")
                print("")
                break
            elif pilihan == "1":
                terjemahan = jp_in
                print("-"*90)
                print(f"Terjemahan dari ( {kata} ) ke bahasa Indonesia : {terjemahan}")
                print("-"*90)
                break
            elif pilihan == "2":
                terjemahan = jp_en
                print("-"*90)
                print(f"Terjemahan dari ( {kata} ) ke bahasa Inggris : {terjemahan}")
                print("-"*90)
                break
            else:
                print("Pilihan tidak valid!")
                continue  