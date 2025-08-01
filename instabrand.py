# instabrand.py

import streamlit as st
from modules.bio_generator import generate_bio

# Streamlit page config
st.set_page_config(
    page_title="InstaBrand AI",
    page_icon="✨",
    layout="centered"
)

# App title
st.title("📱 InstaBrand.AI — Bio Generator")

# Subtitle
st.markdown("Create a fire personal brand bio in seconds 🔥")

# User input
name = st.text_input("Your Name", placeholder="e.g. Ariana")
niche = st.text_input("Your Niche", placeholder="e.g. fashion content creation")

# Tone selection
tone = st.selectbox("Pick Your Vibe (Tone)", ["professional", "funny", "aesthetic"])

# Button
if st.button("Generate My Bio", key="bio_button"):
    if name and niche:
        bio = generate_bio(name, niche, tone)
        st.success("Here’s your slay-worthy bio:")
        st.code(bio, language="markdown")
    else:
        st.warning("Please enter both your name and niche!")
# Generate and show bio
if st.button("Generate My Bio"):
    if name and niche:
        bio = generate_bio(name, niche, tone)
        st.success("Here’s your slay-worthy bio:")
        st.code(bio, language="markdown")

        # Download button
        st.download_button(
            label="Download Bio",
            data=bio,
            file_name=f"{name}_bio.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please enter both your name and niche!")
# Divider
st.markdown("---")

# Caption Generator Section
st.title("📝 Insta Caption Generator")
st.markdown("Craft a scroll-stopping caption with your vibe 🧠✨")

# Inputs
caption_niche = st.text_input("Your Niche", key="caption_niche", placeholder="e.g. fitness, makeup, travel")
caption_mood = st.selectbox("Mood/Vibe", ["funny", "aesthetic", "motivational"], key="caption_mood")
caption_keyword = st.text_input("Optional Keyword or Topic", key="caption_keyword", placeholder="e.g. ootd, grind, coffee")

# Button
if st.button("Generate My Caption", key="caption_button"):

    if caption_niche:
        from modules.caption_generator import generate_caption
        caption = generate_caption(caption_niche, caption_mood, caption_keyword)
        st.success("Here’s your caption:")
        st.code(caption, language="markdown")

        # Download caption
        st.download_button(
            label="Download Caption",
            data=caption,
            file_name=f"{caption_niche}_caption.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please enter your niche to generate a caption.")
# Divider
st.markdown("---")

# Color Palette Generator Section
st.title("🎨 Brand Color Palette Extractor")
st.markdown("Upload an image and get a matching color palette for your aesthetic ✨")

uploaded_image = st.file_uploader("Upload Your Inspo Photo (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    from PIL import Image
    from modules.palette_generator import extract_palette

    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("Extracting palette...")

    hex_colors, palette_img = extract_palette(image)

    if palette_img:
        st.image(palette_img, caption="Generated Color Palette", use_column_width=False)
        st.markdown("**Hex Codes:**")
        st.code(", ".join(hex_colors), language="markdown")

        st.download_button(
            label="Download Palette Image",
            data=palette_img,
            file_name="color_palette.png",
            mime="image/png"
        )
    else:
        st.error("Something went wrong generating the palette.")
# Divider
st.markdown("---")

# Hashtag Generator Section
st.title("📲 Hashtag Suggester")
st.markdown("Boost your reach with curated hashtags 🚀")

hashtag_niche = st.selectbox("Select Your Niche", [
    "fashion", "fitness", "travel", "makeup", "photography", "other"
])

if st.button("Suggest Hashtags", key="hashtag_button"):

    from modules.hashtag_generator import suggest_hashtags

    tags = suggest_hashtags(hashtag_niche)
    tag_output = " ".join(tags)

    st.success("Try using these with your post:")
    st.code(tag_output, language="markdown")

    st.download_button(
        label="Download Hashtags",
        data=tag_output,
        file_name=f"{hashtag_niche}_hashtags.txt",
        mime="text/plain"
    )
