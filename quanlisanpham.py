
import datetime

from datetime import date
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sql
from PIL import Image, ImageTk
from keras.utils import load_img
import time
import locale
# Kết nối tới cơ sở dữ liệu
db = sql.connect(
    host="127.0.0.1",
    user="root",
    password="Quangduy1805@",
    database="project"
)
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM khohang")
sohang = cursor.fetchone()
# Lấy ngày hiện tại
today = datetime.date.today()

# Định dạng ngày tháng
formatted_date = today.strftime('%Y-%m-%d')

thang = today.strftime('%m')
ngay = today.strftime('%d')

current_time = time.strftime('%H:%M:%S', time.localtime())
# In ngày tháng đã định dạng
def main_window():
    global maso, hd, tongtien, luachon, tong, tongcong, tien
    tong = "0"
    tongtien = 0
    maso = 0
    hd = "DH#000"
    luachon = ()
    tongcong = "0"
    tien = 0
    def tinhtien():
        global tongcong, tien
        tongcong = "0"
        tien = 0
        cursor.execute("SELECT COUNT(*) FROM giohang")
        ok = cursor.fetchone()[0]
        cursor.execute("SELECT * FROM giohang")
        datagiohang = cursor.fetchall()
        if ok == 0:
            tongcong = "0"
            tien=0
        elif ok!=0:
            for sp in datagiohang:
                tien += sp[5]
                tongcong = '{:,}'.format(tien)

    def hienlogo():
        load = load_img('C:\\Users\\QDuy\\OneDrive\\Máy tính\\EXE\\logo_truong.png',target_size=(50,50))
        render = ImageTk.PhotoImage(load)
        logo.configure(image=render, bg="pink")
        logo.image = render

    def back_to_login():
        main.destroy()
        dang_nhap()

    def san_pham():
        tinhtien()
        def chonsanpham(event):
            try:
                cur_item = table_sp.focus()
                item = table_sp.item(cur_item)
                values = item["values"]

                entry_ten.delete(0, END)
                entry_ten.insert(0, values[1])
                entry_ma.delete(0, END)
                entry_ma.insert(0, values[2])
                entry_soluong.delete(0, END)
            except: pass

        def on_select1(event=None):
            global val_loaisp, state1, state2, results1
            state1 = 1
            state2 = 0
            results1 = []
            val_loaisp = loai.get()
            val_brand =hang.get()
            print(val_loaisp)
            table_sp.delete(*table_sp.get_children())
            if val_loaisp == "Tất cả":
                for result in datasanpham:
                    gia = '{:,}'.format(result[4])
                    if int(result[3])>10:
                        trangthai = 'Còn hàng'
                        table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))
                    elif 0<int(result[3])<=10:
                        trangthai = 'Sắp hết hàng'
                        table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))
                    else:
                        trangthai = 'Hết hàng'
                        table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))
            else:
                if val_brand == "Tất cả":
                    val_brand = ""
                for rowsp in datasanpham:
                    if (val_brand == rowsp[5] and val_loaisp == rowsp[6]):
                        results1.append(rowsp)
                    elif (val_brand == "" and val_loaisp == rowsp[6]):
                        results1.append(rowsp)
            for result in results1:
                gia = '{:,}'.format(result[4])
                if int(result[3])>10:
                    trangthai = 'Còn hàng'
                    table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))
                elif 0<int(result[3])<=10:
                    trangthai = 'Sắp hết hàng'
                    table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))
                else:
                    trangthai = 'Hết hàng'
                    table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))

        def on_select2(event=None):
            global val_brand, state1, state2, results2
            state1 = 0
            state2 = 1
            results2 = []
            val_loaisp = loai.get()
            val_brand =hang.get()
            table_sp.delete(*table_sp.get_children())
            if val_brand == "Tất cả":
                for result in datasanpham:
                    gia = '{:,}'.format(result[4])
                    if int(result[3])>10:
                        trangthai = 'Còn hàng'
                        table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))
                    elif 0<int(result[3])<=10:
                        trangthai = 'Sắp hết hàng'
                        table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))
                    else:
                        trangthai = 'Hết hàng'
                        table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))
            else:
                if val_loaisp == "Tất cả":
                    val_loaisp = ""
                for rowsp in datasanpham:
                    if (val_brand == rowsp[5] and val_loaisp == rowsp[6]):
                        results2.append(rowsp)
                    elif (val_brand == rowsp[5] and val_loaisp == ""):
                        results2.append(rowsp)

            for result in results2:
                gia = '{:,}'.format(result[4])
                if int(result[3])>10:
                    trangthai = 'Còn hàng'
                    table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))
                elif 0<int(result[3])<=10:
                    trangthai = 'Sắp hết hàng'
                    table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))
                else:
                    trangthai = 'Hết hàng'
                    table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))

        def tim_kiem():
            val_loaisp = loai.get()
            val_brand =hang.get()
            print("check: ", val_loaisp, val_brand )
            ten = entry_ten.get()
            ma = entry_ma.get()
            results = []
            table_sp.delete(*table_sp.get_children())
            if val_loaisp == "Tất cả":
                val_loaisp = ""
            if val_brand == "Tất cả":
                val_brand = ""
            if (ten == "" and ma == "" and val_loaisp=="" and val_brand=="") or (ten == "" and ma == ""):
                messagebox.showerror("Tìm kiếm","Mời bạn nhập thông tin tìm kiếm!")
                for sp in datasanpham:
                    gia = '{:,}'.format(sp[4])
                    if int(sp[3])>10:
                        trangthai = 'Còn hàng'
                        table_sp.insert("", "end", values=(sp[0],sp[1], sp[2],trangthai,sp[3],gia,sp[5]))
                    elif 0<int(sp[3])<=10:
                        trangthai = 'Sắp hết hàng'
                        table_sp.insert("", "end", values=(sp[0],sp[1], sp[2],trangthai,sp[3],gia,sp[5]))
                    else:
                        trangthai = 'Hết hàng'
                        table_sp.insert("", "end", values=(sp[0],sp[1], sp[2],trangthai,sp[3],gia,sp[5]))
            elif isinstance(ten, str) and ma == "" and state1 == 0 and state2==0:

                    for rowsp in datasanpham:
                        if (ten == rowsp[1]):
                            results.append(rowsp)
            elif isinstance(ma, str) and ten == "" and state1 == 0 and state2==0:

                    for rowsp in datasanpham:
                        if (ma == rowsp[2]):
                            results.append(rowsp)
            elif isinstance(ten, str) and isinstance(ma, str) and state1 == 0 and state2==0:

                    for rowsp in datasanpham:
                        if (ten == rowsp[1] and ma == rowsp[2]):
                            results.append(rowsp)
            elif isinstance(val_loaisp, str) and val_brand.isalpha() :
                if state1 == 1:
                    for rowsp in results1:
                        if (ten == rowsp[1] and ma == "" ) or (ten == "" and ma == rowsp[2]):
                            results.append(rowsp)
                        if (ten == rowsp[1] and ma == rowsp[2]):
                            results.append(rowsp)
                if state2 == 1:
                    for rowsp in results2:
                        if (ten == rowsp[1] and ma == "" ) or (ten == "" and ma == rowsp[2]):
                            results.append(rowsp)
                        if (ten == rowsp[1] and ma == rowsp[2]):
                            results.append(rowsp)
            elif val_loaisp=="" and val_brand.isalpha():
                if state2 == 1:
                    for rowsp in results1:
                        if (ten == rowsp[1] and ma == "" ) or (ten == "" and ma == rowsp[2]):
                            results.append(rowsp)
                        if (ten == rowsp[1] and ma == rowsp[2]):
                            results.append(rowsp)
            elif isinstance(val_loaisp, str) and val_brand=="":
                if state1 == 1:
                    for rowsp in results2:
                        if (ten == rowsp[1] and ma == "" ) or (ten == "" and ma == rowsp[2]):
                            results.append(rowsp)
                        if (ten == rowsp[1] and ma == rowsp[2]):
                            results.append(rowsp)


            for result in results:
                gia = '{:,}'.format(result[4])
                if int(result[3])>10:
                    trangthai = 'Còn hàng'
                    table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))
                elif 0<int(result[3])<=10:
                    trangthai = 'Sắp hết hàng'
                    table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))
                else:
                    trangthai = 'Hết hàng'
                    table_sp.insert("", "end", values=(result[0],result[1], result[2],trangthai,result[3],gia,result[5]))
            print("Kết quả: ", results)

        def themvaogio():
            global tongtien, luachon, tong
            ten = entry_ten.get()
            ma = entry_ma.get()
            soluong = entry_soluong.get()
            if (ten=="" and ma == "" and soluong=="") or (isinstance(ten,str) and ma == "" and soluong=="") or (isinstance(ma,str) and ten == "" and soluong=="") or (ma=="" and ten == "" and soluong.isdigit()):
                messagebox.showerror("","Mời nhập đầy đủ Tên sản phẩm, Mã sản phẩm và Số lượng mua!")
            elif (ten=="" or ma=="" or soluong==""):
                messagebox.showerror("","Mời nhập đầy đủ Tên sản phẩm, Mã sản phẩm và Số lượng mua!")
            elif  (isinstance(ten and ma,str) and soluong.isalpha()):
                messagebox.showerror("","Số lượng mua là chữ số!")
            elif (isinstance(ten,str) and isinstance(ma,str)  and soluong.isdigit()):
                cursor.execute("SELECT * FROM sanpham WHERE Tensanpham=%s AND Masanpham=%s", (ten, ma))
                sp = cursor.fetchone()

            try:
                if sp:
                    a = "UPDATE sanpham SET Soluong = %s WHERE Tensanpham = %s AND Masanpham = %s"
                    sql = "INSERT INTO giohang (Hoadon, Tensanpham, Masanpham, Soluong, Tong, Loai, Thuonghieu) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    if (int(soluong) <= int(sp[3])):
                        conlai = int(sp[3])-int(soluong)
                        tien1sp = int(soluong)*sp[4]
                        luachon = (hd, sp[1], sp[2], soluong, tien1sp, sp[6], sp[5])
                        b = (conlai, ten, ma)
                    elif (int(soluong) > int(sp[3]) > 0):
                        conlai = 0
                        tien1sp = int(sp[3])*sp[4]
                        luachon = (hd, sp[1], sp[2], int(sp[3]), tien1sp, sp[6], sp[5])
                        b = (conlai, ten, ma)
                        messagebox.showinfo("", "Đã lấy toàn bộ {:s} vì số lượng yêu cầu nhiều hơn!".format(sp[1]))
                    elif (int(soluong) > int(sp[3])==0):
                        messagebox.showinfo("", "{:s} đã hết hàng!".format(sp[1]))
                    cursor.execute(sql, luachon)
                    cursor.execute(a,b)
                    db.commit()
                    tinhtien()
                    entry_tongtien.delete(0, END)
                    entry_tongtien.insert(0, tongcong)
                else:
                    messagebox.showerror("","Không có sản phẩm này!")

            except: pass
            treeview()

        state1 = 0
        state2 = 0
        #Tên tab
        Label_tab.configure(text='SẢN PHẨM')

        #Tắt các frame khác
        frame_doanhthu.place_forget()
        frame_giohang.place_forget()
        frame_nhansu.place_forget()
        frame_taikhoan.place_forget()
        frame_khohang.place_forget()

        #Mở frame doanh thu
        frame_sanpham.place(x=175, y=50)
        def treeview():
            global table_sp, datasanpham
            table_sp = ttk.Treeview(frame_sanpham, selectmode='extended')
            table_sp['columns'] =('STT','SẢN PHẨM','MÃ SẢN PHẨM ','TRẠNG THÁI','SỐ LƯỢNG','GIÁ','HÃNG')
            scrollbar_sanpham = Scrollbar(table_sp, orient="vertical")
            a=list(table_sp['columns'])

            table_sp.column("#0", width=0, stretch=NO)
            table_sp.heading("#0", text="", anchor=CENTER)
            table_sp.column(a[0], anchor=CENTER, width=30)
            table_sp.heading(a[0], text=a[0], anchor=CENTER)

            table_sp.column(a[1], anchor=CENTER, width=170)
            table_sp.heading(a[1], text=a[1], anchor=CENTER)

            table_sp.column(a[5], anchor=CENTER, width=80)
            table_sp.heading(a[5], text=a[5], anchor=CENTER)

            table_sp.column(a[6], anchor=CENTER, width=95)
            table_sp.heading(a[6], text=a[6], anchor=CENTER)
            table_sp.bind("<ButtonRelease-1>", chonsanpham)
            for i in a[2:5]:
                table_sp.column(i, anchor=CENTER, width=100)
                table_sp.heading(i, text=i, anchor=CENTER)

            scrollbar_sanpham.config(command=table_sp.yview)
            table_sp.configure(yscrollcommand=scrollbar_sanpham.set)

            scrollbar_sanpham.pack(side="right", fill="y")
            table_sp.place(x=50,y=50,width=900,height=150)

            cursor.execute("SELECT * FROM sanpham")
            datasanpham = cursor.fetchall()

            for sp in datasanpham:
                gia = '{:,}'.format(sp[4])
                if int(sp[3])>10:
                    trangthai = 'Còn hàng'
                    table_sp.insert("", "end", values=(sp[0],sp[1], sp[2],trangthai,sp[3],gia,sp[5]))
                elif 0<int(sp[3])<=10:
                    trangthai = 'Sắp hết hàng'
                    table_sp.insert("", "end", values=(sp[0],sp[1], sp[2],trangthai,sp[3],gia,sp[5]))
                else:
                    trangthai = 'Hết hàng'
                    table_sp.insert("", "end", values=(sp[0],sp[1], sp[2],trangthai,sp[3],gia,sp[5]))

        treeview()

        label_loai = Label(frame_sanpham, text="Loại sản phẩm:", font=('TIME', 11), bg='light grey', anchor='center')
        label_loai.place(x=580,y=25,width=120)
        loai = ttk.Combobox(frame_sanpham, values=['Tất cả','Bàn phím','Chuột','Tai nghe','Ghế Gaming'])
        loai.place(x=700, y= 25, width=100,height=25)
        loai.bind("<<ComboboxSelected>>", on_select1)

        label_hang = Label(frame_sanpham, text="Hãng:", font=('TIME', 11), bg='light grey', anchor='center')
        label_hang.place(x=800,y=25,width=50)
        hang = ttk.Combobox(frame_sanpham, values=['Tất cả','Logitech','Razer','Asus','Fuhlen','Dare-U'])
        hang.place(x=850, y= 25, width=100,height=25)
        hang.bind("<<ComboboxSelected>>", on_select2)

        #Frame tìm kiếm và Button
        frame_timkiem = Frame(frame_sanpham, height = 100, width= 900, bg='light gray')
        frame_timkiem.place(x=50, y=200)

        #Frame Button
        frame_button = Frame(frame_timkiem, height = 30, width= 900, bg='light gray')
        frame_button.place(x=0, y=70)

        timkiem = Button(frame_button, text="Tìm kiếm", font=('TIME', 11), bg='light yellow', command=tim_kiem)
        timkiem.place(x=0, y=0, width=300,height=30)

        them = Button(frame_button, text="Thêm vào giỏ", font=('TIME', 11), bg='light yellow', command=themvaogio)
        them.place(x=300, y=0, width=300,height=30)

        lammoi = Button(frame_button, text="Làm mới", font=('TIME', 11), bg='light yellow', command=san_pham)
        lammoi.place(x=600, y=0, width=300,height=30)

        #Frame label
        frame_label = Frame(frame_timkiem, height = 40, width= 900, bg='light gray')
        frame_label.place(x=10, y=15)

        label_ten = Label(frame_label, text="Sản phẩm:", font=('TIME', 11), bg='light gray', anchor='w')
        label_ten.place(x=0, y=10, width=80)

        entry_ten = Entry(frame_label, font=('TIME', 11))
        entry_ten.place(x=80, y=10, width=125)

        label_ma = Label(frame_label, text="Mã sản phẩm:", font=('TIME', 11), bg='light gray', anchor='w')
        label_ma.place(x=215, y=10, width=100)

        entry_ma = Entry(frame_label, font=('TIME', 11))
        entry_ma.place(x=320, y=10, width=100)

        label_soluong = Label(frame_label, text="Số lượng mua:", font=('TIME', 11), bg='light gray', anchor='w')
        label_soluong.place(x=425, y=10, width=100)

        entry_soluong = Entry(frame_label, font=('TIME', 11))
        entry_soluong.place(x=530, y=10, width=100)

        label_tongtien = Label(frame_label, text="Tổng hóa đơn:", font=('TIME', 11), bg='light gray', anchor='w')
        label_tongtien.place(x=635, y=10, width=100)

        entry_tongtien = Entry(frame_label, font=('TIME', 11))
        entry_tongtien.place(x=740, y=10, width=100)



        entry_tongtien.delete(0,END)
        entry_tongtien.insert(INSERT, tongcong)

        entry_tongtien.bind("<Button-1>", "break")

    def gio_hang():

        global hd, maso, sp_ten, sp_ma, sl
        sp_ten = ""
        sp_ma = ""
        sl = ""
        Label_tab.configure(text='GIỎ HÀNG')

        #Tắt các frame khác
        frame_doanhthu.place_forget()
        frame_sanpham.place_forget()
        frame_nhansu.place_forget()
        frame_taikhoan.place_forget()
        frame_khohang.place_forget()

        #Mở frame doanh thu
        frame_giohang.place(x=175, y=50)
        def on_entry_change(event):
            value= entry_tienkhach.get()
            """ Xử lý sự kiên thay đổi đầu vào  """
            try:
                # Chuyển đổi giá trị entry sang kiểu số float
                value = int(value.replace('.', ''))
            except ValueError:
                # Nếu giá trị không phải kiểu số
                value = 0

            # Định dạng giá trị theo chuỗi có phân cách hàng chữ số
            formatted_value = locale.format_string("%d",value, grouping=True)


            # # Cập nhật entry với giá trị mới đã định dạng
            entry_tienkhach.delete(0, END)
            entry_tienkhach.insert(0, formatted_value)

        # Thiết lập locale
        locale.setlocale(locale.LC_ALL, 'vi_VN.utf8')
        global gh
        cursor.execute("SELECT COUNT(*) FROM giohang")
        gh = cursor.fetchone()[0]

        def select_item(event):
            global sp_ten, sp_ma, sl
            try:

                cur_item = table_giohang.focus()
                item = table_giohang.item(cur_item)
                values = item["values"]
                sp_ten = values[2]
                sp_ma = values[3]
                sl = values[4]
                entry_ten.delete(0, END)
                entry_ten.insert(0, values[2])
                entry_ma.delete(0, END)
                entry_ma.insert(0, values[3])
                entry_soluong.delete(0, END)
                entry_soluong.insert(0, values[4])

            except: pass

        def huydon():
            global gh

            if gh==0:
                messagebox.showwarning("","Chưa có đơn hàng trong giỏ!")
                breakpoint
            else:
                box = messagebox.askokcancel(title="",message="Bạn có chắc chắn hủy hết đơn hàng")
                if box:
                    for dh in datagiohang:
                        for sp in datasanpham:
                            if (dh[2]==sp[1] and dh[3]==sp[2]):
                                soluong = str(int(sp[3])+dh[4])
                                cursor.execute("UPDATE sanpham SET Soluong = %s WHERE Tensanpham = %s AND Masanpham = %s",(soluong, dh[2], dh[3]))
                                cursor.execute("TRUNCATE TABLE giohang")
                                db.commit()
                else:
                    breakpoint()
                gio_hang()

        def xoadon():
            if sp_ten == "" and sp_ma == "" and sl == "":
                messagebox.showwarning("", "Chưa chọn đơn hàng!")
            else:
                box = messagebox.askokcancel(title="",message="Bạn có chắc chắn xóa mặt hàng ({:s}) với mã ({:s})".format(sp_ten, sp_ma))
                if box:
                    cursor.execute("SELECT * FROM sanpham WHERE Tensanpham = %s AND Masanpham = %s", (sp_ten, sp_ma))
                    checksp = cursor.fetchone()
                    if checksp:
                        luong = int(sl)+ int(checksp[3])
                        cursor.execute("UPDATE sanpham SET Soluong = %s WHERE Tensanpham = %s AND Masanpham = %s",(luong, sp_ten, sp_ma))
                        cursor.execute("DELETE FROM giohang WHERE Tensanpham=%s AND Masanpham=%s", (sp_ten, sp_ma))
                        db.commit()
                        messagebox.showinfo("","Bạn đã xóa đon hàng ({:s}) với mã ({:s})".format(sp_ten, sp_ma))
                        gio_hang()
                else:
                    breakpoint()

        def capnhatdon():
            global tongtien, tong
            soluongsau= entry_soluong.get()
            # print(sp_ten,sp_ma, sl)
            if sp_ten == "" and sp_ma == "" and sl == "":
                messagebox.showerror("", "Chưa chọn đơn hàng!")
            elif isinstance(sp_ten and sp_ma,str) and soluongsau == "":
                messagebox.showerror("", "Chưa nhập số lượng mua!")
            elif isinstance(sp_ten and sp_ma,str) and soluongsau.isdigit():
                cursor.execute("SELECT * FROM sanpham WHERE Tensanpham = %s AND Masanpham = %s", (sp_ten, sp_ma))
                checksp = cursor.fetchone()
                if checksp:
                    # print(2)
                    if int(soluongsau)==0:
                        xoadon()
                    else:

                        if 0< int(soluongsau) < int(sl):
                            conlai = (int(checksp[3])) + (int(sl)-int(soluongsau))
                            # tongtien = tongtien - ((int(sl)-int(soluongsau))*checksp[4])
                            tien1sp = checksp[4]*int(soluongsau)
                            # print(3)
                        elif int(soluongsau) > int(sl):
                            if 0 < int(soluongsau) <= (int(checksp[3])+int(sl)):
                                conlai = int(checksp[3])+int(sl)-int(soluongsau)
                                tien1sp = checksp[4]*int(soluongsau)
                                # tongtien = tongtien + ((int(soluongsau)-int(sl))*checksp[4])
                            elif 0 < (int(checksp[3])+int(sl)) < int(soluongsau):
                                # print(2)
                                conlai = 0
                                soluongsau = (int(checksp[3])+int(sl))
                                tien1sp = checksp[4]*int(soluongsau)
                                # tongtien = tongtien + ((int(soluongsau)-int(sl))*checksp[4])
                                messagebox.showinfo("", "Đã lấy toàn bộ {:s} vì số lượng yêu cầu nhiều hơn!".format(sp_ten))
                            elif 0 == int(checksp[3]) and (int(sl) < int(soluongsau)):
                                messagebox.showinfo("", "{:s} đã hết hàng, có thể lấy {:d} hoặc ít hơn!".format(sp_ten, int(sl)))
                            # elif  0 == int(checksp[3]):
                            #     messagebox.showinfo("", "{:s} đã hết hàng, có thể lấy {:d} hoặc ít hơn!".format(sp_ten, int(sl)))
                        elif int(soluongsau) == int(sl):
                            breakpoint()
                        cursor.execute("UPDATE sanpham SET Soluong = %s WHERE Tensanpham = %s AND Masanpham = %s",(conlai, sp_ten, sp_ma))
                        cursor.execute("UPDATE giohang SET Soluong = %s, Tong = %s  WHERE Tensanpham = %s AND Masanpham = %s",(int(soluongsau), tien1sp , sp_ten, sp_ma))
                        db.commit()
                        messagebox.showinfo("","Đã cập nhật")
            gio_hang()

        def thanhtoan():
            global maso,gh
            if gh==0:
                messagebox.showwarning("","Chưa có đơn hàng trong giỏ!")
                breakpoint
            else:
                thungan = data[1].split(" ")

                tenkhach = entry_tenkhach.get()

                khachtra = entry_tienkhach.get()
                if khachtra=="":
                    messagebox.showwarning("","Vui lòng nhập số tiền thanh toán!")
                    breakpoint
                else:
                    tientra = int(khachtra.replace('.', ''))
                    cursor.execute("SELECT COUNT(*) FROM giohang")
                    ok = cursor.fetchone()[0]
                    if ok == 0:
                        messagebox.showerror("","Không có đơn hàng nào trong giỏ!")
                    else:
                        box = messagebox.askokcancel(title="",message="Bạn có chắc chắn thanh toán đơn hàng?")
                        if box:
                            if khachtra == "" or khachtra[0].isalpha():
                                messagebox.showerror("","Số tiền không hợp lệ!")
                            elif khachtra[0].isdigit:
                                cursor.execute("SELECT * FROM giohang")
                                datagiohang = cursor.fetchall()
                                for dh in datagiohang:
                                    cursor.execute("INSERT INTO giohangluutru (Hoadon, Tensanpham, Masanpham, Soluong, Tong, Loai, Thuonghieu) VALUES (%s, %s, %s, %s, %s, %s, %s)",dh[1:])
                                cursor.execute("TRUNCATE TABLE giohang")
                                cursor.execute("INSERT INTO doanhthungay (MaHoaDon, ThuNgan, TongHoaDon, KhachTra, Gio, TenKhach, Ngay, Thang, Donvingay) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",(hd, thungan[-1], tien, tientra, current_time, tenkhach, formatted_date, thang, ngay))
                                db.commit()
                        else:
                            breakpoint
                    maso +=1
                    gio_hang()
        if 0<= maso <10:
            hd = "DH#00"+str(maso)
        elif 10<= maso <100:
            hd = "DH#0"+str(maso)
        else:
            hd = "DH#"+str(maso)

        table_giohang = ttk.Treeview(frame_giohang, selectmode='extended')
        table_giohang['columns'] =('STT','HÓA ĐƠN','TÊN SẢN PHẨM ','MÃ SẢN PHẨM ','SỐ LƯỢNG','TỔNG TIỀN','LOẠI','HÃNG')
        scrollbar_giohang = Scrollbar(table_giohang, orient="vertical")
        a=list(table_giohang['columns'])
        table_giohang.column("#0", width=0, stretch=NO)
        table_giohang.heading("#0", text="", anchor=CENTER)
        table_giohang.bind("<ButtonRelease-1>", select_item)

        for i in a:
            table_giohang.column(i, anchor=CENTER, width=100)
            table_giohang.heading(i, text=i, anchor=CENTER)

        scrollbar_giohang.config(command=table_giohang.yview)
        table_giohang.configure(yscrollcommand=scrollbar_giohang.set)

        scrollbar_giohang.pack(side="right", fill="y")
        table_giohang.place(x=50,y=50,width=900,height=150)

        cursor.execute("SELECT * FROM giohang")
        datagiohang = cursor.fetchall()
        for sp in datagiohang:
            gia = '{:,}'.format(sp[5])
            table_giohang.insert("", "end", values=(sp[0],sp[1],sp[2],sp[3],sp[4],gia,sp[6],sp[7]))

        #Frame chỉnh sửa
        frame_chinhsua = Frame(frame_giohang, height = 100, width= 900, bg='light gray')
        frame_chinhsua.place(x=50,y=200)

        frame_entry = Frame(frame_chinhsua, height = 30, width= 900, bg='light gray')
        frame_entry.place(x=0,y=5)

        label_ten = Label(frame_entry, text="Tên sản phẩm:", font=('TIME', 11), bg='light gray', anchor='w')
        label_ten.place(x=15, y=4, width=100)

        entry_ten = Entry(frame_entry, font=('TIME', 11))
        entry_ten.place(x=120, y=4, width=140)
        entry_ten.bind("<Button-1>", "break")

        label_tenkhach = Label(frame_entry, text="Tên khách hàng:", font=('TIME', 11), bg='light gray', anchor='w')
        label_tenkhach.place(x=280, y=4, width=200)

        entry_tenkhach = Entry(frame_entry, font=('TIME', 11))
        entry_tenkhach.place(x=485, y=4, width=125)

        #Frame thông tin trả tiền
        frame_tratien = Frame(frame_chinhsua, height = 30, width= 900, bg='light gray')
        frame_tratien.place(x=0,y=35)

        label_ma = Label(frame_tratien, text="Mã sản phẩm:", font=('TIME', 11), bg='light gray', anchor='w')
        label_ma.place(x=15, y=4, width=100)

        entry_ma = Entry(frame_tratien, font=('TIME', 11))
        entry_ma.place(x=120, y=4, width=140)
        entry_ma.bind("<Button-1>", "break")

        label_tienkhach = Label(frame_entry, text="Tiền khách trả:", font=('TIME', 11), bg='light gray', anchor='w')
        label_tienkhach.place(x=630, y=4, width=100)

        entry_tienkhach = Entry(frame_entry, font=('TIME', 11))
        entry_tienkhach.place(x=745, y=4, width=140)
        entry_tienkhach.bind('<KeyRelease>', on_entry_change)

        label_soluong = Label(frame_tratien, text="Số lượng (thay đổi nếu muốn):", font=('TIME', 11), bg='light gray', anchor='w')
        label_soluong.place(x=280, y=4, width=200)

        entry_soluong = Entry(frame_tratien, font=('TIME', 11))
        entry_soluong.place(x=485, y=4, width=125)


        label_tonghoadon = Label(frame_tratien, text="Tổng hóa đơn:", font=('TIME', 11), bg='light gray', anchor='w')
        label_tonghoadon.place(x=630, y=4, width=100)

        entry_tonghoadon = Entry(frame_tratien, font=('TIME', 11))
        entry_tonghoadon.place(x=745, y=4, width=140)
        entry_tonghoadon.bind("<Button-1>", "break")

        tinhtien()

        entry_tonghoadon.delete(0,END)
        entry_tonghoadon.insert(0,tongcong)

        #Frame thông tin trả tiền
        frame_button = Frame(frame_chinhsua, height = 30, width= 900, bg='light yellow')
        frame_button.place(x=0,y=70)

        huy = Button(frame_button, text="Hủy đơn", font=('TIME', 11), bg='light yellow', command=huydon)
        huy.place(x=0, y=0, width=225,height=30)

        xoa = Button(frame_button, text="Xóa mặt hàng", font=('TIME', 11), bg='light yellow', command=xoadon)
        xoa.place(x=225, y=0, width=225,height=30)

        capnhat = Button(frame_button, text="Cập nhật đơn", font=('TIME', 11), bg='light yellow',command=capnhatdon)
        capnhat.place(x=450, y=0, width=225,height=30)

        mua = Button(frame_button, text="Thanh toán", font=('TIME', 11), bg='light yellow', command=thanhtoan)
        mua.place(x=675, y=0, width=225,height=30)

    def nhan_su():
        def xoa_nguoi():
            if data[10]=="Quản lí":
                if hovaten =="" or ten_dangnhap=="" or (hovaten =="" and ten_dangnhap==""):
                    messagebox.showerror("","Vui lòng chọn người cần xóa trên bảng hoặc điền đầy đủ Họ tên và Tên đăng nhập!")
                elif isinstance(hovaten and ten_dangnhap, str):
                    box = messagebox.askokcancel(title="",message="Bạn có chắc chắn xóa người {:s} với chức vụ {:s} ?".format(hovaten, chuc__vu))
                    if box:
                        cursor.execute("DELETE FROM taikhoan WHERE Fullname = %s AND Username=%s", (hovaten, ten_dangnhap))
                        db.commit()
                    else:
                        breakpoint
                nhan_su()
            else:
                messagebox.showwarning("","Chỉ có Quản Lí được phép chỉnh sửa!")

        def nut_cap_nhat():
            from datetime import datetime
            try:
                if data[10]=="Quản lí":
                    name = entry_ten.get()
                    gender = entry_gioitinh.get()
                    roles = entry_chuc_vu.get()
                    dob = entry_ngay_sinh.get()
                    phone = entry_sodienthoai.get()
                    str_ngaylam = entry_ngay_nhan_viec.get()
                    ok = 0
                    okk=0
                    # print(name,gender,roles,dob,phone,str_ngaylam)
                    # print(values[1:3]+values[4:8])
                    if name == "" and gender=="" and roles=="" and dob=="" and phone=="" and str_ngaylam=="":
                        messagebox.showerror("","Chưa có thông tin cập nhật!")
                    elif name == values[1] and gender==values[3] and roles==values[6] and dob==values[4] and phone==str("0"+str(values[5])) and str_ngaylam==values[7]:
                        messagebox.showerror("","Thông tin chưa được thay đổi vì giống nhau!")
                    elif name != values[1] or gender!=values[3] or roles!=values[6] or phone!=values[5] or str_ngaylam!=values[7]:

                        if isinstance(str_ngaylam,str):
                            for i in str_ngaylam:
                                if i == "-":
                                    okk +=1
                            if okk == 2 and len(str_ngaylam)==10:
                                if str_ngaylam[2] != "-" and str_ngaylam[5] != "-":
                                    messagebox.showerror("","Ngày nhận việc không nhập đúng cú pháp!")
                                else:
                                    ngaylam = datetime.strptime(str_ngaylam, '%d-%m-%Y').date()
                                    cursor.execute("UPDATE taikhoan SET Fullname = %s, Gioitinh = %s, Chucvu = %s , SDT=%s, Ngaynhanviec=%s WHERE Username = %s", (name, gender, roles, phone, ngaylam, ten_dangnhap,))
                            elif str_ngaylam=="":
                                pass
                            else:
                                messagebox.showerror("","Ngày nhận việc không nhập đúng cú pháp!")

                    if dob!=values[4]:
                        for i in dob:
                            if i == "-":
                                ok +=1
                                print(2)
                        if ok == 2 and len(dob)==10:
                            if dob[2] != "-" and dob[5] != "-":
                                messagebox.showerror("","Ngày sinh không nhập đúng cú pháp!")
                            else:
                                dob = dob.split("-")
                                cursor.execute("UPDATE taikhoan SET Fullname = %s, Gioitinh = %s, Chucvu = %s, Ngay = %s, Thang = %s, Nam=%s , SDT=%s, Ngaynhanviec=%s WHERE Username = %s",(name, gender, roles, str(dob[0]),str(dob[1]),str(dob[2]), phone, ngaylam, ten_dangnhap) )
                        elif dob=="":
                            cursor.execute("UPDATE taikhoan SET Fullname = %s, Gioitinh = %s, Chucvu = %s, Ngay = %s, Thang = %s, Nam=%s , SDT=%s, Ngaynhanviec=%s WHERE Username = %s",(name, gender, roles, "","","", phone, ngaylam, ten_dangnhap) )
                        else:
                            messagebox.showerror("","Ngày sinh không nhập đúng cú pháp!")
                    db.commit()
                    nhan_su()
                elif data[10]=="Nhân viên":
                    messagebox.showwarning("","Chỉ có Quản Lí được phép chỉnh sửa!")
            except: messagebox.showerror("","Vui lòng chọn thông tin trên bảng!")

        def select_item(event):
            global hovaten, ten_dangnhap, sdt, chuc__vu, values
            try:

                cur_item = table_nhansu.focus()
                item = table_nhansu.item(cur_item)
                values = item["values"]

                hovaten = values[1]
                ten_dangnhap = values[2]
                sdt = values[5]
                chuc__vu = values[6]

                entry_ten.delete(0, END)
                entry_ten.insert(0, values[1])

                entry_tendangnhap.delete(0, END)
                entry_tendangnhap.insert(0, values[2])

                entry_gioitinh.delete(0, END)
                entry_gioitinh.insert(0, values[3])

                entry_ngay_sinh.delete(0, END)
                entry_ngay_sinh.insert(0, values[4])

                entry_sodienthoai.delete(0, END)
                entry_sodienthoai.insert(0, "0"+str(values[5]))

                entry_chuc_vu.delete(0, END)
                entry_chuc_vu.insert(0, values[6])

                entry_ngay_nhan_viec.delete(0, END)
                entry_ngay_nhan_viec.insert(0, values[7])

            except: pass
        Label_tab.configure(text='NHÂN SỰ')

        #Tắt các frame khác
        frame_doanhthu.place_forget()
        frame_sanpham.place_forget()
        frame_giohang.place_forget()
        frame_taikhoan.place_forget()
        frame_khohang.place_forget()

        #Mở frame doanh thu
        frame_nhansu.place(x=175, y=50)

        table_nhansu= ttk.Treeview(frame_nhansu, selectmode='extended')
        table_nhansu['columns'] =('STT','Họ và tên','Tên đăng nhập','Giới tính','Ngày sinh','Số điện thoại','Chức vụ', 'Ngày nhận việc')
        a=list(table_nhansu['columns'])
        scrollbar_nhansu = Scrollbar(table_nhansu, orient="vertical")
        table_nhansu.column("#0", width=0, stretch=NO)
        table_nhansu.heading("#0", text="", anchor=CENTER)
        table_nhansu.bind("<ButtonRelease-1>", select_item)

        table_nhansu.column(a[0], anchor=CENTER, width=30)
        table_nhansu.heading(a[0], text=a[0], anchor=CENTER)
        table_nhansu.column(a[3], anchor=CENTER, width=70)
        table_nhansu.heading(a[3], text=a[3], anchor=CENTER)
        table_nhansu.column(a[1], anchor=CENTER, width=120)
        table_nhansu.heading(a[1], text=a[1], anchor=CENTER)

        table_nhansu.column(a[2], anchor=CENTER, width=100)
        table_nhansu.heading(a[2], text=a[2], anchor=CENTER)

        for i in a[4:8]:
            table_nhansu.column(i, anchor=CENTER, width=100)
            table_nhansu.heading(i, text=i, anchor=CENTER)

        scrollbar_nhansu.config(command=table_nhansu.yview)
        table_nhansu.configure(yscrollcommand=scrollbar_nhansu.set)

        scrollbar_nhansu.pack(side="right", fill="y")
        table_nhansu.place(x=50,y=50,width=900,height=150)

        cursor.execute("SELECT * FROM taikhoan")
        datanhansu = cursor.fetchall()
        gender = ""
        for ns in datanhansu:
            gender = ns[2]
            if (ns[4]=="" and ns[5]=="" and ns[6]=="") or (ns[4] is None and ns[5] is None and ns[6] is None ):
                ngaysinh = "Chưa cập nhật"
            if ns[2] is None:
                gender = "Chưa cập nhật"
            elif ns[4].isdigit() and ns[5].isdigit() and ns[6].isdigit():
                ngaysinh = ns[4]+"-"+ns[5]+"-"+ns[6]
            ngaynhanviec = ns[12].strftime('%d-%m-%Y')
            table_nhansu.insert("", "end", values=(ns[0],ns[1],ns[8],gender,ngaysinh,ns[9],ns[10],ngaynhanviec))


        #Frame Button, Entry
        frame_chinhsua = Frame(frame_nhansu, height = 100, width= 900, bg='light gray')
        frame_chinhsua.place(x=50, y=200)

        #Frame 1
        frame_1 = Frame(frame_chinhsua, height = 30, width= 900, bg='light gray')
        frame_1.place(x=0, y=5)

        ten=Label(frame_1, text='Họ và tên:', font=('TIME', 11), bg='light gray')
        ten.place(x=10, y=3, width= 90)
        entry_ten=Entry(frame_1, font=('TIME', 11))
        entry_ten.place(x=100, y=3, width= 190)

        tendangnhap =Label(frame_1, text='Tên đăng nhập:', font=('TIME', 11), bg='light gray')
        tendangnhap.place(x=295, y=3, width= 100)
        entry_tendangnhap=Entry(frame_1, font=('TIME', 11))
        entry_tendangnhap.place(x=400, y=3, width= 100)

        gioitinh =Label(frame_1, text='Giới tính:', font=('TIME', 11), bg='light gray')
        gioitinh.place(x=505, y=3, width= 100)
        entry_gioitinh=Entry(frame_1, font=('TIME', 11))
        entry_gioitinh.place(x=610, y=3, width= 100)

        chuc_vu =Label(frame_1, text='Chức vụ:', font=('TIME', 11), bg='light gray')
        chuc_vu.place(x=715, y=3, width= 70)
        entry_chuc_vu=Entry(frame_1, font=('TIME', 11))
        entry_chuc_vu.place(x=790, y=3, width= 100)

        #Frame 2
        frame_2 = Frame(frame_chinhsua, height = 30, width= 900, bg='light gray')
        frame_2.place(x=0, y=35)

        ngay_sinh=Label(frame_2, text='Ngày sinh:', font=('TIME', 11), bg='light gray')
        ngay_sinh.place(x=10, y=3, width= 90)
        entry_ngay_sinh=Entry(frame_2, font=('TIME', 11))
        entry_ngay_sinh.place(x=100, y=3, width= 190)

        sodienthoai =Label(frame_2, text='Số điện thoại:', font=('TIME', 11), bg='light gray')
        sodienthoai.place(x=295, y=3, width= 100)
        entry_sodienthoai=Entry(frame_2, font=('TIME', 11))
        entry_sodienthoai.place(x=400, y=3, width= 100)

        ngay_nhan_viec =Label(frame_2, text='Ngày nhận việc:', font=('TIME', 11), bg='light gray')
        ngay_nhan_viec.place(x=505, y=3, width= 100)
        entry_ngay_nhan_viec=Entry(frame_2, font=('TIME', 11))
        entry_ngay_nhan_viec.place(x=610, y=3, width= 100)

        chuthich =Label(frame_2, text='dd-mm-yyy', font=('TIME', 11), bg='light gray')
        chuthich.place(x=710, y=3, width= 100)

        #Frame button
        frame_button = Frame(frame_chinhsua, height = 30, width= 900, bg='light yellow')
        frame_button.place(x=0,y=70)

        xoa = Button(frame_button, text="Xóa", font=('TIME', 11), bg='light yellow', command=xoa_nguoi)


        capnhat = Button(frame_button, text="Cập nhật", font=('TIME', 11), bg='light yellow',command=nut_cap_nhat)
        capnhat.place(x=450, y=0, width=450,height=30)


        xoa.place(x=0, y=0, width=450,height=30)
        capnhat.place(x=450, y=0, width=450,height=30)

    def doanh_thu():
        global  val_ngay, val_thang, val_nam, dt
        val_ngay = ""
        val_thang = ""
        val_nam = ""

        cursor.execute("SELECT * FROM doanhthungay")
        dt = cursor.fetchall()

        #Tên tab
        Label_tab.configure(text='DOANH THU')

        #Tắt các frame khác
        frame_sanpham.place_forget()
        frame_giohang.place_forget()
        frame_nhansu.place_forget()
        frame_taikhoan.place_forget()
        frame_khohang.place_forget()

        #Mở frame doanh thu
        frame_doanhthu.place(x=175, y=50)

        frame_ngay = Frame(frame_doanhthu, height=250, width=900, bg='light blue')
        frame_ngay.place(x=50, y=50)
        locale.setlocale(locale.LC_ALL, 'vi_VN.utf8')
        def change(event):
            value= entry3.get()
            """ Xử lý sự kiên thay đổi đầu vào  """
            try:
                # Chuyển đổi giá trị entry sang kiểu số float
                value = int(value.replace('.', ''))
            except ValueError:
                # Nếu giá trị không phải kiểu số
                value = 0

            # Định dạng giá trị theo chuỗi có phân cách hàng chữ số
            formatted_value = locale.format_string("%d",value, grouping=True)


            # # Cập nhật entry với giá trị mới đã định dạng
            entry3.delete(0, END)
            entry3.insert(0, formatted_value)

        def chon_ngay(event):
            global val_ngay
            val_ngay = ngay.get()
            table_doanhthu.delete(*table_doanhthu.get_children())
            if int(val_ngay) < 10:
                val_ngay="0"+val_ngay
            for doanhthu in dt:
                if val_ngay == doanhthu[9] and val_thang == doanhthu[8]:
                    tonghd = '{:,}'.format(doanhthu[3])
                    khachtra = '{:,}'.format(doanhthu[4])
                    table_doanhthu.insert("", "end", values=(doanhthu[0],doanhthu[1], doanhthu[2],tonghd,khachtra,doanhthu[5],doanhthu[6]))
                elif val_ngay == doanhthu[9]:
                    table_doanhthu.insert("", "end", values=doanhthu[0:8])

        def chon_thang(event):
            global val_thang, date
            val_thang = thang.get()
            table_doanhthu.delete(*table_doanhthu.get_children())
            if int(val_thang) < 10:
                val_thang="0"+val_thang
            for doanhthu in dt:
                if val_thang == doanhthu[8]:
                    tonghd = '{:,}'.format(doanhthu[3])
                    khachtra = '{:,}'.format(doanhthu[4])
                    table_doanhthu.insert("", "end", values=(doanhthu[0],doanhthu[1], doanhthu[2],tonghd,khachtra,doanhthu[5],doanhthu[6]))
                elif val_thang == doanhthu[8] and val_ngay == doanhthu[9]:
                    tonghd = '{:,}'.format(doanhthu[3])
                    khachtra = '{:,}'.format(doanhthu[4])
                    table_doanhthu.insert("", "end", values=(doanhthu[0],doanhthu[1], doanhthu[2],tonghd,khachtra,doanhthu[5],doanhthu[6]))

        def on_entry_change(event):
            global val_nam
            val_nam = nam.get()

        def tim_kiem():
            val_ngay = ngay.get()
            val_thang = thang.get()
            val_nam = nam.get()
            mahoadon = entry1.get()
            tonghoadon = entry2.get()
            hoadon = []
            if val_nam=="":
                val_nam="2023"
            if val_ngay.isdigit() and val_thang=="":
                messagebox.showerror("","Vui lòng nhập Tháng!")
            elif val_thang.isdigit() and val_ngay=="":
                messagebox.showerror("","Vui lòng nhập Ngày!")

            if tonghoadon == "":
                tonghoadon = 0
            else:
                tonghoadon = int(tonghoadon)

            if mahoadon=="":
                messagebox.showerror("","Vui lòng nhập Mã hóa đơn!")
            if isinstance(mahoadon,str) and val_ngay.isdigit() and val_thang.isdigit():
                table_doanhthu.delete(*table_doanhthu.get_children())
                for dh in dt:
                    if val_ngay.isdigit() and val_thang.isdigit() and val_nam.isdigit():
                        data_date = date(int(val_nam),int(val_thang),int(val_ngay))
                        if  mahoadon == dh[1] and tonghoadon == dh[3] and data_date==dh[7]:
                            hoadon.append(dh)
                        elif data_date==dh[7] and mahoadon == dh[1] and tonghoadon != dh[3]:
                            hoadon.append(dh)
            elif isinstance(mahoadon,str) and val_ngay=="" and val_thang=="":
                table_doanhthu.delete(*table_doanhthu.get_children())
                print(1)
                for dh in dt:
                    if  mahoadon == dh[1] and tonghoadon == dh[3]:
                        hoadon.append(dh)
                    elif mahoadon == dh[1]:
                        hoadon.append(dh)
            for bill in hoadon:
                table_doanhthu.insert("", "end", values=bill[0:8])

        def select_item(event):
            global giomua, ma_hoa_don, tien2
            try:


                cur_item = table_doanhthu.focus()
                item = table_doanhthu.item(cur_item)
                values = item["values"]
                ma_hoa_don = values[1]
                giomua = values[5]
                tien1 = values[3]
                tien2 = values[4]

                """ Xử lý sự kiên thay đổi đầu vào  """
                try:
                    # Chuyển đổi giá trị entry sang kiểu số float
                    tien1 = int(tien1.replace(',', ''))
                    tien2 = int(tien2.replace(',', ''))
                except ValueError:
                    # Nếu giá trị không phải kiểu số
                    tien1 = 0
                    tien2 = 0

                # Định dạng giá trị theo chuỗi có phân cách hàng chữ số
                formatted_value1 = locale.format_string("%d",tien1, grouping=True)
                formatted_value2 = locale.format_string("%d",tien2, grouping=True)
                entry1.delete(0, END)
                entry1.insert(0, values[1])
                entry2.delete(0, END)
                entry2.insert(0, formatted_value1)
                entry3.delete(0, END)
                entry3.insert(0, formatted_value2)
                entry4.delete(0, END)
                entry4.insert(0, values[6])
            except: pass

        def update():
            mahoadon = entry1.get()
            tienkhach = entry3.get()
            tenkhach = entry4.get()
            if mahoadon == "":
                messagebox.showerror("Cập nhật", "Hãy chọn hóa đơn cần chỉnh sửa!")
            else:
                if tienkhach == tien2 and tenkhach==values[6]:
                    messagebox.showwarning("","Vui lòng nhập thông tin muốn cập nhật!")
                else:
                    tienkhach = int(tienkhach.replace(".",""))
                    sql = "UPDATE doanhthungay SET TenKhach = %s, KhachTra = %s WHERE MaHoaDon = %s AND Gio = %s"
                    val = (tenkhach, tienkhach, mahoadon, giomua)
                    cursor.execute(sql, val)
                    db.commit()
                    messagebox.showinfo("","Đã cập nhật thông tin!")
                    doanh_thu()

        def xoa_don():
            if ma_hoa_don=="":
                messagebox.showerror("","Vui lòng chọn đơn cần xóa trên bảng!")
            else:
                box = messagebox.askokcancel(title="",message="Bạn có chắc chắn xóa hóa đơn với mã ({:s}) ?".format(ma_hoa_don))
                if box:
                    cursor.execute("DELETE FROM doanhthungay WHERE MaHoaDon = %s AND Gio=%s", (ma_hoa_don, giomua))
                    db.commit()
            doanh_thu()
        label_ngay = Label(frame_doanhthu, text="Ngày:", font=('TIME', 11), bg='light grey', anchor='center')
        label_ngay.place(x=500,y=25,width=50)
        ngay = ttk.Combobox(frame_doanhthu, font=('TIME', 11), values=[str(i) for i in range(1, 32)])
        ngay.place(x=550, y= 25, width=100,height=25)
        ngay.bind("<<ComboboxSelected>>", chon_ngay)

        label_thang = Label(frame_doanhthu, text="Tháng:", font=('TIME', 11), bg='light grey', anchor='center')
        label_thang.place(x=650,y=25,width=50)
        thang = ttk.Combobox(frame_doanhthu, font=('TIME', 11), values=[str(i) for i in range(1, 13)])
        thang.place(x=700, y= 25, width=100,height=25)
        thang.bind("<<ComboboxSelected>>", chon_thang)

        label_nam = Label(frame_doanhthu, text="Năm:", font=('TIME', 11), bg='light grey', anchor='center')
        label_nam.place(x=800,y=25,width=50)
        nam = Entry(frame_doanhthu,font=('TIME', 11))
        nam.place(x=850, y= 25, width=100,height=25)
        nam.bind('<KeyRelease>', on_entry_change)


        cursor.execute("SELECT * FROM doanhthungay")
        data1 = cursor.fetchall()
        table_doanhthu = ttk.Treeview(frame_ngay, columns=("STT", "Mã hóa đơn", "Thu ngân","Tổng hóa đơn", "Khách trả","Giờ thanh toán", "Tên khách"), show="headings")
        scrollbar = Scrollbar(table_doanhthu, orient="vertical")
        table_doanhthu.column("STT", width=30,anchor=CENTER)
        table_doanhthu.column("Mã hóa đơn", width=100,anchor=CENTER)
        table_doanhthu.column("Thu ngân", width=75,anchor=CENTER)
        table_doanhthu.column("Tổng hóa đơn", width=100,anchor=CENTER)
        table_doanhthu.column("Khách trả", width=100,anchor=CENTER)
        table_doanhthu.column("Giờ thanh toán", width=120,anchor=CENTER)
        table_doanhthu.column("Tên khách", width=120,anchor=CENTER)

        table_doanhthu.heading("STT", text="STT",anchor=CENTER)
        table_doanhthu.heading("Mã hóa đơn", text="MÃ HÓA ĐƠN",anchor=CENTER)
        table_doanhthu.heading("Thu ngân", text="THU NGÂN",anchor=CENTER)
        table_doanhthu.heading("Tổng hóa đơn", text="TỔNG HÓA ĐƠN",anchor=CENTER)
        table_doanhthu.heading("Khách trả", text="KHÁCH TRẢ",anchor=CENTER)
        table_doanhthu.heading("Giờ thanh toán", text="GIỜ THANH TOÁN",anchor=CENTER)
        table_doanhthu.heading("Tên khách", text="TÊN KHÁCH",anchor=CENTER)

        table_doanhthu.bind("<ButtonRelease-1>", select_item)

        for row in data1:
            gia1 = '{:,}'.format(row[3])
            gia2 = '{:,}'.format(row[4])
            money = (gia1,gia2)
            table_doanhthu.insert("", "end", values=row[0:3]+money+row[5:7])

        scrollbar.config(command=table_doanhthu.yview)
        table_doanhthu.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        table_doanhthu.place(x=0, y=0, width=900, height=150)

        frame_tab_dt = Frame(frame_doanhthu, height = 100, width= 900, bg='light gray')
        frame_tab_dt.place(x=50, y=200)

        #Frame 1
        frame_1 = Frame(frame_tab_dt, height = 70, width= 900, bg='light gray')
        frame_1.place(x=0, y=0)

        Label1 = Label(frame_1,text="Mã hóa đơn:",font=('TIME', 11), bg='light gray', anchor = 'center')
        Label1.place(x=15, y=10, width=100)

        entry1 = Entry(frame_1, text="", font=('TIME', 11))
        entry1.place(x=120, y=10, width=100)

        Label2 = Label(frame_1, text="Tổng hóa đơn:", font=('TIME', 11), bg='light gray', anchor = 'center')
        Label2.place(x=235, y=10, width=100)

        entry2 = Entry(frame_1, text="", font=('TIME', 11))
        entry2.place(x=340, y=10, width=100)

        Label3 = Label(frame_1, text="Tiền khách trả:\n(Có thể\nchỉnh sửa)", font=('TIME', 11), bg='light gray', anchor = 'center')
        Label3.place(x=455, y=10, width=100)

        entry3 = Entry(frame_1, text="", font=('TIME', 11))
        entry3.place(x=560, y=10, width=100)

        Label4 = Label(frame_1, text="Khách hàng:\n(Có thể\nchỉnh sửa)", font=('TIME', 11), bg='light gray', anchor = 'center')
        Label4.place(x=675, y=10, width=100)

        entry4 = Entry(frame_1, text="", font=('TIME', 11))
        entry4.place(x=770, y=10, width=100)
        entry3.bind('<KeyRelease>', change)

        #Frame button
        frame_2 = Frame(frame_tab_dt, height = 30, width= 900, bg='light yellow')
        frame_2.place(x=0, y=70)

        button_xoadon = Button(frame_2, text="Xóa hóa đơn", font=('TIME', 11), bg='light yellow', command=xoa_don)
        button_xoadon.place(x=0, y= 0, height = 30,width=300)
        button_timkiem = Button(frame_2, text="Tìm hóa đơn", font=('TIME', 11), bg='light yellow', command=tim_kiem)
        button_timkiem.place(x=300, y= 0, height = 30,width=300)
        button_capnhat = Button(frame_2, text="Cập nhật thông tin", font=('TIME', 11), bg='light yellow',command=update)
        button_capnhat.place(x=600, y=0, height = 30,width=300)

    def kho_hang():
        global brand, loaisp
        brand=""
        loaisp=""
        #Tên tab
        Label_tab.configure(text='KHO HÀNG')

        #Tắt các tab khác
        frame_sanpham.place_forget()
        frame_giohang.place_forget()
        frame_nhansu.place_forget()
        frame_taikhoan.place_forget()
        frame_doanhthu.place_forget()

        #Mở Frame kho hàng
        frame_khohang.place(x=175, y=50)

        #Label phân biệt bảng
        label_khohang = Label(frame_khohang, text="Kho hàng:", font=('TIME', 11), bg='light blue', anchor='center')
        label_khohang.place(x=100,y=50,width=350)
        label_sanpham = Label(frame_khohang, text="Sản phẩm hiện có:", font=('TIME', 11), bg='light blue', anchor='center')
        label_sanpham.place(x=550,y=50,width=350)

        def select_item_khohang(event):
            try:
                cur_item = table_khohang.focus()
                item = table_khohang.item(cur_item)
                values = item["values"]

                entry_tensanpham.delete(0, END)
                entry_tensanpham.insert(0, values[1])
                entry_masanpham.delete(0, END)
                entry_masanpham.insert(0, values[2])
                combo2.delete(0, END)
                combo2.insert(0, values[3])
                for cot_hang in hang:
                    if values[1] == cot_hang[1] and values[2] == cot_hang[2]:
                        combo1.delete(0, END)
                        combo1.insert(0, cot_hang[4])
            except: pass
        def select_item_sanpham(event):
            global  ma_sp, ten_sp
            try:
                chonsanpham = bang.focus()
                sp = bang.item(chonsanpham)
                sanphamchon = sp["values"]

                ten_sp = sanphamchon[0]
                ma_sp = sanphamchon[1]
            except: pass

        def on_select1(event=None):
            global brand, loaisp
            loaisp = combo1.get()
            brand = combo2.get()
            try:
                table_khohang.delete(*table_khohang.get_children())
                for hangkho in hang:
                    if brand==hangkho[3] and loaisp == hangkho[4]:
                        table_khohang.insert("", "end", values=hangkho[0:5])
                    elif loaisp == hangkho[4] and brand=="":
                        table_khohang.insert("", "end", values=hangkho[0:5])
                    elif loaisp == "" and brand==hangkho[3]:
                        table_khohang.insert("", "end", values=hangkho[0:5])
                    if loaisp=="" and brand=="":
                        table_khohang.insert("", "end", values=hangkho[0:5])

                bang.delete(*bang.get_children())
                for row_sanpham in datasanpham:
                    gia = '{:,}'.format(row_sanpham[4])
                    if brand==row_sanpham[5] and loaisp == row_sanpham[6]:
                        bang.insert("", "end", values=(row_sanpham[1], row_sanpham[2],row_sanpham[3], gia))
                    elif loaisp == row_sanpham[6] and loaisp == "" :
                        bang.insert("", "end", values=(row_sanpham[1], row_sanpham[2],row_sanpham[3], gia))
                    elif loaisp == "" and brand==row_sanpham[5]:
                        bang.insert("", "end", values=(row_sanpham[1], row_sanpham[2],row_sanpham[3], gia))
                    if loaisp == "" and brand=="":
                        bang.insert("", "end", values=(row_sanpham[1], row_sanpham[2],row_sanpham[3], gia))

            except: pass

        def on_select2(event=None):
            global brand, loaisp
            loaisp = combo1.get()
            brand = combo2.get()
            try:
                table_khohang.delete(*table_khohang.get_children())
                for hangkho in hang:
                    if brand==hangkho[3] and loaisp == hangkho[4]:
                        table_khohang.insert("", "end", values=hangkho[0:5])
                    elif brand==hangkho[3] and loaisp=="":
                        table_khohang.insert("", "end", values=hangkho[0:5])
                    elif brand=="" and loaisp==hangkho[4]:
                        table_khohang.insert("", "end", values=hangkho[0:5])
                    if loaisp=="" and brand=="":
                        table_khohang.insert("", "end", values=hangkho[0:5])

                bang.delete(*bang.get_children())
                for row_sanpham in datasanpham:
                    gia = '{:,}'.format(row_sanpham[4])
                    if brand==row_sanpham[5] and loaisp == row_sanpham[6]:
                        bang.insert("", "end", values=(row_sanpham[1], row_sanpham[2],row_sanpham[3], gia))
                    elif brand==row_sanpham[5] and  loaisp=="":
                        bang.insert("", "end", values=(row_sanpham[1], row_sanpham[2],row_sanpham[3], gia))
                    elif brand=="" and loaisp== row_sanpham[6]:
                        bang.insert("", "end", values=(row_sanpham[1], row_sanpham[2],row_sanpham[3], gia))
                    if loaisp=="" and brand=="":
                        bang.insert("", "end", values=(row_sanpham[1], row_sanpham[2],row_sanpham[3], gia))

            except: pass
        #Bảng kho hàng
        cursor.execute("SELECT * FROM khohang")
        hang = cursor.fetchall()
        table_khohang = ttk.Treeview(frame_khohang, columns=("STT", "Tensanpham", "Masanpham", "Thuonghieu","Loai"), show="headings")
        scrollbar_khohang = Scrollbar(table_khohang, orient="vertical")
        table_khohang.column("STT", anchor=CENTER, width=30)
        table_khohang.column("Tensanpham", anchor=CENTER, width=100)
        table_khohang.column("Masanpham", anchor=CENTER, width=100)
        table_khohang.column("Thuonghieu", anchor=CENTER, width=90)
        table_khohang.column("Loai", anchor=CENTER, width=90)

        table_khohang.heading("STT", text="STT", anchor=CENTER)
        table_khohang.heading("Tensanpham", text="TÊN SẢN PHẨM", anchor=CENTER)
        table_khohang.heading("Masanpham", text="MÃ SẢN PHẨM", anchor=CENTER)
        table_khohang.heading("Thuonghieu", text="HÃNG", anchor=CENTER)
        table_khohang.heading("Loai", text="Loại", anchor=CENTER)

        table_khohang.bind("<ButtonRelease-1>", select_item_khohang)
        for cot_hang in hang:
            table_khohang.insert("", "end", values=cot_hang[0:5])

        scrollbar_khohang.config(command=table_khohang.yview)
        table_khohang.configure(yscrollcommand=scrollbar_khohang.set)

        scrollbar_khohang.pack(side="right", fill="y")
        table_khohang.place(x=50, y=75, width=450, height=125)

        #Bảng sản phẩm
        cursor.execute("SELECT * FROM sanpham")
        datasanpham = cursor.fetchall()
        bang = ttk.Treeview(frame_khohang, columns=("Tensanpham", "Masanpham", "Soluong","Gia"), show="headings")
        scrollbar_sanpham = Scrollbar(bang, orient="vertical")

        bang.column("Tensanpham", anchor=CENTER, width=90)
        bang.column("Masanpham", anchor=CENTER, width=95)
        bang.column("Soluong", anchor=CENTER, width=60)
        bang.column("Gia", anchor=CENTER, width=50)


        bang.heading("Tensanpham", text="TÊN SẢN PHẨM", anchor=CENTER)
        bang.heading("Masanpham", text="MÃ SẢN PHẨM", anchor=CENTER)
        bang.heading("Soluong", text="SỐ LƯỢNG", anchor=CENTER)
        bang.heading("Gia", text="GIÁ", anchor=CENTER)

        bang.bind("<ButtonRelease-1>", select_item_sanpham)
        for row_sanpham in datasanpham:
            gia = '{:,}'.format(row_sanpham[4])
            bang.insert("", "end", values=(row_sanpham[1], row_sanpham[2],row_sanpham[3], gia))

        scrollbar_sanpham.config(command=bang.yview)
        bang.configure(yscrollcommand=scrollbar_sanpham.set)

        scrollbar_sanpham.pack(side="right", fill="y")
        bang.place(x=500, y=75, width=450, height=125)


        def tim_kiem():
            global tensp, masp
            tensp = entry_tensanpham.get()
            masp = entry_masanpham.get()
            loaisp = combo1.get()
            brand = combo2.get()
            results = []
            results_sp = []
            table_khohang.delete(*table_khohang.get_children())
            bang.delete(*bang.get_children())
            if tensp == "" and masp == "" and loaisp=="" and brand=="":
                messagebox.showerror("Tìm kiếm","Mời bạn nhập thông tin tìm kiếm!")
                for row1 in hang:
                    table_khohang.insert("", "end", values=row1[0:4])
                for row2 in datasanpham:
                    bang.insert("", "end", values=row2[1:5])
            else:
                #Kho hàng
                for rowkh in hang:
                    if (tensp == rowkh[1] and masp == rowkh[2] and brand == rowkh[3] and loaisp == rowkh[4]) :
                        results.append(rowkh)
                    elif (tensp == rowkh[1] and masp == "" and loaisp == "" and brand == "") or (tensp == "" and masp == rowkh[2] and loaisp == "" and brand == ""):
                        results.append(rowkh)
                    elif (tensp == "" and masp == ""  and brand == rowkh[3] and loaisp == "") or (tensp == "" and masp == "" and loaisp == rowkh[4] and brand == ""):
                        results.append(rowkh)
                    elif (tensp == rowkh[1] and masp == rowkh[2] and brand == rowkh[3]) or (tensp == rowkh[1] and masp == rowkh[2] and loaisp == rowkh[4]):
                        results.append(rowkh)
                    elif (brand == rowkh[3] and loaisp == rowkh[4] and tensp == rowkh[1]) or (brand == rowkh[3] and loaisp == rowkh[4] and masp == rowkh[2]):
                        results.append(rowkh)
                    elif (tensp == rowkh[1] and masp == rowkh[2]):
                        results.append(rowkh)
                    elif (tensp == rowkh[1] and brand == rowkh[3]):
                        results.append(rowkh)
                    elif (tensp == rowkh[1] and loaisp == rowkh[4]):
                        results.append(rowkh)
                    elif (masp == rowkh[2] and brand == rowkh[3]):
                        results.append(rowkh)
                    elif (masp == rowkh[2] and loaisp == rowkh[4]):
                        results.append(rowkh)
                    elif (brand == rowkh[3] and loaisp == rowkh[4]):
                        results.append(rowkh)
                    elif (tensp == rowkh[1] and brand == "" and loaisp == ""):
                        results.append(rowkh)
                    elif (masp == rowkh[2] and brand == "" and loaisp == ""):
                        results.append(rowkh)
                #Sản phẩm
                for row_sp in datasanpham:
                    if (tensp == row_sp[0] and masp == row_sp[1]):
                        results_sp.append(row_sp)
                    elif (tensp == row_sp[0] and masp == "") or (tensp == "" and masp == row_sp[1]):
                        results_sp.append(row_sp)

            for result in results:
                table_khohang.insert("", "end", values=result[0:5])

            for sp in results_sp:
                bang.insert("", "end", values=(sp[1],sp[2],sp[3],sp[4]))
            print(results)

        def lam_moi():
            kho_hang()
            entry_tensanpham.delete(0, END)
            entry_masanpham.delete(0, END)
            entry_soluong.delete(0, END)

        def nhap_kho():
            tensp = entry_tensanpham.get()
            masp = entry_masanpham.get()
            so_luong = entry_soluong.get()
            if (masp=="" and tensp=="" and so_luong==""):
                messagebox.showerror("","Hãy nhập tên, mã và số lượng sản phẩm!")
            elif (tensp=="" and so_luong==""):
                messagebox.showerror("","Hãy nhập tên và số lượng sản phẩm!")
            elif (masp=="" and so_luong==""):
                messagebox.showerror("","Hãy nhập mã và số lượng sản phẩm!")
            elif (masp=="" and tensp=="") or (masp=="" and isinstance(tensp,str)) or (isinstance(masp,str) and tensp==""):
                messagebox.showerror("","Hãy nhập tên và mã sản phẩm!")
            elif (so_luong=="") :
                messagebox.showerror("","Hãy nhập số lượng sản phẩm!")
            elif so_luong.isdigit():
                cursor.execute("SELECT * FROM khohang WHERE Tensanpham=%s AND Masanpham=%s", (tensp, masp))
                checkkhohang = cursor.fetchone()
                cursor.execute("SELECT * FROM sanpham WHERE Tensanpham=%s AND Masanpham=%s", (tensp, masp))
                check = cursor.fetchone()
                so_luong = int(so_luong)
                if checkkhohang:
                    if check:
                        if so_luong > 0:
                            box = messagebox.askokcancel(title="",message="Bạn có chắc chắn nhập kho ({:s}) với số lượng là {:d}".format(tensp, so_luong))
                            if box:
                                if (tensp == check[1] and masp == check[2]):
                                    so_luong = int(so_luong) + int(check[3])
                                a = "UPDATE sanpham SET Soluong = %s WHERE Tensanpham = %s AND Masanpham = %s"
                                b = (so_luong, tensp, masp)
                                cursor.execute(a, b)
                                db.commit()
                                lam_moi()
                            else:
                                kho_hang()
                        else:
                            messagebox.showerror("","Hãy nhập số lượng sản phẩm!")
                    else:
                        def dinh_gia():
                            loaisp = combo1.get()
                            brand = combo2.get()
                            don_gia = entry_dinhgia.get()
                            if don_gia[0:2].isdigit:
                                don_gia = int(don_gia.replace('.', ''))
                                sql = "INSERT INTO sanpham (Tensanpham, Masanpham, Soluong, Dongia, Thuonghieu, Loai) VALUES (%s, %s, %s, %s, %s, %s)"
                                val = (tensp, masp, so_luong, don_gia,brand,loaisp)
                                cursor.execute(sql, val)
                                db.commit()
                                tab_dinhgia.destroy()
                            elif don_gia.isalpha() or don_gia=="" :
                                messagebox.showerror("","Định giá không hợp lệ!")
                                breakpoint()
                            lam_moi()
                        def on_entry_change(event):
                            value= entry_dinhgia.get()
                            """ Xử lý sự kiên thay đổi đầu vào  """
                            try:
                                # Chuyển đổi giá trị entry sang kiểu số float
                                value = int(value.replace('.', ''))
                            except ValueError:
                                # Nếu giá trị không phải kiểu số
                                value = 0

                            # Định dạng giá trị theo chuỗi có phân cách hàng chữ số
                            formatted_value = locale.format_string("%d",value, grouping=True)


                            # # Cập nhật entry với giá trị mới đã định dạng
                            entry_dinhgia.delete(0, END)
                            entry_dinhgia.insert(0, formatted_value)


                        tab_dinhgia = Toplevel(frame_khohang)
                        tab_dinhgia.title("Định giá sản phẩm")
                        tab_dinhgia.geometry('%dx%d+%d+%d' % (600, 150, (width/2 - 600/2), (height/2 - 100)))
                        tab_dinhgia.configure(bg='light blue')

                        lb = Frame(tab_dinhgia, bg="light blue")
                        lb.place(x=100,y=25,width=400,height=100)

                        dinhgia = Label(lb, text="Đặt đơn giá cho\n{:s}".format(tensp), font=('TIME', 11), bg='light blue', anchor='center')
                        dinhgia.place(x=0, y=0, width=400)

                        entry_dinhgia = Entry(lb, font=('TIME', 11))
                        entry_dinhgia.place(x=125, y=55, width=150)
                        entry_dinhgia.bind('<KeyRelease>', on_entry_change)

                        ok = Button(lb, text="OK", font=('TIME', 11), bg='light yellow', anchor='center', command=dinh_gia)
                        ok.place(x=150, y=80, width=100)
                else:
                    messagebox.showerror("","Mặt hàng này không có trong kho!")
            elif so_luong.isalpha:
                 messagebox.showerror("","Số lượng là chữ số!")

        def xoa_hang():
            try:
                box = messagebox.askokcancel(title="",message="Bạn có chắc chắn xóa mặt hàng ({:s}) với mã ({:s})".format(ten_sp, ma_sp))
                if box:
                    cursor.execute("DELETE FROM sanpham WHERE Tensanpham=%s AND Masanpham=%s", (ten_sp, ma_sp))
                    db.commit()
                    messagebox.showinfo("","Bạn đã xóa mặt hàng ({:s}) với mã ({:s})".format(ten_sp, ma_sp))
                    lam_moi()
                else:
                    breakpoint
            except: messagebox.showinfo("","Không có sản phẩm để xóa!")
        locale.setlocale(locale.LC_ALL, 'vi_VN.utf8')

        #Frame chọn bill
        frame_nhaphang = Frame(frame_khohang, height = 100, width= 900, bg='light gray')
        frame_nhaphang.place(x=50, y=200)

        loai = Label(frame_nhaphang, text="Loại sản phẩm:", font=('TIME', 11), bg='light gray', anchor='w')
        loai.place(x=10, y=10, width=100)

        combo1 = ttk.Combobox(frame_nhaphang, values=["",'Bàn phím','Chuột','Tai nghe','Ghế Gaming'])
        combo1.place(x=115, y= 10, width=100)

        combo1.bind("<<ComboboxSelected>>", on_select1)

        tensanpham = Label(frame_nhaphang, text="Tên sản phẩm:", font=('TIME', 11), bg='light gray', anchor='w')
        tensanpham.place(x=220, y=10, width=100)

        entry_tensanpham = Entry(frame_nhaphang, font=('TIME', 11))
        entry_tensanpham.place(x=325, y=10, width=300)

        masanpham = Label(frame_nhaphang, text="Mã sản phẩm:", font=('TIME', 11), bg='light gray', anchor='w')
        masanpham.place(x=220, y=40, width=100)

        entry_masanpham = Entry(frame_nhaphang, font=('TIME', 11))
        entry_masanpham.place(x=325, y=40, width=100)

        thuonghieu = Label(frame_nhaphang, text="Hãng:", font=('TIME', 11), bg='light gray', anchor='w')
        thuonghieu.place(x=10, y=40, width=100)

        combo2 = ttk.Combobox(frame_nhaphang, values=["",'Logitech','Razer','Asus','Fuhlen','Dare-U'])
        combo2.place(x=115, y= 40, width=100)

        combo2.bind("<<ComboboxSelected>>", on_select2)

        soluong = Label(frame_nhaphang, text="Số lượng nhập kho:", font=('TIME', 11), bg='light gray', anchor='w')
        soluong.place(x=640, y=10, width=150)

        entry_soluong = Entry(frame_nhaphang, font=('TIME', 11))
        entry_soluong.place(x=785, y=10, width=100)

        timkiem = Button(frame_nhaphang, text="Tìm kiếm", font=('TIME', 11), bg='light yellow', command=tim_kiem)
        timkiem.place(x=0, y=70, width=225,height=30)

        lammoi = Button(frame_nhaphang, text="Làm mới", font=('TIME', 11), bg='light yellow', command=lam_moi)
        lammoi.place(x=225, y=70, width=225,height=30)

        nhapkho = Button(frame_nhaphang, text="Nhập kho", font=('TIME', 11), bg='light yellow', command=nhap_kho)
        nhapkho.place(x=450, y=70, width=225,height=30)

        xoahang = Button(frame_nhaphang, text="Xóa mặt hàng", font=('TIME', 11), bg='light yellow', command=xoa_hang)
        xoahang.place(x=675, y=70, width=225,height=30)

    def tai_khoan():
        def hienthongtin():
            cursor.execute("SELECT * FROM taikhoan WHERE Username=%s", (username,))
            info = cursor.fetchone()

            entry_hovaten.delete(0, END)
            entry_hovaten.insert(0, info[1])

            entry_tendangnhap.delete(0, END)
            entry_tendangnhap.insert(0, info[8])

            entry_matkhau.delete(0, END)
            entry_matkhau.insert(0, info[11])

            ngaynhanviec = info[12].strftime('%d-%m-%Y')
            entry_sdt.delete(0, END)
            entry_sdt.insert(0, info[9])

            entry_chuc_vu.delete(0, END)
            entry_chuc_vu.insert(0, info[10])

            entry_ngaynhanviec.delete(0, END)
            entry_ngaynhanviec.insert(0, ngaynhanviec)
            try:
                entry_gioitinh.delete(0, END)
                entry_gioitinh.insert(0, info[2])

                entry_dantoc.delete(0, END)
                entry_dantoc.insert(0, info[3])

                day_entry.delete(0, END)
                day_entry.insert(0, info[4])

                month_entry.delete(0, END)
                month_entry.insert(0, info[5])

                year_entry.delete(0, END)
                year_entry.insert(0, info[6])

                entry_tongiao.delete(0, END)
                entry_tongiao.insert(0, info[7])
            except: pass

        def cap_nhat():
            from datetime import datetime
            try:
                ok=0
                id = data[0]
                ten = entry_hovaten.get()
                gioitinh = entry_gioitinh.get()
                dantoc = entry_dantoc.get()
                ngay = day_entry.get()
                thang = month_entry.get()
                nam = year_entry.get()
                tongiao = entry_tongiao.get()
                tendangnhap = entry_tendangnhap.get()
                sdt = entry_sdt.get()
                chucvu = entry_chuc_vu.get()
                matkhau = entry_matkhau.get()
                ngaynhanviec = entry_ngaynhanviec.get()
                for i in ngaynhanviec:
                    if i == "-":
                        ok +=1
                if ok == 2 and len(ngaynhanviec)==10:
                    if ngaynhanviec[2] != "-" and ngaynhanviec[5] != "-":
                        messagebox.showerror("","Ngày nhận việc không nhập đúng cú pháp!")
                    else:
                        ngaynhanviec = datetime.strptime(ngaynhanviec, '%d-%m-%Y').date()
                        a = "UPDATE taikhoan SET Fullname = %s, Gioitinh = %s, Dantoc = %s, Ngay = %s, Thang = %s, Nam = %s, Tongiao = %s, SDT = %s, Chucvu=%s, Password = %s, Ngaynhanviec = %s WHERE ID = %s AND Username = %s"
                        b = (ten, gioitinh, dantoc, ngay, thang, nam, tongiao, sdt, chucvu, matkhau, ngaynhanviec, id , tendangnhap)
                        cursor.execute(a,b)
                        db.commit()
                else:
                    messagebox.showerror("","Ngày nhận việc không nhập đúng cú pháp!")
                tai_khoan()
            except: pass

        #Tên tab
        Label_tab.configure(text='TÀI KHOẢN')

        #Tắt các tab khác
        frame_sanpham.place_forget()
        frame_giohang.place_forget()
        frame_nhansu.place_forget()
        frame_khohang.place_forget()
        frame_doanhthu.place_forget()

        #Mở Frame
        frame_taikhoan.place(x=175, y=50)

        #Frame dữ liệu tài khoản
        frame_info = Frame(frame_taikhoan, width= 800, height = 250,  bg='light grey')
        frame_info.place(x=100, y=50)

        #Label #Entry
        canhan = Label(frame_info, text="Thông tin cá nhân:", font=('TIME', 13,"bold"), bg='light grey', anchor='w')
        canhan.place(x=40, y=5, width=160)

        hovaten = Label(frame_info, text="Họ và tên:", font=('TIME', 14), bg='light grey', anchor='w')
        hovaten.place(x=40, y=40, width=95)
        entry_hovaten = Entry(frame_info, font=('TIME', 14))
        entry_hovaten.place(x=140,y=40,width=215)

        gioitinh = Label(frame_info, text="Giới tính:", font=('TIME', 14), bg='light grey', anchor='w')
        gioitinh.place(x=390, y=40, width=80)
        entry_gioitinh = Entry(frame_info, font=('TIME', 14))
        entry_gioitinh.place(x=485,y=40,width=60)

        dantoc = Label(frame_info, text="Dân tộc:", font=('TIME', 14), bg='light grey', anchor='w')
        dantoc.place(x=565, y=40, width=70)
        entry_dantoc = Entry(frame_info, font=('TIME', 14))
        entry_dantoc.place(x=645,y=40,width=100)

        dob = Label(frame_info, text="Ngày sinh:", font=('TIME', 14), bg='light grey', anchor='w')
        dob.place(x=40, y=75, width=100)

        frame_dob = Frame(frame_info, width=150, height=25, bg="light grey")
        frame_dob.place(x=140, y=75)

        day_entry = Entry(frame_dob,font=('TIME', 14))
        day_entry.place(x=0,y=0,width=50)
        month_entry = Entry(frame_dob,font=('TIME', 14))
        month_entry.place(x=50,y=0,width=50)
        year_entry = Entry(frame_dob,font=('TIME', 14))
        year_entry.place(x=100,y=0,width=50)

        tongiao = Label(frame_info, text="Tôn giáo:", font=('TIME', 14), bg='light grey', anchor='w')
        tongiao.place(x=390, y=75, width=100)
        entry_tongiao = Entry(frame_info, font=('TIME', 14))
        entry_tongiao.place(x=485,y=75,width=100)

        ######
        account = Label(frame_info, text="Thông tin tài khoản:", font=('TIME', 13,"bold"), bg='light grey', anchor='w')
        account.place(x=40, y=115, width=160)

        tendangnhap = Label(frame_info, text="Tên đăng nhập:", font=('TIME', 14), bg='light grey', anchor='w')
        tendangnhap.place(x=40, y=150, width=140)
        entry_tendangnhap = Entry(frame_info, font=('TIME', 14))
        entry_tendangnhap.place(x=180,y=150,width=100)

        sdt = Label(frame_info, text="Số điện thoại:", font=('TIME', 14), bg='light grey', anchor='w')
        sdt.place(x=300, y=150,width=120)
        entry_sdt = Entry(frame_info, font=('TIME', 14))
        entry_sdt.place(x=425,y=150,width=120)

        chuc_vu = Label(frame_info, text="Chức vụ:", font=('TIME', 14), bg='light grey', anchor='w')
        chuc_vu.place(x=560, y=150,width=80)
        entry_chuc_vu = Entry(frame_info, font=('TIME', 14))
        entry_chuc_vu.place(x=645,y=150,width=100)

        matkhau = Label(frame_info, text="Mật khẩu:", font=('TIME', 14), bg='light grey', anchor='w')
        matkhau.place(x=40, y=185, width=100)
        entry_matkhau = Entry(frame_info, font=('TIME', 14))
        entry_matkhau.place(x=180,y=185,width=100)

        ngaynhanviec = Label(frame_info, text="Ngày nhận việc:", font=('TIME', 14), bg='light grey', anchor='w')
        ngaynhanviec.place(x=300, y=185, width=135)
        entry_ngaynhanviec = Entry(frame_info, font=('TIME', 14))
        entry_ngaynhanviec.place(x=440,y=185,width=115)

        ngaynhanviec = Label(frame_info, text="dd-mm-yyyy", font=('TIME', 11), bg='light grey', anchor='w')
        ngaynhanviec.place(x=450, y=210, width=135)

        #Button
        capnhat = Button(frame_info, text="Cập nhật", font=('TIME', 14), bg='light yellow', command=cap_nhat)
        capnhat.place(x=700, y=220, width=100, height=30)
        lammoi = Button(frame_info, text="Làm mới", font=('TIME', 14), bg='light yellow', command=tai_khoan)
        lammoi.place(x=600, y=220, width=100, height=30)
        hienthongtin()
    main = Tk()
    main.title('QUẢN LÍ CỬA HÀNG')
    main.geometry('%dx%d+%d+%d' % (1175, 400, (width/2 - 1175/2), (height/2 - 300)))
    main.configure(bg = 'light blue')

    cursor.execute("SELECT * FROM taikhoan WHERE Username=%s", (username,))
    data = cursor.fetchone()
    #Frame chucvu
    frame_ten = Frame(main, height = 50, width= 175, bg='pink')
    frame_ten.place(x=0, y=0)
    #Frame chứa Label, logo
    frame_chucvu = Frame(main, height = 50, width= 1000, bg='pink')
    frame_chucvu.place(x=175, y=0)

    user = Label(frame_ten, text = 'Người đăng nhập:', font=('TIME', 10, 'bold'), bg='pink', anchor="center")
    user.place(x=175/2-63, y=3)

    Ten = Label(frame_ten, text = data[1], font=('TIME', 10), bg='pink', anchor="center")
    Ten.place(x=175/2-63, y=24)

    role = Label(frame_chucvu, text = 'Chức vụ:', font=('TIME', 10, 'bold'), bg='pink',anchor="center")
    role.place(x=(1000/2-175/2), y=3, width=175)

    chucvu = Label(frame_chucvu, text = data[10], font=('TIME', 10), bg='pink', anchor="center")
    chucvu.place(x=(1000/2-175/2), y=24, width=175)

    #Frame chứa giao diện từng tab
    frame_sanpham = Frame(main, height=350, width=1000, bg='light blue')
    frame_giohang = Frame(main, height=350, width=1000, bg='light blue')
    frame_nhansu = Frame(main, height=350, width=1000, bg='light blue')
    frame_doanhthu = Frame(main, height=350, width=1000, bg='light blue')
    frame_khohang = Frame(main, height=350, width=1000, bg='light blue')
    frame_taikhoan = Frame(main, height=350, width=1000, bg='light blue')

    Label_tab = Label(main, text="", font=('TIME', 14), bg = 'light blue',anchor = 'w')
    Label_tab.place(x=190, y=60, width=120)

    #Logo
    logo=Label(frame_chucvu,text='' ,font=('TIME', 14), bg="pink")
    logo.place(x=950, y=0)
    hienlogo()

    #Button
    sanpham = Button(main,text="SẢN PHẨM", font=('TIME', 14), bg='yellow', command=san_pham)
    sanpham.place(x=0, y=50, height=50, width=175)

    giohang = Button(main,text="GIỎ HÀNG", font=('TIME', 14), bg='yellow', command=gio_hang)
    giohang.place(x=0, y=100, height=50, width=175)

    nhansu = Button(main,text="NHÂN SỰ", font=('TIME', 14), bg='yellow',command=nhan_su)
    nhansu.place(x=0, y=150, height=50, width=175)

    doanhthu = Button(main,text="DOANH THU", font=('TIME', 14), bg='yellow',command=doanh_thu)
    doanhthu.place(x=0, y=200, height=50, width=175)

    khohang = Button(main,text="KHO HÀNG", font=('TIME', 14), bg='yellow', command=kho_hang)
    khohang.place(x=0, y=250, height=50, width=175)

    taikhoan = Button(main,text="TÀI KHOẢN", font=('TIME', 14), bg='yellow', command=tai_khoan)
    taikhoan.place(x=0, y=300, height=50, width=175)

    thoat = Button(main,text="ĐĂNG XUẤT", font=('TIME', 14), command=back_to_login, bg='yellow')
    thoat.place(x=0, y=350, height=50, width=175)
    san_pham()

