import streamlit as st
import pandas as pd

# Membuat data dalam bentuk dictionary
data = {
    'Kata': [
        'わたし', 'あなた', 'あの　ひと／あの　かた', 'ーさん', '～ちゃん', '～じん', 
        'せんせい', 'きょうし', 'がくせい', 'かいしゃいん', 'しゃいん', 'ぎんこういん', 
        'いしゃ', 'けんきゅうしゃ', 'だいがく', 'びょういん', 'だれ（どなた）', '～さい', 
        'なんさい（おいくつ）', 'はい', 'いいえ', 'はじめまして', 'からきました', 
        'どうぞよろしくおねがいします', 'しつれいですが', 'おなまえは?', 
        'こちらは　〜さんです', 'イギリス', 'インド', 'ブラジル', 'にほん', 
        'タイ', 'ドイツ', 'ちゅごく', 'ドイツ', 'にほん', 'ブラジル'
    ],
    'Kanji': [
        '私', '', 'あの人／あの方', '', '', '～ひと', 
        '先生', '教師', '学生', '会社員', '社員', '銀行員', 
        '医者', '研究者', '大学', '病院', '', '～歳', 
        '何歳', '', '', '', '', '', 'お名前は?', 
        '', '', '', '', '', '', '', '', '', ''
    ],
    'Arti': [
        'Saya', 'Anda', 'Orang itu/beliau', 'Saudara-bapak-ibu', 'Akhiran untuk panggilan anak-anak', 
        'Orang', 'Guru, dosen, pengajar', 'Guru, dosen', 'Pelajar', 'Karyawan perusahaan', 
        'Karyawan perusahaan (dipakai bersama nama perusahaan)', 'Karyawan bank', 'Dokter', 
        'Peneliti', 'Universitas', 'Rumah sakit', 'Siapa', '--tahun', 'Berapa umurnya', 
        'Ya', 'Tidak, bukan', 'Perkenalkan', 'Datang dari, Berasal dari', 'Salam kenal', 
        'Permisi, maaf', 'Siapa namanya?', 'Ini bapak〜/ Ini ibu, sdr.', 'Inggris', 'India', 
        'Brasil', 'Jepang', 'Thailand', 'Jerman', 'Cina', 'Jerman', 'Jepang', 'Brasil'
    ],
    'Romaji': [
        'watashi', 'anata', 'ano hito/ano kata', '-san', '-chan', '-jin', 
        'sensei', 'kyoushi', 'gakusei', 'kaishain', 'shain', 'ginkouin', 
        'isha', 'kenkyuusha', 'daigaku', 'byouin', 'dare (donata)', '-sai', 
        'nansai (oikutsu)', 'hai', 'iie', 'hajimemashite', 'kara kimashita', 
        'douzo yoroshiku onegaishimasu', 'shitsureidesuga', 'onamae wa?', 
        'kochira wa 〜san desu', 'Igirisu', 'Indo', 'Burajiru', 'Nihon', 
        'Tai', 'Doitsu', 'Chuugoku', 'Doitsu', 'Nihon', 'Burajiru'
    ],
    'Keterangan': [
        '', '', '', '', '', '', '', '', '', '', 
        '', '', '', '', '', '', '', '', '', '', 
        '', 'ucapan salam pada waktu pertama kali berkenalan', '', 
        'ucapan terakhir untuk perkenalan diri', 
        'digunakan ketika bertanya tentang hal yang pribadi seperti nama, alamat, dan sebagainya', 
        '', '', '', '', '', '', '', '', '', '', ''
    ]
}

# Membuat DataFrame dari dictionary
df = pd.DataFrame(data)

st.title("Kosakata - Bab 1")

# Opsi untuk menampilkan Romaji atau tidak
show_romaji = st.checkbox('Tampilkan Romaji', value=True)
show_keterangan = st.checkbox('Tampilkan Keterangan', value=True)

# Menampilkan tabel dengan atau tanpa kolom Romaji dan Keterangan
if show_romaji and show_keterangan:
    st.table(df)
elif show_romaji:
    st.table(df.drop(columns=['Keterangan']))
elif show_keterangan:
    st.table(df.drop(columns=['Romaji']))
else:
    st.table(df.drop(columns=['Romaji', 'Keterangan']))

st.write("by aru")
