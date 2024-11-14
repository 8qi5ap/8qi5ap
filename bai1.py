# tạo danh bạ(dictionary)
danh_ba = {}

# Hàm để thêm sđt vào danh bạ
def them_lien_lac(ten, so_dien_thoai):
    danh_ba[ten] = so_dien_thoai
    print(f"Đã thêm: {ten} - {so_dien_thoai}")

# Hàm để tìm kiếm liên lạc trong danh bạ
def tim_kiem_lien_lac(ten):
    if ten in danh_ba:
        print(f"Tìm thấy: {ten} - {danh_ba[ten]}")
    else:
        print("Không tìm thấy")

# Hàm để xóa liên lạc khỏi danh bạ
def xoa_lien_lac(ten):
     #Dòng này kiểm tra xem tên có tồn tại trong danh bạ hay không
    if ten in danh_ba:
        del danh_ba[ten]
        print(f"Đã xóa: {ten}")
    else:
        print("Không tìm thấy")

while True:
    lua_chon = input("thêm/tìm/xóa/thoát muốn chon cái nào?").lower()
    if lua_chon == 'thêm':
        ten = input("Nhập tên: ")
        so_dien_thoai = input("Nhập số điện thoại: ")
        them_lien_lac(ten, so_dien_thoai)
    elif lua_chon == 'tìm':
        ten = input("Nhập tên: ")
        tim_kiem_lien_lac(ten)
    elif lua_chon == 'xóa':
        ten = input("Nhập tên: ")
        xoa_lien_lac(ten)
    elif lua_chon == 'thoát':
        break
    else:
        print("Chọn không hợp lệ.")
