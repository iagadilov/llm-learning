from importlib.metadata import version
import tiktoken
print("tiktoken version:", version("tiktoken"))

tokenizer = tiktoken.get_encoding("gpt2")

with open("the-verdict.txt", "r") as file:
  raw_text = file.read()

encoded_text = tokenizer.encode(raw_text)
# Зашифровали текст из вердикт ткст в инпут токены

print(len(encoded_text))