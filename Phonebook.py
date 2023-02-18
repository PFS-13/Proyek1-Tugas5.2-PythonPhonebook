import os

#DEFINE A MENU FUNCTION
def menu():
    #ENTRY VARIABLE
    entry = int(input("""Selamat datang di Buku Kontak Raizenway.
    Silahkan pilih opsi...
    1. Display kontak saat ini
    2. Tambah kontak baru
    3. Cek nomor                            
    4. Hapus nomor
    5. Update nomor
    6. Exit 
    Masukkan opsi... """))
    return entry

#DEFINE A FUNCTION PHONEBOOK
def phonebook():

    #inisiasi perulangan while untuk menjalankan program phonebook secara berkelanjutan
    while True:
        #panggil menu
        #set variabel entri dengan function menu
        os.system('cls')
        entry = menu()

        #LIST KONTAK
        if entry == 1:
        # untuk entri pertama, cek apakah buku kontak kosong
        # jika kosong, maka print kontak list
            with open("Kontak.txt", "r") as file:
                lines = file.readlines()

            if len(lines) > 0:
                # baca file
                with open("Kontak.txt", "r") as file:
                    print(file.read())
                input("Tekan enter untuk kembali ke menu... ")
                # jika tidak, informasikan pengguna bahwa kontak kosong
            else:
                print("Kontak kamu kosong nih :( Yuk tambah kontak baru dulu!")

        #TAMBAH KONTAK
        elif entry == 2:
            #minta input nomor dan nama kontak
            file = open("Kontak.txt", "r")
            phone_number = input('Silahkan masukkan nomor ')
            contact_name = input('Silahkan masukkan nama kontak: ')
            #cek apakah nomor kontak sudah tersedia
            #jika tidak, maka update list kontak terkini
            lines = file.readlines()
            found = False
            #cek

            for line in lines:
                if line.find(contact_name) != -1:
                    print('Nomor sudah ada di dalam buku kontak!')
                    found = True
                    input("Tekan enter untuk kembali ke menu... ")                    
            if not found:
                with open("Kontak.txt", "a") as file:
                    file.write(contact_name)
                    file.write('\n')
                    file.write(phone_number)
                    file.write('\n\n')
                    #tampilkan pesan berhasil
                    print('Kontak berhasil disimpan')
                    input("Tekan enter untuk kembali ke menu... ")
                
            file.close()

        #CEK NOMOR
        elif entry == 3:
            file = open("Kontak.txt", "r")
            lines = file.readlines()
            #inisiasi nama variabel
            name = input('Masukkan nama/nomor kontak yang ingin anda lihat: ')
            found = False
            #cek
            for line in lines:
                if line.find(name) != -1:
                    if name[0]=='0' or name[0]=='6'or name[0]=='+':
                        index = lines.index(line)
                        print(lines[index-1], lines[index], sep='')
                        found = True
                        input("Tekan enter untuk kembali ke menu... ")
                    else:
                        index = lines.index(line)
                        print(lines[index], lines[index+1], sep='')
                        found = True
                        input("Tekan enter untuk kembali ke menu... ")
                    
            if not found:
                print('Kontak tidak ada')
                input("Tekan enter untuk kembali ke menu... ")                  

        #OPSI MENGHAPUS
        elif entry == 4:
            with open('Kontak.txt', 'r') as fr:
                # reading line by line
                lines = fr.readlines()
                found = False
                # pointer for position
                name = input('Masukkan nama kontak yang ingin anda hapus: ')
                for line in lines:
                    if line.find(name) != -1:
                        found = True
                        konfirmasi = input('Apakah kamu yakin untuk menghapus kontak ini? Ya/Tidak\n')
                        if konfirmasi == 'Ya':
                            # opening in writing mode
                            with open('Kontak.txt', 'w') as fw:
                                #cari cek poin
                                for line in lines:
                                    if line.find(name) != -1:
                                        nomordihapus = lines.index(line)

                                for line in lines:
                                # we want to remove name line
                                    if line.strip('\n') != name:
                                        if line != lines[nomordihapus+1]:
                                            if lines.index(line) != nomordihapus:
                                                fw.write(line)
                            print("Deleted")
                        
            if not found:
                print("Kontak tidak ada")

            input("Tekan enter untuk kembali ke menu... ") 

        #UPDATE
        elif entry == 5:
            file = open("Kontak.txt", "r")
            lines = file.readlines()
            #inisiasi nama variabel
            opsi = input('Ingin update nama atau nomor kontak?\n1. Nama\n2. Nomor\n')
            found = False
            #cek
            if opsi == '1':
                name = input('Masukkan nama kontak :')
                for line in lines: 
                    if line.find(name) != -1:
                        index = lines.index(line)
                        found = True
                        namabaru = input('Silahkan masukkan nama baru: ')
                        lines[index] = namabaru+('\n')
                        with open("Kontak.txt", "w") as file:
                            file.writelines(lines)
                        print('Nama berhasil di perbarui')
                        input("Tekan enter untuk kembali ke menu... ")

                if not found:
                        print('Kontak tidak ada')
                        input("Tekan enter untuk kembali ke menu... ")

            elif opsi == '2':
                nomor = input('Masukkan nomor kontak :')
                for line in lines:
                    if line.find(nomor) != -1:
                        index = lines.index(line)
                        found = True
                        nomorbaru = input('Silahkan masukkan nomor baru: ')
                        lines[index] = nomorbaru+('\n')
                        with open("Kontak.txt", "w") as file:
                            file.writelines(lines)
                        print('Nomor berhasil di perbarui')
                        input("Tekan enter untuk kembali ke menu... ")
                if not found:
                    print('Kontak tidak ada')
                    input("Tekan enter untuk kembali ke menu... ")

        elif entry == 6:
            print('Terima kasih telah menggunakan Buku Kontak Raizenway')
            break

        #Error
        else:
            print('Opsi salah!')

        #end

phonebook()