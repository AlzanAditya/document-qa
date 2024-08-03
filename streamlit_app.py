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
    ]
}

# Membuat DataFrame dari dictionary
df = pd.DataFrame(data)

# Menampilkan tabel menggunakan Streamlit
st.table(df)
