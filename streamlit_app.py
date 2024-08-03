import streamlit as st
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Fungsi untuk menghitung waktu yang telah berlalu
def calculate_time_elapsed(birth_date):
    now = datetime.now()
    difference = relativedelta(now, birth_date)

    years = difference.years
    months = difference.months
    days = difference.days
    hours = difference.hours
    minutes = difference.minutes
    seconds = difference.seconds

    return years, months, days, hours, minutes, seconds

# Aplikasi Streamlit
def main():
    st.title("Kalkulator Waktu")

    # Input tanggal lahir
    birth_date_input = st.date_input("Masukkan tanggal lahir Anda", value=datetime(2000, 1, 1))
    
    # Hitung total waktu yang telah terlewat
    if st.button("Hitung"):
        birth_date = datetime.combine(birth_date_input, datetime.min.time())
        years, months, days, hours, minutes, seconds = calculate_time_elapsed(birth_date)

        # Tampilkan hasil
        st.header("Hasil Perhitungan")
        st.write(f"Total waktu yang telah terlewat sejak tanggal lahir Anda:")
        st.write(f"- **{years}** tahun")
        st.write(f"- **{months}** bulan")
        st.write(f"- **{days}** hari")
        st.write(f"- **{hours}** jam")
        st.write(f"- **{minutes}** menit")
        st.write(f"- **{seconds}** detik")
        
        st.header("Sisa usia anda")
        st.write(f"- **{random.randint(3,40)}** Tahun")
        st.write("Selamat menjalani sisa hidup :)")
        st.write("")
        st.write("")
        st.write("ini cuma candaan aja jangan di bawa hati gitu ahh")
        st.write("-- ARUZAN ")

if __name__ == "__main__":
    main()
