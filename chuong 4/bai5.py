import re

with open("demo_file1.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

words = re.findall(r'\w+', text)

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

# Tìm từ xuất hiện nhiều nhất
max_word = max(count, key=count.get)

print("Từ xuất hiện nhiều nhất:")
print(max_word, ":", count[max_word])
