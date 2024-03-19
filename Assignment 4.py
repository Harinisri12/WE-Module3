import random

def generate_text_data(num_sentences=100, min_sentence_length=5, max_sentence_length=20):
    lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    sentences = lorem_ipsum.split('. ')
    text_data = []
    for _ in range(num_sentences):
        sentence = random.choice(sentences)
        sentence_length = random.randint(min_sentence_length, max_sentence_length)
        words = sentence.split()
        if len(words) < sentence_length:
            text_data.append(' '.join(words))
        else:
            text_data.append(' '.join(random.sample(words, sentence_length)))
    return ' '.join(text_data)

def generate(filename: str, start_words: list[str], chain_length: int, num_generated: int) -> str:
    # Generate text data
    text_data = generate_text_data()
    
    # Tokenize the text into words
    words = text_data.split()
    
    # Create a dictionary of Markov chains
    markov_chains = {}
    for i in range(len(words) - chain_length):
        key = tuple(words[i:i + chain_length])
        value = words[i + chain_length]
        if key in markov_chains:
            markov_chains[key].append(value)
        else:
            markov_chains[key] = [value]
    
    # Generate a sentence
    current_words = tuple(start_words)
    sentence = list(current_words)
    for _ in range(num_generated):
        if current_words in markov_chains:
            next_word = random.choice(markov_chains[current_words])
            sentence.append(next_word)
            current_words = tuple(sentence[-chain_length:])
        else:
            break
    
    return ' '.join(sentence)

# Example usage:
filename = 'generated_text.txt'
start_words = ['Lorem', 'ipsum']
chain_length = 2
num_generated = 10
generated_sentence = generate(filename, start_words, chain_length, num_generated)
print(generated_sentence)

# Write generated text to a file
with open(filename, 'w') as file:
    file.write(generated_sentence)
