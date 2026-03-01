# RNN Encoder-Decoder: The Pre-LLM Translation Flow

This document explains the architecture used for language translation before the invention of Transformers (and GPT). It highlights how Recurrent Neural Networks (RNNs) work and why they struggled with long sequences.

## 1. The Architecture: A "Relay Race"

In a traditional RNN-based translation model (often called **Seq2Seq**), there are two main components: the **Encoder** and the **Decoder**.

### The Encoder (The "Reader")
The Encoder processes the input sequence (e.g., a French sentence) one token at a time.
*   **Step 1:** It takes the first word $x_1$ and an initial hidden state $h_0$ (usually zeros). It produces a new hidden state $h_1$.
*   **Step 2:** It takes the second word $x_2$ and the *previous* hidden state $h_1$. It produces $h_2$.
*   **Context Vector:** This continues until the last word. The **final hidden state** (the "Context Vector") is intended to be a complete numerical summary of the entire sentence.

### The Decoder (The "Writer")
The Decoder takes the Context Vector and starts generating the target sequence (e.g., an English sentence).
*   **Initial State:** Its first hidden state is set to the Encoder's final Context Vector.
*   **Generation:** At each step, it takes its own previous output (the word it just generated) and its current hidden state to predict the next word.

---

## 2. The "Information Bottleneck" Limitation

The biggest problem with this architecture is the **Information Bottleneck**.

1.  **Fixed-Size Memory:** No matter how long the input sentence is (5 words or 50 words), the Encoder is forced to "squeeze" the entire meaning into a single, fixed-size Context Vector.
2.  **Vanishing Context:** In long sentences, the information from the *beginning* of the sentence often gets "washed out" or forgotten by the time the Encoder reaches the end.
3.  **No "Look Back":** Once the Decoder starts writing, it **cannot** see the original input words. it only has access to that single, final summary vector. If that summary is missing a detail, the translation will be wrong.

---

## 3. Comparison: RNN vs. Transformer (GPT)

| Feature | RNN Encoder-Decoder | Transformer (GPT) |
| :--- | :--- | :--- |
| **Processing** | Sequential (one by one) | Parallel (all at once) |
| **Memory** | Fading (recursively updated) | Perfect (non-fading attention) |
| **Bottleneck** | Yes (single Context Vector) | No (direct access to all tokens) |
| **Dependency** | Struggles with long-distance | Handles long-distance easily |

## 4. Visualizing the Flow
You can run the `visualize_rnn_flow.py` script in this directory to see a diagram of this "Relay Race" architecture.