def sign_up_window():
    def sign_up():
        fullname = entry_fullname.get()
        username = entry_username.get()
        password = entry_password.get()
        repassword = entry_repassword.get()
        sdt = entry_sdt.get()
        chucvu = entry_chucvu.get()
        cursor.execute("SELECT * FROM taikhoan WHERE Username=%s", (username,))
        user= cursor.fetchone()
        if fullname=="" or username=="" or password=="" or repassword =="":
            messagebox.showerror("Đăng ký", "Thông tin bắt buộc chưa được nhập!")
        elif repassword != password:
            messagebox.showerror("Đăng ký", "Mật khẩu nhập lại chưa đúng!")
        elif user:
            messagebox.showerror("Đăng ký", "Tên đăng nhập tồn tại!")
        else:
            sql = "INSERT INTO taikhoan (Fullname, Username, Password, SDT, Chucvu, Ngaynhanviec) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (fullname, username, password, sdt, chucvu, formatted_date)
            cursor.execute(sql, val)
            db.commit()

            messagebox.showinfo("Đăng ký", "Đăng ký tài khoản thành công!")

            entry_fullname.delete(0, END)
            entry_username.delete(0, END)
            entry_password.delete(0, END)
            entry_repassword.delete(0, END)
            entry_sdt.delete(0, END)
            entry_chucvu.delete(0, END)

    def back():
        cuasodangky.destroy()

    cuasodangky = Toplevel()
    cuasodangky.title("Đăng ký tài khoản")
    cuasodangky.geometry('450x450')
    cuasodangky.configure(bg='light blue')

    labelfullname = Label(cuasodangky,text="Họ và tên", font=('TIME', 14), bg = 'light pink', width= 20)
    labelfullname.pack()

    entry_fullname = Entry(cuasodangky,font=('TIME', 14), width=20)
    entry_fullname.pack()

    label_username = Label(cuasodangky,text="Tên đăng nhập", font=('TIME', 14), bg = 'light pink', width= 20)
    label_username.pack()

    entry_username = Entry(cuasodangky, font=('TIME', 14), width=20)
    entry_username.pack()

    label_password = Label(cuasodangky, text="Mật khẩu", font=('TIME', 14), bg = 'light pink', width= 20)
    label_password.pack()

    entry_password = Entry(cuasodangky, font=('TIME', 14), width=20)
    entry_password.pack()

    label_repassword = Label(cuasodangky, text="Nhập lại mật khẩu", font=('TIME', 14), bg = 'light pink', width= 20)
    label_repassword.pack()

    entry_repassword = Entry(cuasodangky, font=('TIME', 14), width=20)
    entry_repassword.pack()

    label_sdt = Label(cuasodangky, text="Số điện thoại\n(bắt buộc)", font=('TIME', 14), bg = 'light pink', width= 20)
    label_sdt.pack()

    entry_sdt = Entry(cuasodangky, font=('TIME', 14), width=20)
    entry_sdt.pack()

    label_chucvu = Label(cuasodangky, text="Vị trí làm việc", font=('TIME', 14), bg = 'light pink', width= 20)
    label_chucvu.pack()
    entry_chucvu = ttk.Combobox(cuasodangky, font=('TIME', 14), values=['Quản lí','Nhân viên'], width=19)
    entry_chucvu.pack()

    dangky = Button(cuasodangky,text="Đăng ký", font=('TIME', 14), width= 10,bg = 'Gray', command=sign_up)
    dangky.pack()

    quaylai = Button(cuasodangky,text="Back", font=('TIME', 14), width= 10,bg = 'Gray', command=back)
    quaylai.pack()

