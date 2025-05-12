# Nhập số từ người dùng
so = int(input("Nhập một số nguyên: ")) 
# Kiểm tra xem số đó có phải số chăn hay không 4 
if so % 2 == 0:
    print(so, "là số chắn.")
else:
    print(so, "không phải là số chẳn.")