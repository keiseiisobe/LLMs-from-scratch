import matplotlib.pyplot as plt

def draw_rnn_flow():
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Settings
    box_w, box_h = 1.5, 0.8
    y_encoder = 2
    y_decoder = 0.5
    
    # --- Encoder ---
    words_in = ["Hello", "how", "are", "you?"]
    for i, word in enumerate(words_in):
        x = i * 2.5
        # Hidden State Box
        rect = plt.Rectangle((x, y_encoder), box_w, box_h, fill=False, color='blue', lw=2)
        ax.add_patch(rect)
        ax.text(x + box_w/2, y_encoder + box_h/2, f"h_{i+1}", ha='center', va='center', fontweight='bold')
        
        # Input Word
        ax.text(x + box_w/2, y_encoder + box_h + 0.3, word, ha='center', va='center', color='darkblue')
        ax.annotate('', xy=(x + box_w/2, y_encoder + box_h), xytext=(x + box_w/2, y_encoder + box_h + 0.2),
                    arrowprops=dict(arrowstyle='->', color='gray'))

        # Recurrent Arrow
        if i > 0:
            ax.annotate('', xy=(x, y_encoder + box_h/2), xytext=(x - 1, y_encoder + box_h/2),
                        arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

    # --- Context Vector (The Bottleneck) ---
    x_context = 9.5
    y_context = 1.25
    ax.annotate('Context Vector\n(The Bottleneck)', xy=(x_context, y_decoder + box_h), 
                xytext=(x_context, y_encoder),
                arrowprops=dict(facecolor='red', shrink=0.05, width=2),
                ha='center', va='center', fontweight='bold', color='red')

    # --- Decoder ---
    words_out = ["Bonjour", "comment", "vas-tu?"]
    for i, word in enumerate(words_out):
        x = 11 + (i * 2.5)
        # Hidden State Box
        rect = plt.Rectangle((x, y_decoder), box_w, box_h, fill=False, color='green', lw=2)
        ax.add_patch(rect)
        ax.text(x + box_w/2, y_decoder + box_h/2, f"s_{i+1}", ha='center', va='center', fontweight='bold')
        
        # Output Word
        ax.text(x + box_w/2, y_decoder - 0.3, word, ha='center', va='center', color='darkgreen')
        ax.annotate('', xy=(x + box_w/2, y_decoder - 0.1), xytext=(x + box_w/2, y_decoder),
                    arrowprops=dict(arrowstyle='<-', color='gray'))

        # Recurrent Arrow
        if i > 0:
            ax.annotate('', xy=(x, y_decoder + box_h/2), xytext=(x - 1, y_decoder + box_h/2),
                        arrowprops=dict(arrowstyle='->', color='green', lw=1.5))

    # Formatting
    ax.set_xlim(-1, 20)
    ax.set_ylim(-1, 4)
    ax.axis('off')
    plt.title("RNN Encoder-Decoder: The Information Bottleneck", fontsize=16, pad=20)
    
    # Save the diagram
    plt.savefig('rnn_bottleneck_diagram.png', dpi=300, bbox_inches='tight')
    print("Diagram saved to rnn_bottleneck_diagram.png")

if __name__ == "__main__":
    draw_rnn_flow()
