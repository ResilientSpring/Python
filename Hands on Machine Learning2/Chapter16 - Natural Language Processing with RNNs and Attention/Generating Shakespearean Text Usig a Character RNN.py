import tensorflow as tf

shakespeare_url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
filepath = tf.keras.utils.get_file("shakespeare.txt", shakespeare_url)
with open(filepath) as f:
    shakespeare_text = f.read()


print(shakespeare_text[:148])

# Initialize Java's tokenizer
tokenizer = tf.keras.preprocessing.text.Tokenizer(char_level=True)

# Fit a tokenizer to the text - tokenizer will find all the characters in the text and map them to
# a different character ID, as char_level = True, from 1 to the number of distinct characters.
# 0 is reserved for masking.
tokenizer.fit_on_texts([shakespeare_text])

print(tokenizer.texts_to_sequences(['First']))

print(tokenizer.sequences_to_texts([[20, 6, 9, 8, 3]]))

print(tokenizer.texts_to_sequences('Citizen'))

print(tokenizer.sequences_to_texts([[19], [6], [3], [6], [36], [2], [10]]))
