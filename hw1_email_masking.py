# hw1_email_masking.py
email = input("Nhập địa chỉ email: ")
#tách tên đăng nhập và email
ten_dang_nhap, ten_email = email.split("@")
#trích 3 kí tự đầu tiên của tên đăng nhập
ba_ki_tu = ten_dang_nhap[0:3]
#ghép email sau khi che tên
email_che = ba_ki_tu + "***@" + ten_email
#in ra kết quả
print("Địa chỉ email sau khi che:", email_che)
                                    
