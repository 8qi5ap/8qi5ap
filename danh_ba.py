from guizero import *

danh_sach_so_dth = {}

def them_so_dth():
    new_window = Window(app, title="Thêm số điện thoại")
    space=Text(new_window, text=" ", size=10)
    message1=Text(new_window, text="Thêm số điện thoại", size=20, font="Arial")
    space=Text(new_window, text=" ", size=10)
    name=Text(new_window, text="Tên", size=20)
    input_name=TextBox(new_window, width=20,height=1)
    space=Text(new_window, text=" ", size=10)
    phone=Text(new_window, text="Số điện thoại", size=20)
    space=Text(new_window, text=" ", size=10)
    input_phone_number=TextBox(new_window, width=20,height=1)
    space=Text(new_window, text=" ", size=10)
    def them_so_vao_list():
        danh_sach_so_dth[input_name.value] = input_phone_number.value
        message=Text(app,text="Đã thêm số điện thoại", size=20, font="Arial")
        new_window.destroy()
    PushButton(new_window, text="OK", command=them_so_vao_list)


def xoa_so_dth():
    new_window = Window(app, title="Xóa số điện thoại")
    space=Text(new_window, text=" ", size=10)
    message1=Text(new_window, text="Xóa số điện thoại", size=20, font="Arial")
    space=Text(new_window, text=" ", size=10)
    name=Text(new_window, text="Tên", size=20)
    input_name=TextBox(new_window, width=20,height=1)
    space=Text(new_window, text=" ", size=10)
    def xoa_so():
        if input_name.value in danh_sach_so_dth:
            del danh_sach_so_dth[input_name.value]
            message=Text(app,text="Đã xóa số điện thoại", size=20, font="Arial")
        else:
            message=Text(app,text="Không tìm thấy số điện thoại", size=20, font="Arial")
        new_window.destroy()
    PushButton(new_window, text="OK", command=xoa_so)


def tim_so_dth():
    new_window = Window(app, title="Tìm số điện thoại")
    space=Text(new_window, text=" ", size=10)
    message1=Text(new_window, text="Tìm số điện thoại", size=20, font="Arial")
    space=Text(new_window, text=" ", size=10)
    name=Text(new_window, text="Tên", size=20)
    input_name=TextBox(new_window, width=20,height=1)
    space=Text(new_window, text=" ", size=10)
    def tim_so():
        if input_name.value in danh_sach_so_dth:
            message=Text(app,text="Số điện thoại: "+danh_sach_so_dth[input_name.value], size=20, font="Arial")
        else:
            message=Text(app,text="Không tìm thấy số điện thoại", size=20, font="Arial")
        new_window.destroy()
    PushButton(new_window, text="OK", command=tim_so)




app = App(title="Danh bạ điện thoại", width=700, height=200)
main_page = Box(app, layout="grid")

message=Text(main_page, text="DANH BẠ ĐIỆN THOẠI", size=20, font="Arial", grid=[1,0])
xoa_so =PushButton(main_page, text="Xóa số điện thoại",command=xoa_so_dth,grid=[1,2])
them_so =PushButton(main_page, text="Thêm số điện thoại",command=them_so_dth, grid=[0,3])
tim_so =PushButton( main_page  ,   text= "Tìm số điện thoại" ,command=tim_so_dth,grid=[2,3])
app.display()