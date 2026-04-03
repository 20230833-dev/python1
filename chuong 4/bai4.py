import re

with open("demo_file1.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

# Tách từ (loại bỏ dấu câu)
words = re.findall(r'\w+', text)

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print("Kết quả đếm từ:")
print(count)
