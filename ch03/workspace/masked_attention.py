import torch.nn as nn
import torch

class MaskedAttention(nn.Module):
    def __init__(self, d_in, d_out, dropout):
        super().__init__()
        self.W_query = nn.Parameter(torch.rand(d_in, d_out))
        self.W_key = nn.Parameter(torch.rand(d_in, d_out))
        self.W_value = nn.Parameter(torch.rand(d_in, d_out))
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, input):
        query = input @ self.W_query
        key = input @ self.W_key
        value = input @ self.W_value
        attention_score = query @ key.transpose(1, 2)
        context_length = attention_score.shape[-1]
        mask = torch.triu(torch.ones(context_length, context_length), diagonal=1)
        print(f"mask: {mask}")
        masked = attention_score.masked_fill_(mask.bool(), -torch.inf)
        print(f"masked: {masked}")
        attention_weight = torch.softmax(masked, dim=-1)
        attention_weight = self.dropout(attention_weight)
        print(f"dropout: {attention_weight}")
        context_vector = attention_weight @ value
        return context_vector

torch.manual_seed(123)
input = torch.tensor([[0.1, 0.2, 0.3],[0.4, 0.5, 0.6],[0.7, 0.8, 0.9]])
batch = torch.stack((input, input), dim=0)
sha = MaskedAttention(3, 3, 0.0)
print(sha(batch))
    
