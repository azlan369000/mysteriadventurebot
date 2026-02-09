import time
import random

class PemainAdventure:
    def __init__(self, nama):
        self.nama = nama
        self.kesehatan = 100
        self.nyawa = 3
        self.inventory = []
        self.poin = 0
        self.lokasi_sekarang = "desa"
        
    def tampilkan_status(self):
        print(f"\n{'='*50}")
        print(f"Status {self.nama}")
        print(f"{'='*50}")
        print(f"❤️  Kesehatan: {self.kesehatan}/100")
        print(f"⭐ Nyawa: {self.nyawa}")
        print(f"💰 Poin: {self.poin}")
        print(f"🎒 Inventory: {', '.join(self.inventory) if self.inventory else 'Kosong'}")
        print(f"📍 Lokasi: {self.lokasi_sekarang}")
        print(f"{'='*50}\n")
        
    def tambah_item(self, item):
        self.inventory.append(item)
        print(f"✨ Anda mendapatkan {item}!")
        
    def gunakan_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False

def intro_cerita():
    print("\n" + "="*60)
    print("🎮 SELAMAT DATANG DI PETUALANGAN MISTERI ADVENTURE 🎮")
    print("="*60)
    print("\nAnda adalah seorang petualang yang baru tiba di desa misterius.")
    print("Desa ini terkenal dengan peristiwa aneh yang terjadi setiap malam.")
    print("Tujuan Anda adalah mengungkap misteri di balik kejadian itu.\n")

def desa(pemain):
    print("\n📍 ANDA BERADA DI DESA MISTERIUS")
    print("-" * 50)
    print("\nAnda melihat desa yang sepi dengan beberapa bangunan:")
    print("1. 🏠 Rumah Penduduk - Rumah tua yang tampak ditinggalkan")
    print("2. 🏪 Toko Penjual - Mungkin ada perlengkapan berguna")
    print("3. 🌲 Hutan Gelap - Suara aneh terdengar dari sana")
    print("4. 📖 Perpustakaan Kuno - Mungkin berisi informasi penting")
    print("5. 📊 Lihat Status")
    print("6. 🚪 Keluar Game")
    
    pilihan = input("\nPilihan Anda (1-6): ").strip()
    
    if pilihan == "1":
        rumah(pemain)
    elif pilihan == "2":
        toko(pemain)
    elif pilihan == "3":
        hutan(pemain)
    elif pilihan == "4":
        perpustakaan(pemain)
    elif pilihan == "5":
        pemain.tampilkan_status()
        desa(pemain)
    elif pilihan == "6":
        print("\n👋 Terima kasih telah bermain! Sampai jumpa!")
        return False
    else:
        print("❌ Pilihan tidak valid!")
        desa(pemain)
    
    return True

def rumah(pemain):
    print("\n🏠 ANDA MEMASUKI RUMAH PENDUDUK")
    print("-" * 50)
    print("\nRumah ini sangat gelap dan dingin. Ada debu di mana-mana.")
    print("Tiba-tiba, Anda melihat bayangan misterius bergerak cepat!")
    print("\n1. ⚔️  Hadapi bayangan tersebut")
    print("2. 🏃 Lari dan kembali ke desa")
    
    pilihan = input("\nPilihan Anda (1-2): ").strip()
    
    if pilihan == "1":
        if pertarungan(pemain, "Bayangan Misterius", 50):
            print("\n✅ Anda menang! Di sudut rumah, Anda menemukan:")
            pemain.tambah_item("Kunci Emas")
            pemain.poin += 50
        else:
            if pemain.nyawa > 0:
                print("\n🏃 Anda kabur dari rumah dengan selamat!")
    elif pilihan == "2":
        print("\n🏃 Anda berlari keluar rumah!")
    
    desa(pemain)

