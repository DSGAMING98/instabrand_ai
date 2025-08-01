import random

TONE_STYLES = {
    "professional": [
        "Empowering brands with creative storytelling.",
        "Helping businesses grow through strategic design.",
        "Turning ideas into scalable brands."
    ],
    "funny": [
        "I make memes and money. Sometimes at the same time.",
        "Full-time icon, part-time napper.",
        "CEO of not replying to emails on time."
    ],
    "aesthetic": [
        "Dreaming in pastel and building in bold.",
        "Soft vibe. Sharp mind.",
        "Creating things that feel like poetry and punch."
    ]
}

def generate_bio(name, niche, tone="professional"):
    try:
        intros = [
            f"I'm {name}, a {niche} specialist.",
            f"Hey! I’m {name} and I live for {niche}.",
            f"{name} here – obsessed with {niche}!"
        ]
        vibe_lines = TONE_STYLES.get(tone, TONE_STYLES["professional"])
        intro = random.choice(intros)
        vibe = random.choice(vibe_lines)
        return f"{intro} {vibe}"
    except Exception as e:
        return f"Oops, error generating bio: {e}"
