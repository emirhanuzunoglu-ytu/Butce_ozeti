import json
import os

# JSON dosya adı
FILE_NAME = "veri.json"

# Eğer dosya yoksa, varsayılan veri oluştur
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        json.dump({"bakiye": 0, "gelirler": {"Yatırım": 0, "Ev İçin": 0, "Diğer": 0}, 
                   "giderler": {"Fatura": 0, "Ev İçin": 0, "Diğer": 0}}, file)

# JSON dosyasını oku
def load_data():
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# JSON dosyasına kaydet
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def main():
    # Verileri yükle
    data = load_data()
    bakiye = data["bakiye"]
    gelirler = data["gelirler"]
    giderler = data["giderler"]

    while True:
        # Bakiye gösterimi
        print(f"\nBakiye: {bakiye} TL")

        # Menü
        print("1. Gelir Ekleme")
        print("2. Gider Ekleme")
        print("3. Çıkış")

        # Menü seçimi
        choice_menu = input("Seçim yapınız: ")

        if choice_menu == "1":
            print("\n📥 GELİR EKLEME MENÜSÜ")
            category_gelir_list = {"1": "Yatırım", "2": "Ev İçin", "3": "Diğer"}

            for key, value in category_gelir_list.items():
                print(f"{key} - {value}")

            choice_category_gelir = input("Kategori Seçin: ")

            if choice_category_gelir in category_gelir_list:
                miktar = float(input(f"{category_gelir_list[choice_category_gelir]} için gelir miktarı giriniz: "))
                kategori_adi = category_gelir_list[choice_category_gelir]

                gelirler[kategori_adi] += miktar
                bakiye += miktar
                print(f"✅ {kategori_adi} kategorisine {miktar} TL eklendi!")

                # Verileri güncelle ve kaydet
                data["bakiye"] = bakiye
                data["gelirler"] = gelirler
                save_data(data)
            else:
                print("❌ Geçersiz seçim!")

        elif choice_menu == "2":
            print("\n📤 GİDER EKLEME MENÜSÜ")
            category_gider_list = {"1": "Fatura", "2": "Ev İçin", "3": "Diğer"}

            for key, value in category_gider_list.items():
                print(f"{key} - {value}")

            choice_category_gider = input("Kategori Seçin: ")

            if choice_category_gider in category_gider_list:
                miktar = float(input(f"{category_gider_list[choice_category_gider]} için gider miktarı giriniz: "))
                kategori_adi = category_gider_list[choice_category_gider]

                giderler[kategori_adi] += miktar
                bakiye -= miktar
                print(f"✅ {kategori_adi} kategorisine {miktar} TL eklendi!")

                # Verileri güncelle ve kaydet
                data["bakiye"] = bakiye
                data["giderler"] = giderler
                save_data(data)
            else:
                print("❌ Geçersiz seçim!")

        elif choice_menu == "3":
            print("🚪 Çıkış yapılıyor...")
            break

        else:
            print("❌ Geçersiz seçim!")

main()
