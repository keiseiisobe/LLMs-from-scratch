# Understanding "Encoding" in LLMs: Data Transformation vs. Architecture

When discussing Large Language Models (LLMs) like GPT, the term "encoding" can be used in two different ways, which often leads to confusion. This document clarifies those differences.

## 1. Encoding as a Data Transformation
In a general context, **encoding** refers to the process of converting data from one format into another. In the LLM workflow, this happens in several stages:

*   **Tokenization:** Converting raw text (strings) into discrete integer IDs. For example, using a tokenizer to turn "Hello" into `[15496]`. In libraries like `tiktoken`, this method is explicitly called `.encode()`.
*   **Embedding:** Converting those integer IDs into continuous multi-dimensional vectors (embeddings). This "encodes" the semantic meaning of a token into a vector space that the neural network can process.

In this sense, **every LLM performs encoding**, as they all must transform text into numerical representations.

## 2. Encoder as an Architectural Component
In the specific context of the **Transformer architecture** (introduced in the "Attention Is All You Need" paper), an **Encoder** is a specific structural block with distinct properties:

*   **Bi-directional Attention:** An Encoder block allows every token in a sequence to "attend" to every other token (both before and after it). This is ideal for tasks like classification or translation where you have the full input context available. Models like **BERT** are "Encoder-only."
*   **The "Decoder-Only" Label:** Models like **GPT** and **Llama** are called "decoder-only" because they lack these bi-directional Encoder blocks. Instead, they use **Causal (Masked) Self-Attention**, where a token can only see tokens that appeared before it. This is designed for autoregressive generation (predicting the next token).

## Why is GPT called "Decoder-Only" if it "Encodes" text?
GPT is a **decoder-only** model because of its **structural design**:
1. It uses masked attention (causal).
2. it lacks the separate Encoder-Decoder cross-attention layers found in the original Transformer.

While GPT certainly "encodes" text into vectors (as a data transformation), it does not use the "Encoder" architectural component.

| Concept | Definition | Usage in GPT |
| :--- | :--- | :--- |
| **Token Encoding** | Transformation of text to IDs | Yes (Chapter 2) |
| **Embedding** | Transformation of IDs to vectors | Yes (Chapter 2) |
| **Encoder Block** | Architectural unit with bi-directional attention | **No** (Chapter 4) |
| **Decoder Block** | Architectural unit with causal attention | **Yes** (Chapter 4) |
