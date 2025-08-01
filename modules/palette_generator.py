# modules/palette_generator.py

from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import io

def extract_palette(image: Image.Image, num_colors=5):
    try:
        image = image.resize((200, 200))  # Speed up processing
        img_data = np.array(image)
        img_data = img_data.reshape((-1, 3))

        kmeans = KMeans(n_clusters=num_colors, random_state=0)
        kmeans.fit(img_data)

        colors = kmeans.cluster_centers_.astype(int)
        hex_colors = ['#%02x%02x%02x' % tuple(color) for color in colors]

        # Create palette image
        fig, ax = plt.subplots(figsize=(6, 1))
        for i, color in enumerate(colors):
            ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=np.array(color)/255))
        ax.set_xlim(0, num_colors)
        ax.set_ylim(0, 1)
        ax.axis("off")

        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches='tight')
        plt.close(fig)
        buf.seek(0)

        return hex_colors, buf
    except Exception as e:
        return [f"Error: {e}"], None
