# 📱 InstaBrand.AI — Personal Branding Toolkit

**InstaBrand.AI** is a powerful, AI-driven Streamlit web app that helps creators, influencers, and entrepreneurs build their personal brand in seconds. Generate bios, captions, color palettes, and hashtags — all in one aesthetic dashboard.

---

## 🚀 Features

| 🔧 Tool                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| ✍️ **Bio Generator**        | Create professional, funny, or aesthetic bios based on name and niche       |
| 📝 **Caption Generator**    | Get scroll-stopping Instagram captions based on mood and topic              |
| 🎨 **Palette Extractor**    | Upload any image to extract a custom brand color palette                    |
| 📲 **Hashtag Suggester**    | Auto-suggest viral hashtags tailored to your niche                          |
| 📥 **Download Ready**       | Export bios, captions, hashtags, and palettes with one click                |

---

## 📂 Project Structure

```bash
instabrand_ai/
├── instabrand.py               # Main Streamlit app
├── modules/                    # Functional feature modules
│   ├── __init__.py
│   ├── bio_generator.py
│   ├── caption_generator.py
│   ├── palette_generator.py
│   └── hashtag_generator.py
├── assets/                     # Brand visuals & assets (optional)
├── data/                       # Exported/downloadable data (optional)
├── .streamlit/config.toml      # UI theme customization
├── requirements.txt            # Dependencies
└── README.md                   # You're reading it 😎
