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
        
        translate = controller.kataIndonesia()
         
    elif menu == "2":
        
        translate = controller.kataInggris()
        
    elif menu == "3":
        
        translate = controller.kataJepang()
    else:
        print("="*30)
        print("Pilihan tidak valid!")
        print("="*30)
        continue
    