def dang_nhap():
    def check_login():
        global username
        global password
        username = entry_username.get()
        password = entry_password.get()
        # username = "khoa"
        # password = "1"
        cursor.execute("SELECT * FROM taikhoan WHERE Username=%s AND Password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Đăng nhập", "Đăng nhập thành công!")
            login_window.destroy()
            main_window()
        else:
            messagebox.showerror("Đăng nhập", "Tên đăng nhập hoặc mật khẩu không đúng!")

    def on_closing():
        if messagebox.askokcancel("Đóng", "Bạn có muốn thoát khỏi chương trình?"):
            login_window.destroy()

    def enter(event):
        # Lấy thông tin đăng nhập từ entry
        # username = entry_username.get()
        # password = entry_password.get()
        username = "khoa"
        password = "1"
        cursor.execute("SELECT * FROM taikhoan WHERE Username=%s AND Password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Đăng nhập", "Đăng nhập thành công!")
            login_window.destroy()
            main_window()
        else:
            messagebox.showerror("Đăng nhập", "Tên đăng nhập hoặc mật khẩu không đúng!")
            login_window.destroy()

    #Cửa sổ đăng nhập
    global width
    global height
    login_window = Tk()
    login_window.title("Đăng nhập")
    width = login_window.winfo_screenwidth()
    height = login_window.winfo_screenheight()
    login_window.geometry('%dx%d+%d+%d' % (450, 200, (width/2 - 450/2), (height/2 - 150)))
    login_window.configure(bg='light blue')

    # Tạo label "Tên đăng nhập"
    empty = Label(bg = 'light blue')
    empty.grid(row=0, column=0, columnspan=2)
    labeldangnhap = Label(text="Tên đăng nhập", font=('TIME', 14), bg = 'light pink', width= 20)
    labeldangnhap.grid(row=1, column=0, columnspan=2)

    # Tạo entry để nhập tên đăng nhập
    entry_username = Entry(font=('TIME', 14), width=20)
    entry_username.grid(row=2, column=0, columnspan=2)

    # Tạo label "Mật khẩu"
    labelmatkhau = Label(text="Mật khẩu", font=('TIME', 14), bg = 'light pink', width= 20)
    labelmatkhau.grid(row=3, column=0, columnspan=2)

    # Tạo entry để nhập mật khẩu
    entry_password = Entry(font=('TIME', 14), show="*", width=20)
    entry_password.bind('<Return>', enter)
    entry_password.grid(row=4, column=0, columnspan=2)

    dangnhap = Button(text="Đăng nhập", font=('TIME', 14), width= 20,bg='yellow', command=check_login)
    dangnhap.grid(row=5, column=0, columnspan=2)

    text = Label(text="Nếu chưa có tài khoản thì bấm vào: ", font=('TIME', 14), bg = 'light blue', width= 30)
    text.grid(row=6, column=0)
    dangky = Button(text="Đăng ký", font=('TIME', 14), width= 10, fg = 'blue',bg = 'light blue', highlightthickness=0, bd=0, activebackground="light blue", activeforeground="red", command=sign_up_window)
    dangky.grid(row=6, column=1)

    login_window.protocol("WM_DELETE_WINDOW", on_closing) # Đăng ký xử lý sự kiện khi đóng cửa sổ
    mainloop()
dang_nhap()
# # %%