def toko(pemain):
    print("\n🏪 ANDA MASUK KE TOKO PENJUAL")
    print("-" * 50)
    print("\nSeorang penjual tua melihat Anda dengan pandangan curiga.")
    penjual_dialog = [
        "Halo, ada yang bisa saya bantu?",
        "Barang-barang langka ada di sini...",
        "Jika Anda mencari sesuatu, saya punya informasi berharga."
    ]
    print(f"\nPenjual: {random.choice(penjual_dialog)}")
    
    print("\n🛍️  LAYANAN TOKO:")
    print("1. 💊 Beli Ramuan Penyembuh (Pulihkan 50 Kesehatan) - 20 Poin")
    print("2. 🗡️  Beli Pedang Besi (Senjata Bagus) - 30 Poin")
    print("3. 🗺️  Beli Peta Rahasia - 15 Poin")
    print("4. 💬 Minta Informasi - Gratis")
    print("5. ↩️  Kembali ke Desa")
    
    pilihan = input("\nPilihan Anda (1-5): ").strip()
    
    if pilihan == "1":
        if pemain.poin >= 20:
            pemain.poin -= 20
            pemain.kesehatan = min(100, pemain.kesehatan + 50)
            print("\n💊 Anda minum ramuan. Kesehatan pulih!")
        else:
            print("\n❌ Poin tidak cukup!")
    elif pilihan == "2":
        if pemain.poin >= 30:
            pemain.poin -= 30
            pemain.tambah_item("Pedang Besi")
        else:
            print("\n❌ Poin tidak cukup!")
    elif pilihan == "3":
        if pemain.poin >= 15:
            pemain.poin -= 15
            pemain.tambah_item("Peta Rahasia")
        else:
            print("\n❌ Poin tidak cukup!")
    elif pilihan == "4":
        informasi = [
            "Misteri ini dimulai 5 tahun lalu, tidak ada yang berani keluar malam hari...",
            "Katanya ada makhluk aneh di hutan yang menjaga sesuatu yang berharga...",
            "Kunci Emas adalah kunci untuk membuka pintu gua rahasia!"
        ]
        print(f"\nPenjual: {random.choice(informasi)}")
    elif pilihan == "5":
        return
    
    toko(pemain)

def hutan(pemain):
    print("\n🌲 ANDA MEMASUKI HUTAN GELAP")
    print("-" * 50)
    print("\nHutan sangat gelap dan suram. Pohon-pohon besar menjulang tinggi.")
    print("Anda mendengar suara makhluk aneh...")
    print("\n1. ⚔️  Serang makhluk tersebut")
    print("2. 🤐 Bersembunyi dan amati")
    print("3. 🏃 Lari kembali")
    
    pilihan = input("\nPilihan Anda (1-3): ").strip()
    
    if pilihan == "1":
        if "Pedang Besi" in pemain.inventory:
            print("\n⚔️  Dengan Pedang Besi, Anda merasa lebih percaya diri!")
            if pertarungan(pemain, "Makhluk Hutan", 60):
                print("\n✅ Makhluk terpukul mundur!")
                pemain.tambah_item("Kristal Mistis")
                pemain.poin += 100
            else:
                if pemain.nyawa == 0:
                    return
        else:
            if pertarungan(pemain, "Makhluk Hutan", 60):
                print("\n✅ Anda berhasil!")
                pemain.poin += 50
            else:
                if pemain.nyawa == 0:
                    return
    elif pilihan == "2":
        print("\n🤐 Anda menyembunyikan diri dan mengamati...")
        print("Makhluk itu terlihat seperti penjaga sesuatu yang penting...")
        print("Anda perlu persiapan lebih baik untuk menghadapinya.")
    elif pilihan == "3":
        print("\n🏃 Anda keluar dari hutan dengan cepat!")
    
    desa(pemain)

def perpustakaan(pemain):
    print("\n📖 ANDA MASUK KE PERPUSTAKAAN KUNO")
    print("-" * 50)
    print("\nBuku-buku bertumpuk di mana-mana. Ada aroma kertas tua dan lembab.")
    print("Seorang pustakawan tua memandang Anda dengan terkejut.")
    
    if "Peta Rahasia" in pemain.inventory:
        print("\nPustakawan: 'Ah! Anda memiliki Peta Rahasia! Ikuti saya...'")
        print("\nPustakawan membawa Anda ke ruang rahasia di bawah perpustakaan.")
        print("Di sana, Anda menemukan catatan tentang misteri desa:")
        print("- Kristal Mistis adalah sumber kekuatan aneh di desa")
        print("- Kunci Emas membuka gua tempat Kristal disimpan")
        print("- Anda harus menggabungkan keduanya untuk menghentikan misteri!")
        pemain.poin += 100
    else:
        print("\nPustakawan: 'Anda seperti orang asing. Tidak ada yang istimewa di sini.'")
        print("Pustakawan menunjukkan Anda ke pintu keluar, tanpa banyak bicara.")
    
    desa(pemain)

