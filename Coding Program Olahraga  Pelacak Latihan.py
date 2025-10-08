## Coding Program Olahraga: Pelacak Latihan

def buat_rutinitas_latihan():
    """Mendefinisikan rutinitas latihan dasar."""
    rutinitas = {
        "Senin": ["Squat (3 set x 12 repetisi)", "Push-up (3 set x 10 repetisi)", "Lari (30 menit)"],
        "Selasa": ["Istirahat", "Istirahat", "Istirahat"],
        "Rabu": ["Deadlift (3 set x 8 repetisi)", "Overhead Press (3 set x 10 repetisi)", "Plank (3 set x 60 detik)"],
        "Kamis": ["Yoga (45 menit)", "Stretching (15 menit)", "Istirahat"],
        "Jumat": ["Bench Press (3 set x 10 repetisi)", "Rowing (3 set x 12 repetisi)", "Mountain Climber (3 set x 20 repetisi)"],
        "Sabtu": ["Lari Jarak Jauh (60 menit)", "Cool-down", "Istirahat"],
        "Minggu": ["Istirahat", "Istirahat", "Istirahat"]
    }
    return rutinitas

def tampilkan_dan_lacak_latihan():
    """Menampilkan latihan hari ini dan mencatat penyelesaiannya."""
    
    import datetime
    
    # Dapatkan nama hari ini dalam Bahasa Inggris (misalnya 'Monday')
    nama_hari = datetime.datetime.now().strftime("%A") 
    
    # Peta dari Inggris ke Indonesia (agar mudah dibaca)
    peta_hari = {
        "Monday": "Senin", "Tuesday": "Selasa", "Wednesday": "Rabu", 
        "Thursday": "Kamis", "Friday": "Jumat", "Saturday": "Sabtu", 
        "Sunday": "Minggu"
    }
    
    hari_ini = peta_hari.get(nama_hari, "Hari tidak ditemukan")
    
    # Dapatkan rutinitas dari fungsi
    rutinitas = buat_rutinitas_latihan()
    latihan_hari_ini = rutinitas.get(hari_ini, ["Tidak ada jadwal latihan."])
    
    print(f"--- Jadwal Latihan Hari Ini: **{hari_ini}** ---")
    
    if latihan_hari_ini == ["Istirahat", "Istirahat", "Istirahat"] or latihan_hari_ini == ["Tidak ada jadwal latihan."]:
        print("Hari ini adalah Hari Istirahat atau Tidak ada jadwal.")
        return

    hasil_lacak = {}
    
    for i, latihan in enumerate(latihan_hari_ini):
        # Lewati jika latihan adalah "Istirahat"
        if "Istirahat" in latihan:
            continue
            
        print(f"\nLatihan {i+1}: **{latihan}**")
        
        # Meminta input dari pengguna untuk mencatat penyelesaian
        status = input("Sudah selesai? (ya/belum): ").lower()
        
        if status == 'ya':
            hasil_lacak[latihan] = "Selesai ✅"
        else:
            hasil_lacak[latihan] = "Tertunda ❌"

    # Tampilkan ringkasan
    print("\n==================================")
    print(f"**Ringkasan Latihan {hari_ini}**")
    print("==================================")
    
    for latihan, status in hasil_lacak.items():
        print(f"- {latihan}: {status}")
    
    print("Selamat! Tetap konsisten!")

# Jalankan program
if __name__ == "__main__":
    tampilkan_dan_lacak_latihan()