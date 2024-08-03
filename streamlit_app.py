import streamlit as st
import pandas as pd

# Membuat data dalam bentuk dictionary
data = {
    'Kata': [
        'きょうし', 'がくせい', 'かいしゃいん', 'しゃいん', 'ぎんこういん', 
        'いしゃ', 'けんきゅうしゃ', 'だいがく', 'びょういん', 'だれ / どなた', 
        'さい', 'なんさい / おいくつ', 'はい', 'いいえ', 'はじめまして', 
        'からきました', 'どうぞよろしくおねがいします', 'イギリス', 'インド', 
        'ブラジル', 'にほん', 'タイ', 'ドイツ', 'ちゅごく'
    ],
    'Arti': [
        'Guru atau dosen', 'Mahasiswa', 'Karyawan', 'Karyawan beserta perusahaannya', 'Pegawai bank',
        'Dokter', 'Peneliti', 'Universitas', 'Rumah sakit', 'Siapa / sopannya',
        'Tahun', 'Umur berapa', 'Ya', 'Tidak, bukan', 'Perkenalkan',
        'Berasal dari', 'Salam kenal', 'Inggris', 'India',
        'Brasil', 'Jepang', 'Thailand', 'Jerman', 'Cina'
    ],
    'Romaji': [
        'kyoushi', 'gakusei', 'kaishain', 'shain', 'ginkouin',
        'isha', 'kenkyuusha', 'daigaku', 'byouin', 'dare / donata',
        'sai', 'nansai / oikutsu', 'hai', 'iie', 'hajimemashite',
        'kara kimashita', 'douzo yoroshiku onegaishimasu', 'Igirisu', 'Indo',
        'Burajiru', 'Nihon', 'Tai', 'Doitsu', 'Chuugoku'
    ]
}

# Membuat DataFrame dari dictionary
df = pd.DataFrame(data)

# Opsi untuk menampilkan Romaji atau tidak
show_romaji = st.checkbox('Tampilkan Romaji', value=True)

# Menampilkan tabel dengan atau tanpa kolom Romaji
if show_romaji:
    st.table(df)
else:
    st.table(df.drop(columns=['Romaji']))
