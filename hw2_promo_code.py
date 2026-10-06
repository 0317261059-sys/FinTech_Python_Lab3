# hw2_promo_code.py
# Nhập thông tin khách hàng
hoten = input("Nhập Họ Tên đầy đủ: ")
sinh = str(input("Nhập năm sinh: "))
# Dùng strip() loại bỏ khoảng trắng thừa
hoten_chuan = hoten.strip()
# Lấy tên
cac = hoten_chuan.split()
ten = cac[-1]
# Lấy 3 chữ cái đầu của tên và viết hoa
ba_ten = ten[:3].upper()
# Mã ưu đãi
ma = ba_ten + "-" + sinh + "-VIP"
# In hóa đơn
print("Mã ưu đãi:",ma)           
