# modules/caption_generator.py

import random

CAPTION_MOODS = {
    "funny": [
        "Serving looks and leftovers 😌",
        "Too glam to give a damn 💅",
        "Mentally I'm here 👉🍕"
    ],
    "aesthetic": [
        "Golden hour hits different 🌞✨",
        "Soft days & strong coffee ☕🌸",
        "Letting the light do the talking 📸"
    ],
    "motivational": [
        "You are the brand. Build it. 💼",
        "Create. Post. Repeat. 🚀",
        "Dream big, post bigger 🧠🔥"
    ]
}

def generate_caption(niche, mood, keyword=None):
    try:
        base = random.choice(CAPTION_MOODS.get(mood, CAPTION_MOODS["motivational"]))
        if keyword:
            return f"{base} #{keyword} #{niche.replace(' ', '')}"
        return f"{base} #{niche.replace(' ', '')}"
    except Exception as e:
        return f"Oops, error generating caption: {e}"
