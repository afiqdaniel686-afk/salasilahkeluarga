```python
import streamlit as st
import pandas as pd

st.title("Sistem Salasilah Keluarga Melayu-Islam")

data = [
    {
        "ID": 1,
        "Nama Penuh": "Ahmad",
        "Bin/Binti": "Bin Ali",
        "ID Bapa": 2,
        "ID Ibu": 3,
        "Status": "Kandung",
        "Nota": "Datuk",
    },
    {
        "ID": 2,
        "Nama Penuh": "Ali",
        "Bin/Binti": "Bin Abu",
        "ID Bapa": 0,
        "ID Ibu": 0,
        "Status": "Kandung",
        "Nota": "Moyang",
    },
]

df = pd.DataFrame(data)

st.write("Senarai Ahli Keluarga:")
st.dataframe(df)

st.subheader("Tambah Ahli Keluarga Baru")
nama = st.text_input("Nama Penuh")
bin_binti = st.text_input("Bin / Binti")
id_bapa = st.number_input("ID Bapa", min_value=0, step=1)
id_ibu = st.number_input("ID Ibu", min_value=0, step=1)

if st.button("Simpan"):
    st.success(f"Berjaya menambah {nama}!")

```
