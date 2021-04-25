from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
import socket
import hashlib
def main():
    filepath = ""
    def selectExcelfile():
        global  filepath
        sfname = filedialog.askopenfilename()
        filepath=sfname
        text1.insert(INSERT, sfname)

    def closeThisWindow():
        root.destroy()

    def begin_serve():
        # 创建套接字 socket
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2. 绑定本地信息 bind
        tcp_server_socket.bind(("10.0.0.2", 7890))

        # 3. 将手机设置为正常的 响铃模式(让默认的套接字由主动变为被动 listen)
        tcp_server_socket.listen(128)

        print("-----1----")
        # 4. 等待客户端的链接 accept
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("-----2----")

        print(client_addr)

        # 接收客户端发送过来的请求
        recv_data = new_client_socket.recv(1024)
        print(recv_data)
        scr.insert(INSERT,str(recv_data)+'\n')
        # 回送一部分数据给客户端
        new_client_socket.send("hahahghai-----ok-----".encode("utf-8"))

        # 关闭套接字
        new_client_socket.close()
        tcp_server_socket.close()


    def stop_serve():
        print("ffff")

    def cal_md5():
        global filepath
        print(filepath)
        with open(filepath, 'rb') as fp:
            data = fp.read()
        file_md5 = hashlib.md5(data).hexdigest()
        text2.insert(0, file_md5)
        scr.insert(INSERT, "MD5 of "+filepath+" is "+file_md5 + '\n')

    # 初始化
    root = Tk()
    # 设置窗体标题
    root.title('Python GUI Learning')

    # 设置窗口大小和位置
    root.geometry('500x300+570+200')

    label1 = Label(root, text='请选择文件:')
    label2=Label(root,text='MD5:')

    text1 = Entry(root, bg='white', width=45)
    text2 = Entry(root, bg='white', width=45)

    button1 = Button(root, text='浏览', width=8, command=selectExcelfile)
    button2 = Button(root, text='打开服务', width=8, command=begin_serve)
    button3 = Button(root, text='退出', width=8, command=closeThisWindow)
    button4 = Button(root, text='计算', width=8, command=cal_md5)
    scr = scrolledtext.ScrolledText(root, width=62, height=8,font=("隶书",10))  #滚动文本框（宽，高（这里的高应该是以行数为单位），字体样式）


    label1.pack()
    text1.pack()
    label2.pack()
    text2.pack()

    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    scr.pack()

    label1.place(x=30, y=30)
    text1.place(x=100, y=30)
    label2.place(x=30, y=70)
    text2.place(x=100, y=70)

    button1.place(x=425, y=26)
    button2.place(x=140, y=120)
    button3.place(x=340, y=120)
    button4.place(x=425,y=65)
    scr.place(x=30,y=170)

    root.mainloop()


if __name__ == "__main__":
    main()

