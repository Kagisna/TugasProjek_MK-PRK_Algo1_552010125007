FILE_GAME = "kfm.txt"
FILE_KOLEKSI = "koleksi.txt"

# ===== WARNA ANSI =====
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

# ---------- MENU ----------
def tampil_menu():
    print(CYAN + BOLD)
    print("╔════════════════════════════════════╗")
    print("║        🎮 KOLEKSI GAME 🎮          ║")
    print("╠════════════════════════════════════╣")
    print("║ 1.  ➕ Tambah Game                 ║")
    print("║ 2.  📋 Tampilkan Semua Game        ║")
    print("║ 3.  ⭐ Tambah ke Koleksi           ║")
    print("║ 4.  💎 Lihat Koleksi Game          ║")
    print("║ 5.  ❌ Keluar                      ║")
    print("╚════════════════════════════════════╝")
    print(RESET)

# ---------- TAMBAH GAME ----------
def tambah_game():
    judul = input("🎮 Nama Game   : ")
    developer = input("👨 Developer   : ")
    device = input("💻 Device       : ")
    genre = input("🎯 Genre        : ")

    while True:
        tahun = input("📅 Tahun Rilis  : ")
        if tahun.isdigit() and len(tahun) == 4:
            break
        print(RED + "⚠ Tahun harus 4 digit!" + RESET)

    with open(FILE_GAME, "a") as file:
        file.write(f"{judul}|{developer}|{device}|{genre}|{tahun}\n")

    print(GREEN + "✅ Game berhasil disimpan\n" + RESET)

# ---------- LIHAT GAME ----------
def lihat_game():
    try:
        with open(FILE_GAME, "r") as file:
            data = file.readlines()

        if not data:
            print(RED + "📭 Data kosong" + RESET)
            return

        for i, baris in enumerate(data, 1):
            g = baris.strip().split("|")
            print(f"{i}. {g[0]} ({g[4]}) - {g[3]}")

    except FileNotFoundError:
        print(RED + "⚠ File game belum ada" + RESET)

# ---------- TAMBAH KOLEKSI ----------
def tambah_koleksi():
    judul = input("⭐ Nama game favorit: ")
    tahun = input("📅 Tahun rilis: ")

    with open(FILE_KOLEKSI, "a") as file:
        file.write(f"{judul}|{tahun}\n")

    print(GREEN + "✅ Game ditambahkan ke koleksi\n" + RESET)

# ---------- LIHAT KOLEKSI ----------
def lihat_koleksi():
    try:
        with open(FILE_KOLEKSI, "r") as file:
            data = file.readlines()

        if not data:
            print(RED + "📭 Koleksi kosong" + RESET)
            return

        print(CYAN + BOLD + "\n⭐ GAME FAVORIT\n" + RESET)
        for baris in data:
            g = baris.strip().split("|")
            print(f"🎮 {g[0]} ({g[1]})")

    except FileNotFoundError:
        print(RED + "⚠ File koleksi belum ada" + RESET)

# ---------- PROGRAM UTAMA ----------
while True:
    tampil_menu()
    pilih = input("👉 Pilih menu (1-5): ")

    if pilih == "1":
        tambah_game()
    elif pilih == "2":
        lihat_game()
    elif pilih == "3":
        tambah_koleksi()
    elif pilih == "4":
        lihat_koleksi()
    elif pilih == "5":
        print(GREEN + "🙏 Program selesai" + RESET)
        break
    else:
        print(RED + "⚠ Pilihan salah" + RESET)
