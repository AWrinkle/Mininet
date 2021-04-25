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

    #tcp
    def doSend():
        try:
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 2. 连接服务器
            server_ip = text3.get()
            server_port = int(text4.get())
            server_addr = (server_ip, server_port)
            # 192.168.248.1
            tcp_socket.connect(server_addr)
            scr.insert(INSERT, "Connect succeed" + '\n')
            # 3. 发送数据/接收数据
            send_data = text2.get()
            tcp_socket.send(send_data.encode("utf-8"))
            # 4. 关闭套接字
            tcp_socket.close()
        except:
            scr.insert(INSERT, "Connect fail" + '\n')
        '''
        if tcp_socket.connect(server_addr) != socket.error:
            scr.insert(INSERT, "Connect succeed" + '\n')
            # 3. 发送数据/接收数据
            send_data = input("请输入要发送的数据:")
            tcp_socket.send(send_data.encode("utf-8"))
            # 4. 关闭套接字
            tcp_socket.close()
        else:
            scr.insert(INSERT, "Connect fail" + '\n')
        '''

    def cal_md5():
        filepath=text1.get()
        try:
            with open(filepath, 'rb') as fp:
                data = fp.read()
            file_md5 = hashlib.md5(data).hexdigest()
            text2.delete(0, END)
            text2.insert(0, file_md5)
            scr.insert(INSERT, "MD5 of "+filepath+" is "+file_md5 + '\n')
        except:
            text2.delete(0, END)
            scr.insert(INSERT, "Invalid filename" + '\n')
    # 初始化
    root = Tk()
    # 设置窗体标题
    root.title('Python GUI Learning')

    # 设置窗口大小和位置
    root.geometry('500x300+570+200')

    label1 = Label(root, text='请选择文件:')
    label2=Label(root,text='MD5:')
    label3 = Label(root, text='dst_ip:')
    label4=Label(root,text='dst_port:')
    text1 = Entry(root, bg='white', width=45)
    text2 = Entry(root, bg='white', width=45)
    text3 = Entry(root, bg='white', width=18)
    text4=Entry(root, bg='white', width=8)
    button1 = Button(root, text='浏览', width=8, command=selectExcelfile)
    button2 = Button(root, text='发送', width=8, command=doSend)
    button3 = Button(root, text='退出', width=8, command=closeThisWindow)
    button4 = Button(root, text='计算', width=8, command=cal_md5)

    scr = scrolledtext.ScrolledText(root, width=62, height=8,font=("隶书",10))  #滚动文本框（宽，高（这里的高应该是以行数为单位），字体样式）


    label1.pack()
    text1.pack()
    label2.pack()
    text2.pack()
    label3.pack()
    text3.pack()
    label4.pack()
    text4.pack()
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()

    scr.pack()

    label1.place(x=30, y=30)
    text1.place(x=100, y=30)
    label2.place(x=30, y=70)
    text2.place(x=100, y=70)
    label3.place(x=30, y=100)
    text3.place(x=100, y=100)
    label4.place(x=290, y=100)
    text4.place(x=360, y=100)
    button1.place(x=425, y=26)
    button2.place(x=160, y=150)
    button3.place(x=260, y=150)
    button4.place(x=425,y=65)

    scr.place(x=30,y=190)

    root.mainloop()


if __name__ == "__main__":
    main()
