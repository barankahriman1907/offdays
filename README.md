# OFFDAYS

Vardiyalı çalışanlar için takvim değil, cevap veren planlayıcı.
Çevrimdışı çalışır, sunucusu yoktur, hiçbir veri toplamaz.

- `www/index.html` — uygulamanın tamamı (tek dosya, bağımlılıksız)
- `assets/` — ikon ve açılış ekranı kaynakları (build sırasında `tools/make_assets.py` üretir)
- `store/` — App Store metinleri ve inceleme notları
- `tools/` — ikon üreten betik

## Geliştirme

```bash
npm install
npx cap add ios
npx cap sync ios
```

Derleme Codemagic üzerinden yapılır (`codemagic.yaml`), Mac gerekmez.

## Yerel önizleme

```bash
python3 -m http.server 8000
# http://localhost:8000/www/
```

LODOS
