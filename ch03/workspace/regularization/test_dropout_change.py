import torch
import torch.nn as nn

# Set seed for reproducibility in each run, but not between calls
torch.manual_seed(42)

dropout = nn.Dropout(p=0.5)
example = torch.ones(5, 5)

print("--- First Call (Training Mode) ---")
print(dropout(example))

print("\n--- Second Call (Training Mode) ---")
print(dropout(example))

dropout.eval()
print("\n--- Third Call (Evaluation Mode) ---")
print(dropout(example))
