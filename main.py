import controller

while True:
    print("""
      MENU YANG TERSEDIA DI KAMUS INI :
      
      1. Translate dari Bahasa Indonesia   
      2. Translate dari Bahasa Inggris
      3. Translate dari Bahasa Jepang
      
      
      """)
    
    menu = input("Menu yang anda pilih : ")
    
    if menu == "1":
        
        controller.kataIndonesia()
        break
         
    elif menu == "2":
        
        controller.kataInggris()
        break
        
    elif menu == "3":
        
        controller.kataJepang()
        break
        
    else:
        print("="*30)
        print("Pilihan tidak valid!")
        print("="*30)
        continue 