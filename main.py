meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "SHEESH": "Sedikit ketidaksetujuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "AGGRO": "Untuk menjadi agresif/marah"
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Mohon maaf, kami tidak bisa menemukan kata ini di kamus")
