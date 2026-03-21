import torch
import torch.nn as nn

class SingleHeadAttention_v1(nn.Module):
    def __init__(self, d_in, d_out):
        super().__init__()
        self.W_query = nn.Parameter(torch.rand(d_in, d_out))
        self.W_key = nn.Parameter(torch.rand(d_in, d_out))
        self.W_value = nn.Parameter(torch.rand(d_in, d_out))
   
    def forward(self, input):
        query = input @ self.W_query
        key = input @ self.W_key
        attention_score = query @ key.T
        attention_weight = torch.softmax(attention_score / key.shape[-1]**0.5, dim=-1)
        value = input @ self.W_value
        context_vector = attention_weight @ value
        return context_vector

torch.manual_seed(123)
input = torch.tensor([[0.1, 0.2, 0.3],[0.4, 0.5, 0.6]])
sha = SingleHeadAttention(3, 3)
print(sha(input))
