import torch
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import json

def visualize_3d_embeddings():
    # 1. Define a simple vocabulary and their "semantic" categories
    vocab = {
        "apple": 0, "banana": 0, "cherry": 0,  # Fruits
        "dog": 1, "cat": 1, "wolf": 1,         # Animals
        "car": 2, "bus": 2, "train": 2,       # Vehicles
        "blue": 3, "red": 3, "green": 3        # Colors
    }
    
    words = list(vocab.keys())
    categories = list(vocab.values())
    category_names = ["Fruits", "Animals", "Vehicles", "Colors"]
    
    # 2. Define "Centroids" for each category to ensure clustering
    # Each category is placed in a different quadrant of the 3D space
    centroids = torch.tensor([
        [ 2.0,  2.0,  2.0],  # Fruits (Top-Right-Front)
        [-2.0, -2.0,  2.0],  # Animals (Bottom-Left-Front)
        [ 2.0, -2.0, -2.0],  # Vehicles (Top-Left-Back)
        [-2.0,  2.0, -2.0]   # Colors (Bottom-Right-Back)
    ])
    
    # 3. Create embeddings by adding small random noise to the centroids
    torch.manual_seed(42)
    embeddings = torch.zeros((len(vocab), 3))
    for i, cat_idx in enumerate(categories):
        # Add a small amount of Gaussian noise (std=0.5) to the category centroid
        noise = torch.randn(3) * 0.5
        embeddings[i] = centroids[cat_idx] + noise

    # 4. Export data for interactive JS visualization
    plot_data = []
    for i, word in enumerate(words):
        plot_data.append({
            "word": word,
            "x": float(embeddings[i][0]),
            "y": float(embeddings[i][1]),
            "z": float(embeddings[i][2]),
            "category": category_names[categories[i]]
        })
    
    with open('embeddings_data.json', 'w') as f:
        json.dump(plot_data, f, indent=4)
    print("Clustered data exported to embeddings_data.json")

    # 5. Create the static 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    colors = plt.cm.rainbow(np.linspace(0, 1, 4))
    
    for i, word in enumerate(words):
        x, y, z = embeddings[i].numpy()
        category = categories[i]
        ax.scatter(x, y, z, color=colors[category], s=100)
        ax.text(x, y, z, f" {word}", size=12, zorder=1, color='black')

    ax.set_title('Clustered 3D Word Embeddings')
    ax.set_xlabel('Dimension 1')
    ax.set_ylabel('Dimension 2')
    ax.set_zlabel('Dimension 3')
    
    plt.savefig('word_embeddings_3d.png', dpi=300)
    print("Static clustered visualization saved to word_embeddings_3d.png")

if __name__ == "__main__":
    visualize_3d_embeddings()
