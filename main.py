while True:
    print("""
      MENU YANG TERSEDIA DI KAMUS INI :
      
      1. Translate dari Bahasa Indonesia   
      2. Translate dari Bahasa Inggris
      3. Translate dari Bahasa Jepang
      
      
      """)
    
        
    menu = input("Menu yang anda pilih : ")
    
    if menu == "1":
        translate = input("Masukkan nama hewan yang ingin di terjemahkan: ").lower()
        
        from db import indonesia 
        in_en = indonesia.indonesiaToEnglish(translate)
        in_jp = indonesia.indonesiaToJapan(translate)
        
        from src import ind 
        ina = ind.indonesia(translate)
        
        if translate == ina:
            print("="*50)
            print(f"Kata yang dimasukkan : {translate}")
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
                print(f"Terjemahan dari ( {translate} ) ke bahasa Inggris adalah : {terjemahan}")
                print("-"*90)
                break
            elif pilihan == "2":
                terjemahan = in_jp
                print("-"*90)
                print(f"Terjemahan dari ( {translate} ) ke bahasa Jepang adalah : {terjemahan}")
                print("-"*90)
                break
            else:
                print("pilihan tidak valid!")
                continue
        else:
            print("Pilihan tidak valid!")
            continue  
    elif menu == "2":
        translate = input("Masukkan nama hewan yang ingin di terjemahkan: ").lower()
        
        from db import inggris
        en_in = inggris.englishToIndonesia(translate)
        en_jp = inggris.englishToJapan(translate)
        
        from src import eng
        en = eng.english(translate)
        
        
        if translate == en:
            print("="*50)
            print(f"Kata yang dimasukkan : {translate}")
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
                print(f"Terjemahan dari ( {translate} ) ke bahasa Indonesia : {terjemahan}")
                print("-"*90)
                break
            elif pilihan == "2":
                terjemahan = en_jp
                print("-"*90)
                print(f"Terjemahan dari ( {translate} ) ke bahasa Jepang : {terjemahan}")
                print("-"*90)
                break
            else:
                print("Pilihan tidak valid!")
                continue
        else:
            print("Pilihan tidak valid!")
            continue
    elif menu == "3":
        translate = input("Masukkan nama hewan yang ingin di terjemahkan: ").lower()
        
        from db import jepang
        jp_in = jepang.japanToIndonesia(translate)
        jp_en = jepang.japanToEnglish(translate)
        
        from src import jpg
        jap = jpg.jepang(translate)
        
        
        if translate == jap:
            print("="*50)
            print(f"Bahasa yang dimasukkan : {translate}")
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
                print(f"Terjemahan dari ( {translate} ) ke bahasa Indonesia : {terjemahan}")
                print("-"*90)
                break
            elif pilihan == "2":
                terjemahan = jp_en
                print("-"*90)
                print(f"Terjemahan dari ( {translate} ) ke bahasa Inggris : {terjemahan}")
                print("-"*90)
                break
            else:
                print("Pilihan tidak valid!")
                continue
        else:
            print("Pilihan tidak valid!")
            continue
    else:
        print("="*30)
        print("Pilihan tidak valid!")
        print("="*30)
        continue
    