
# STEP 1: LOAD TEXT FROM URL
# import urllib.request
# url = ("https://raw.githubusercontent.com/rasbt/"
# "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
# "the-verdict.txt")
# file_path = "the-verdict.txt"
# urllib.request.urlretrieve(url, file_path)

# STEP 2: Next, we can load the the-verdict.txt file using Python’s standard file reading utilities.
# with open("the-verdict.txt", "r", encoding="utf-8") as f:
#     raw_text = f.read()
#     print("Total number of character:", len(raw_text))
#     print(raw_text[:99])