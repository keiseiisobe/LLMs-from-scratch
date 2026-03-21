# Static Parameters vs. Dynamic Activations

This document explains the fundamental difference between the **Static Weights** (Parameters) and the **Dynamic Weights** (Activations) in a Transformer model.

---

## 1. Static Parameters (The "Knowledge")
The matrices $W_Q, W_K, W_V$ and the weights of the Feed-Forward Network (FFN) are the **Static Parameters** of the model.

*   **When they change:** Only during the **Training Phase** via backpropagation.
*   **During Inference:** They are fixed. They stay exactly the same whether you ask the model about "cats" or "quantum physics."
*   **Analogy (The Recipe):** They are like the **printed recipe** in a cookbook. It doesn't change based on who is cooking or when.

---

## 2. Dynamic Weights/Activations (The "Process")
The Query ($Q$), Key ($K$), Value ($V$) vectors and the final **Attention Weights** are **Dynamic Activations**.

*   **How they are created:** They are the result of multiplying the **Static Weights** by the **Dynamic Input** ($x$).
*   **When they change:** Every time you provide a new input sequence.
*   **During Inference:** They exist only in your computer's RAM while the model is "thinking." Once the answer is generated, they are typically discarded.
*   **Analogy (The Cooking):** They are like the **actual measurements** of ingredients you use for a specific meal. They change based on how many people you are feeding.

---

## 3. Why This Distinction Matters

### A. Generalization
Because the $W_Q, W_K, W_V$ matrices are static, the model can apply the **same logic** to many different sentences. 
*   **The Logic:** "If I see a Subject (Query), look for its Verb (Key)."
*   **The Result:** This logic works whether the subject is "The robot" or "The fox."

### B. Memory (VRAM)
*   **Parameters:** Take up a **fixed amount** of space on your GPU (e.g., a 7B parameter model takes ~14GB of VRAM).
*   **Activations:** Take up a **variable amount** of space. The longer your input sequence (context), the more VRAM you need to store the dynamic attention weights.

---

## 💡 Summary Comparison Table

| Feature | **Static Weights ($W_Q, W_K, W_V$)** | **Dynamic Weights (Attention Scores)** |
| :--- | :--- | :--- |
| **Common Name** | **Parameters** | **Activations** |
| **Change Over Time** | Only during **Training**. | Every single **Forward Pass**. |
| **Storage** | Saved on your **Hard Drive**. | Exists in **RAM/VRAM** temporarily. |
| **Input Dependency** | Independent of the specific input. | Completely dependent on the input. |
| **Goal** | Learning **General Rules** of language. | Applying rules to a **Specific Context**. |

---

**Key Insight:** The power of the Transformer comes from using **static knowledge** (the weights) to create **dynamic attention** (the focus), allowing the model to be flexible and context-aware.
