
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Endpoint baru
# GET /baca
@app.get("/baca")
def baca_dari_file_csv():
    # Baca file csv dari pandas
    df = pd.read_csv("latian_LC3rev1.csv")  # DataFrame

    # Kembalian dari suatu endpoint harus dalam bentuk Dictionary
    # DataFrame harus bisa diubah jadi dictionary, caranya...?
    # Fungsi bawaan dari DataFrame untuk mengubah dataframe jadi dict
    # to_dict
    converted_dict = df.to_dict(orient="records")

    return converted_dict

# membuat endpoint baru
#GET / hapus data

@app.delete("/hapusnilai/value/{nilai}")
def hapus_duration_by_value(nilai: int):
    #baca file csv dari pandas
    df = pd.read_csv("latian_LC3rev1.csv")

    if nilai not in df["duration_sec"].values:
     return {"nilai": "tidak ditemukan"}

    df = df[df["duration_sec"] != nilai]

    df.to_csv("cobadrop.csv", index=False)          #terserah mau output yang mana

    df_drop = df.to_dict(orient="records")

    return df_drop

    #return {"message": f"Data dengan duration {nilai} berhasil dihapus"}
