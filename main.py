from fastapi import FastAPI
import pandas as pd

# Instance untuk FastAPI nya
app = FastAPI()

# <Method>  /url
# GET       /todos
# Mendefinisikan (endpoint) - GET /todos via @app.sesuatu (decorator)
@app.get("/todos")
def ambil_data_todos():
    # Gw harus mengembalikan data (JSON / Dictionary)
    return {
        # Ini adalah data JSON-nya
        "message": "Halo Dunia"
    }

# GET       /perkalian/angka_1/angka_2
# GET       /perkalian/10/20
# Mendefinisikan (endpoint) - GET /perkalian/angka_1/angka_2 via @app.get
@app.get("/perkalian/{angka_1}/{angka_2}")
def perkalian_dua(angka_1: int, angka_2: int):
    # Pengen melakukan suatu logic (apapun itu)
    hasil_perkalian = angka_1 * angka_2

    # Bikin hasil kembaliannya
    return {
        # Ingat di sini bentuknya adalah dictionary atau list
        "angka_pertama": angka_1,
        "angka_kedua": angka_2,
        "hasil_dari_perkalian": hasil_perkalian,
    }

# Endpoint baru
# GET /pandas
@app.get("/pandas")
def baca_dari_file_csv():
    # Baca file csv dari pandas
    df = pd.read_csv("coba1.csv")  # DataFrame

    # Kembalian dari suatu endpoint harus dalam bentuk Dictionary
    # DataFrame harus bisa diubah jadi dictionary, caranya...?
    # Fungsi bawaan dari DataFrame untuk mengubah dataframe jadi dict
    # to_dict
    converted_dict = df.to_dict(orient="records")

    return converted_dict