text = input("Nhập đoạn văn: ")

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Đọc lại để hiển thị
with open("output.txt", "r", encoding="utf-8") as f:
    print("Nội dung file:")
    print(f.read())
