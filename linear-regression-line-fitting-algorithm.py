# =====================================================
# LİNEER REGRESYON - En İyi Doğruyu Bulma
# Amaç: Verilen noktalara en iyi uyan y = mx + b
# doğrusunun m (eğim) ve b (kesişim) değerlerini bulmak
# =====================================================


# -----------------------------------------------------
# GÖREV 1: y = mx + b formülünü hesaplayan fonksiyon
# Parametreler:
#   m → doğrunun eğimi
#   b → y eksenini kestiği nokta
#   x → tahmin yapmak istediğimiz x değeri
# Döndürür: o x'e karşılık gelen y değeri
# -----------------------------------------------------
def get_y(m, b, x):
  y = m * x + b
  return y

print(get_y(1, 0, 7) == 7)    # Beklenen: True → y = 1*7 + 0 = 7
print(get_y(5, 10, 3) == 25)  # Beklenen: True → y = 5*3 + 10 = 25


# -----------------------------------------------------
# GÖREV 2-3: Tek bir nokta için hata hesaplayan fonksiyon
# Hata = tahmin edilen y ile gerçek y arasındaki fark
# Mutlak değer alınır çünkü yön değil, mesafe önemli
# Parametreler:
#   m, b → doğrunun denklemi
#   point → (x, y) formatında gerçek veri noktası
# Döndürür: noktanın doğruya olan uzaklığı
# -----------------------------------------------------
def calculate_error(m, b, point):
  x_point = point[0]   # noktanın x koordinatı
  y_point = point[1]   # noktanın gerçek y değeri

  y_predicted = get_y(m, b, x_point)    # doğrunun tahmin ettiği y
  difference = y_predicted - y_point    # tahmin - gerçek

  return abs(difference)   # negatif çıkabilir, mutlak değer alıyoruz


# GÖREV 4: Hata hesaplamasını test et
print(calculate_error(1, 0, (3, 3)))   # Beklenen: 0 → (3,3) y=x üzerinde
print(calculate_error(1, 0, (3, 4)))   # Beklenen: 1 → (3,4) y=x'e 1 birim uzak
print(calculate_error(1, -1, (3, 3)))  # Beklenen: 1 → (3,3) y=x-1'e 1 birim uzak
print(calculate_error(-1, 1, (3, 3)))  # Beklenen: 5 → (3,3) y=-x+1'e 5 birim uzak


# -----------------------------------------------------
# GÖREV 5: Tüm veri seti için toplam hatayı hesapla
# Her noktanın hatasını ayrı ayrı hesaplayıp toplar
# Toplam hata ne kadar düşükse, doğru o kadar iyi uyuyor
# Parametreler:
#   m, b → doğrunun denklemi
#   points → (x, y) çiftlerinden oluşan veri seti listesi
# Döndürür: tüm noktaların toplam hatası
# -----------------------------------------------------
def calculate_all_error(m, b, points):
  total_error = 0
  for point in points:                           # BUG DÜZELTMESİ: eskiden "datapoints" yazıyordu
    point_error = calculate_error(m, b, point)  # her nokta için ayrı hata
    total_error += point_error                  # hataları topla
  return total_error


# GÖREV 6: Toplam hata hesaplamasını test et
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]

print(calculate_all_error(1, 0, datapoints))   # Beklenen: 0  → tüm noktalar y=x üzerinde
print(calculate_all_error(1, 1, datapoints))   # Beklenen: 4  → her nokta y=x+1'e 1 birim uzak
print(calculate_all_error(1, -1, datapoints))  # Beklenen: 4  → her nokta y=x-1'e 1 birim uzak
print(calculate_all_error(-1, 1, datapoints))  # Beklenen: 18 → hatalar: 1+5+9+3 = 18


# -----------------------------------------------------
# GÖREV 8-9: Denenecek m ve b değerlerinin listesi
# m: -10.0 ile +10.0 arası, 0.1 adımlarla → 201 değer
# b: -20.0 ile +20.0 arası, 0.1 adımlarla → 401 değer
# Toplam: 201 × 401 = 80.601 kombinasyon denenecek
# -----------------------------------------------------
possible_ms = [m/10 for m in range(-100, 101)]
possible_bs = [b/10 for b in range(-200, 201)]


# -----------------------------------------------------
# GÖREV 10: Brute-force (kaba kuvvet) ile en iyi doğruyu bul
# Mantık: Her m ve b kombinasyonunu dene,
#         en düşük hatayı veren kombinasyonu kaydet
# -----------------------------------------------------
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

smallest_error = float("inf")  # Başlangıçta sonsuz büyük (her hata bundan küçük olacak)
best_m = 0
best_b = 0

for m in possible_ms:
  for b in possible_bs:
    error = calculate_all_error(m, b, datapoints)
    if error < smallest_error:   # daha iyi bir doğru bulduk mu?
      best_m = m
      best_b = b
      smallest_error = error     # rekoru güncelle

# Beklenen çıktı: 0.4  1.6  5.0
# Yani en iyi doğru: y = 0.4x + 1.6, toplam hata = 5.0
print(best_m, best_b, smallest_error)


# -----------------------------------------------------
# GÖREV 11-12: Bulunan en iyi doğruyla tahmin yap
# y = 0.4x + 1.6 doğrusunda x=6 için y değeri nedir?
# -----------------------------------------------------
print(get_y(0.4, 1.6, 6))  # Beklenen: 4.0 → y = 0.4*6 + 1.6 = 4.0


# -----------------------------------------------------
# GÖREV 13: (Boş bırakıldı - tamamlanacak)
# -----------------------------------------------------
