from importlib.metadata import version
import tiktoken
print("tiktoken version:", version("tiktoken"))

tokenizer = tiktoken.get_encoding("gpt2")

with open("the-verdict.txt", "r") as file:
  raw_text = file.read()

encoded_text = tokenizer.encode(raw_text)
# Зашифровали текст из вердикт ткст в инпут токены

# print(len(encoded_text))
# убрали первые 50 токенов
enc_sample = encoded_text[50:]

context_size = 4 # контекст определяет сколько токенов будет использовано для инпута 
# x = enc_sample[:context_size]
# y = enc_sample[1:context_size+1]
# print(f"x: {x}")
# print(f"y: {y}")

# весь сок - предсказываем следующий токен
for i in range(1, context_size+1):
  # print(f"Context size: {i}")
  context = enc_sample[:i]
  desired = enc_sample[i]
  print(f"{context} ----> {desired}")
  print(f"{tokenizer.decode(context)} ----> {tokenizer.decode([desired])}")

  