# Word Embedding Visualization in 3D

This workspace demonstrates how words are converted into multi-dimensional vectors (embeddings).

## Concept
In Chapter 2, we learned that LLMs cannot process raw text. Instead:
1.  **Tokenization** converts text into token IDs.
2.  **Embedding** converts those IDs into vectors.

While real LLMs use hundreds or thousands of dimensions (e.g., 768 in GPT-2), this visualization shows a simplified **3D representation** where each word is a point in a 3-dimensional coordinate system.

## Contents
*   `visualize_embeddings.py`: A Python script using `PyTorch` to generate 3D embeddings and export them as `embeddings_data.json`.
*   `index.html`: A rotatable 3D visualization using **Plotly.js**.
*   `word_embeddings_3d.png`: A static preview of the embeddings.

## How to View the Rotatable 3D Visualization
To avoid browser security restrictions (CORS) when loading local JSON files, it is best to serve this folder with a simple web server:

1.  Open your terminal in this directory:
    ```bash
    cd ch02/workspace/word-embedding-visualization
    ```
2.  Start a local Python web server:
    ```bash
    python3 -m http.server 8080
    ```
3.  Open your browser and navigate to:
    [http://localhost:8080](http://localhost:8080)

You can now click and drag to **rotate** the 3D space, use the scroll wheel to **zoom**, and hover over points to see the word labels.