def pertarungan(pemain, musuh, kesehatan_musuh):
    print(f"\n⚔️  PERTARUNGAN! Anda melawan {musuh}!")
    print("-" * 50)
    
    putaran = 0
    while pemain.kesehatan > 0 and kesehatan_musuh > 0:
        putaran += 1
        print(f"\n📍 Putaran {putaran}")
        print(f"Kesehatan Anda: {pemain.kesehatan} | Kesehatan {musuh}: {kesehatan_musuh}")
        
        print("\n1. ⚔️  Serangan Kuat (60% akurat)")
        print("2. 🛡️  Pertahanan Kuat (Kurangi 50% damage)")
        print("3. 💣 Serangan Dasar")
        
        pilihan = input("Pilihan Anda (1-3): ").strip()
        
        pertahanan = False
        if pilihan == "1":
            if random.random() < 0.6:
                damage = random.randint(20, 40)
                kesehatan_musuh -= damage
                print(f"\n✅ Ambil! {musuh} menerima {damage} damage!")
            else:
                print("\n❌ Serangan meleset!")
        elif pilihan == "2":
            pertahanan = True
            print("\n🛡️  Anda bertahan dengan kuat!")
        elif pilihan == "3":
            damage = random.randint(8, 15)
            kesehatan_musuh -= damage
            print(f"\n⚔️  Anda mengeluarkan {damage} damage!")
        
        # Serangan musuh
        if kesehatan_musuh > 0:
            damage_musuh = random.randint(10, 25)
            if pertahanan:
                damage_musuh = int(damage_musuh * 0.5)
                print(f"\n🛡️  Pertahanan Anda mengurangi sebagian damage!")
            
            pemain.kesehatan -= damage_musuh
            print(f"🔥 {musuh} menyerang Anda! Anda menerima {damage_musuh} damage!")
        
        # Penyembuhan otomatis jika kesehatan kritis
        if pemain.kesehatan <= 20:
            print(f"\n⚠️  Kesehatan Anda kritis! ({pemain.kesehatan}/100)")
        
        time.sleep(1)
    
    if pemain.kesehatan > 0:
        print(f"\n✅ MENANG! Anda mengalahkan {musuh}!")
        return True
    else:
        pemain.nyawa -= 1
        print(f"\n💀 KALAH! Anda dikalahkan oleh {musuh}...")
        print(f"Nyawa tersisa: {pemain.nyawa}")
        
        if pemain.nyawa > 0:
            print("\n⚡ Anda bangkit kembali dengan penuh semangat!")
            pemain.kesehatan = 50
        else:
            print("\n💀 GAME OVER! Anda tidak memiliki nyawa lagi!")
            print(f"Total poin yang didapat: {pemain.poin}")
            return False
        
        return False

def game_utama():
    intro_cerita()
    nama = input("Siapa nama petualang Anda? ").strip()
    
    if not nama:
        nama = "Petualang Tanpa Nama"
    
    pemain = PemainAdventure(nama)
    pemain.poin = 30  # Modalkan pemain dengan poin awal
    
    print(f"\n✨ Selamat datang, {nama}!")
    print("Petualangan Anda dimulai sekarang...\n")
    time.sleep(2)
    
    # Loop game utama
    while pemain.nyawa > 0:
        if not desa(pemain):
            break
    
    # Akhir cerita
    if pemain.poin >= 200:
        print("\n🎉 SELAMAT! ANDA MENGUNGKAP MISTERI DESA!")
        print(f"Total Poin: {pemain.poin}")
        print("Desa menghargai keberanian Anda... Misteri telah terpecahkan!")
    else:
        print("\n📖 Cerita berakhir di sini...")
        print(f"Total Poin yang dikumpulkan: {pemain.poin}")

if __name__ == "__main__":
    game_utama()