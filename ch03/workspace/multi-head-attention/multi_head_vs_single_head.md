# Multi-Head vs. Single-Head Attention

This document explains why modern Transformers (like GPT) use **Multi-Head Attention (MHA)** instead of a single attention mechanism.

---

## 1. The Problem: The "One Lens" Limitation
In **Single-Head Attention**, the model has only one set of $W_Q, W_K, W_V$ matrices. This means for any given word, the model can only "look" for one type of relationship at a time.

*   **Example:** In the sentence *"The robot painted a picture,"* the word **"robot"** has multiple roles:
    1.  **Grammar:** It is preceded by the article "The".
    2.  **Action:** It is the subject of the verb "painted".
    3.  **Logic:** It is an entity that can perform art.
*   A single head might struggle to focus on all these aspects simultaneously because the Softmax function forces it to "choose" the most statistically significant connection.

---

## 2. The Solution: Representation Subspaces
**Multi-Head Attention** solves this by running the attention mechanism multiple times in parallel. We split the embedding dimension into several "heads" (e.g., GPT-2 has 12 heads).

*   **Parallel Perspectives:** Each head learns a different set of weights. This allows the model to jointly attend to information from different **representation subspaces**.
*   **Specialization:** Over time, different heads specialize in different tasks:
    *   **Head 1:** Focuses on immediate neighbors (syntax/grammar).
    *   **Head 2:** Focuses on the subject-verb relationship (logic).
    *   **Head 3:** Focuses on long-distance references (context).

---

## 3. Analogy: The Team of Experts

| Architecture | Strategy | Analogy |
| :--- | :--- | :--- |
| **Single-Head** | A single person trying to analyze a book for plot, grammar, and history all at once. | The "Generalist" who might miss details. |
| **Multi-Head** | A team of 12 experts. Each expert is assigned one specific task (one for grammar, one for plot, etc.). | The "Specialist Team" that sees everything. |

---

## 4. How it Works (The Flow)
1.  **Split:** The input vector is projected into $N$ different Query, Key, and Value vectors.
2.  **Calculate:** Each head calculates its own **Context Vector** independently.
3.  **Concatenate:** All the context vectors are "glued" together.
4.  **Project:** A final linear layer (`out_proj`) blends these different perspectives back into a single, rich representation.

---

## 💡 Summary Table

| Feature | Single-Head Attention | Multi-Head Attention |
| :--- | :--- | :--- |
| **Views** | One single view. | Multiple parallel views. |
| **Complexity** | Limited to one relationship type. | Captures syntax, semantics, and distance. |
| **Performance** | Sufficient for small tasks. | Essential for complex language understanding. |

**The Insight:** Multi-Head Attention is the "multi-tasking" engine of the Transformer. It allows the model to build a three-dimensional, nuanced understanding of a sentence rather than a flat, one-dimensional one.
