import streamlit as st
import pandas as pd

# Membuat data dalam bentuk dictionary
data = {
    'Kata': [
        'わたし', 'あなた', 'あの ひと', 'あの かた', 'ーさん', '～ちゃん', '～じん', 
        'せんせい', 'きょうし', 'がくせい', 'かいしゃいん', 'しゃいん', 'ぎんこういん', 
        'いしゃ', 'けんきゅうしゃ', 'だいがく', 'びょういん', 'だれ（どなた）', '～さい', 
        'なんさい（おいくつ）', 'はい', 'いいえ', 'はじめまして', 'からきました', 
        'どうぞよろしくおねがいします', 'しつれいですが', 'おなまえは?', 
        'こちらは 〜さんです', 'イギリス', 'インド', 'ブラジル', 'にほん', 
        'タイ', 'ドイツ', 'ちゅうごく'
    ],
    'Kanji': [
        '私', '', 'あの人', 'あの方', '', '', '', 
        '先生', '教師', '学生', '会社員', '社員', '銀行員', 
        '医者', '研究者', '大学', '病院', '', '～歳', 
        '何歳', '', '', '', '', '', '', '',
        '', '', '', '', '', '', '', ''
    ],
    'Arti': [
        'Saya', 'Anda', 'Orang itu/beliau', 'Orang itu/beliau', 'Saudara-bapak-ibu', 'Akhiran untuk panggilan anak-anak', 
        'Orang', 'Guru, dosen, pengajar', 'Guru, dosen', 'Pelajar', 'Karyawan perusahaan', 
        'Karyawan perusahaan', 'Karyawan bank', 'Dokter', 
        'Peneliti', 'Universitas', 'Rumah sakit', 'Siapa', '--tahun', 'Berapa umurnya', 
        'Ya', 'Tidak, bukan', 'Perkenalkan', 'Datang dari, Berasal dari', 'Salam kenal', 
        'Permisi, maaf', 'Siapa namanya?', 'Ini bapak〜/ Ini ibu, sdr.', 'Inggris', 'India', 
        'Brasil', 'Jepang', 'Thailand', 'Jerman', 'Cina'
    ],
    'Romaji': [
        'watashi', 'anata', 'ano hito', 'ano kata', '-san', '-chan', '-jin', 
        'sensei', 'kyoushi', 'gakusei', 'kaishain', 'shain', 'ginkouin', 
        'isha', 'kenkyuusha', 'daigaku', 'byouin', 'dare (donata)', '-sai', 
        'nansai (oikutsu)', 'hai', 'iie', 'hajimemashite', 'kara kimashita', 
        'douzo yoroshiku onegaishimasu', 'shitsureidesuga', 'onamae wa?', 
        'kochira wa 〜san desu', 'Igirisu', 'Indo', 'Burajiru', 'Nihon', 
        'Tai', 'Doitsu', 'Chuugoku'
    ],
    'Keterangan': [
    '', '', '', 'lebih sopan dari あの ひと', ' akhiran untuk mengekspresikan kesopanan yang diletakkan di belakang nama orang', 'akhiran yang dipakai untuk anak laki-laki dan anak perempuan sebagai pengganti 〜 さん yang diletakkan di belakang nama anak', 'akhiran yang menyatakan warga negara. contoh: アメリカじん (orang amerika)', 'tidak dipakai jika tidak menyebut pekerjaan sendiri', '', '', '',
    'dipakai bersama nama perusahaan', '', '', '', '', '', '', '', '', '', 
    '', 'ucapan salam pada waktu pertama kali berkenalan', '', 
    'ucapan terakhir untuk perkenalan diri', 
    'digunakan ketika bertanya tentang hal yang pribadi seperti nama, alamat, dan sebagainya', 
    '', '', '', '', '', '', '', '', ''
    ]
}

df = pd.DataFrame(data)


# Opsi untuk menampilkan Romaji atau tidak
show_romaji = st.checkbox('Tampilkan Romaji', value=True)
show_keterangan = st.checkbox('Tampilkan Keterangan', value=True)
show_kanji = st.checkbox('Tampilkan Kanji', value=True)

st.title("Kosakata - Bab 1")

# Menampilkan tabel dengan atau tanpa kolom Romaji
if show_romaji and show_kanji and show_keterangan:
    st.table(df)
elif show_romaji and show_kanji:
    st.table(df.drop(columns=['Keterangan']))
elif show_romaji and show_keterangan:
    st.table(df.drop(columns=['Kanji']))
elif show_kanji and show_keterangan:
    st.table(df.drop(columns=['Romaji']))
elif show_romaji:
    st.table(df.drop(columns=['Kanji', 'Keterangan']))
elif show_kanji:
    st.table(df.drop(columns=['Romaji', 'Keterangan']))
elif show_keterangan:
    st.table(df.drop(columns=['Romaji', 'Kanji']))
else:
    st.table(df.drop(columns=['Romaji', 'Kanji', 'Keterangan']))

st.write("by aru")
