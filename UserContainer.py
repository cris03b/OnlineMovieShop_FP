from tkinter import *
from User import User, Order, write_file_user, append_file_user, write_file_order


class UserMenu:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry("800x500")
        self.master.config(bg='gray21')
        self.master.title("User menu")

        self.title = Label(self.master, text="USER MENU", bg='gray21', fg="sienna2",
                           font=('times new roman bold', 28)).place(x=300, y=40)

        self.add_user_button = Button(self.master, text="Add user", bg='gray21', fg="green3", width=15, height=1,
                                      font=('times new roman', 15), command=self.add_user_window).place(x=110, y=150)

        self.chg_lname_button = Button(self.master, text="Change last name", bg='gray21', fg="green3", width=15,
                                       height=1, font=('times new roman', 15), command=self.change_lname_window).place(
            x=110, y=250)

        self.del_user_button = Button(self.master, text="Delete user", bg='gray21', fg="green3", width=15, height=1,
                                      font=('times new roman', 15), command=self.delete_user_window).place(x=110, y=350)

        self.user_list_button = Button(self.master, text="Show users", bg='gray21', fg="green3", width=15, height=1,
                                       font=('times new roman', 15), command=self.show_users_window).place(x=540, y=200)

        self.order_list_button = Button(self.master, text="Show orders", bg='gray21', fg="green3", width=15, height=1,
                                        font=('times new roman', 15), command=self.show_orders_window).place(x=540,
                                                                                                             y=300)

        self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.close_window).place(x=730, y=450)

        self.quitButton = Button(self.master, text="Quit", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.frame.quit).place(x=70, y=450)

        self.helpButton = Button(self.master, text="Help", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.help_window).place(x=20, y=450)

    def add_user_window(self):
        self.add_user = Toplevel(self.frame)
        app = AddUser(self.add_user)

    def change_lname_window(self):
        self.change_lname = Toplevel(self.frame)
        app = ChangeName(self.change_lname)

    def delete_user_window(self):
        self.delete_user = Toplevel(self.frame)
        app = DeleteUser(self.delete_user)

    def show_users_window(self):
        self.show_users = Toplevel(self.frame)
        app = ShowUsers(self.show_users)

    def show_orders_window(self):
        self.show_orders = Toplevel(self.frame)
        app = ShowOrders(self.show_orders)

    def help_window(self):
        self.help = Toplevel(self.frame)
        app = Help(self.help)

    def close_window(self):
        self.master.destroy()


class AddUser:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.user = User
        self.master.geometry('600x300')
        self.master.config(bg='gray21')
        self.master.title("Add user")

        self.lname = Label(self.master, text="Last name", bg='gray21', fg="orange", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_lname = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
        self.entry_lname.place(x=150, y=43)

        self.fname = Label(self.master, text="First name", bg='gray21', fg="orange",
                           font=('times new roman', 16)).place(
            x=40, y=90)

        self.entry_fname = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
        self.entry_fname.place(x=150, y=93)

        self.enter_button = Button(self.master, text="Enter", bg='gray21', fg='green3', font=(None, 12),
                                       command=lambda: self.verify(self.entry_lname.get(), self.entry_fname.get()))
        self.enter_button.place(x=400, y=91)

        self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def verify(self, lname, fname):
        """
        Se cauta last name si first name in listele de user
        Dc se gasesc, mesaj
        Dc nu se gasesc, se adauga in lista si mesaj
        :param lname: entry_lname
        :param fname: entry_fname
        """
        if lname in self.user.llname and fname in self.user.lfname:
            self.message = Label(self.master, text="Sorry, the user is already in the list :(", bg='gray21', fg="red",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=150)

        if lname not in self.user.llname or fname not in self.user.lfname:
            self.msg = Label(self.master, bg='gray21', font=(None, 20))
            self.msg.place(x=40, y=130, width=420, height=110)

            self.message = Label(self.master, text="User added successfully! ", bg='gray21', fg="green3",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=150)

            self.user.llname.append(lname)
            self.user.lfname.append(fname)

            self.enter_button.config(command=append_file_user)


class ChangeName:
    def __init__(self, master):
        self.user = User
        self.order = Order
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry('600x300')
        self.master.config(bg='gray21')
        self.master.title("Change last name")

        self.lname = Label(self.master, text="Last name", bg='gray21', fg="orange", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_lname = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
        self.entry_lname.place(x=170, y=43)

        self.fname = Label(self.master, text="First name", bg='gray21', fg="orange",
                           font=('times new roman', 16)).place(
            x=40, y=90)

        self.entry_fname = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
        self.entry_fname.place(x=170, y=93)

        self.enter_button = Button(self.master, text="Enter", bg='gray21', fg='green3', font=(None, 12),
                                   command=lambda: self.verify(self.entry_lname.get(), self.entry_fname.get()))
        self.enter_button.place(x=420, y=91)

        self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def verify(self, lname, fname):
        """
        Se cauta lname si fname in listele de user
        Dc nu se gasesc, mesaj
        Dc se gasesc, entry nou new last name si se creeaza butonul de change
        :param lname: entry_lname
        :param fname: entry_fname
        """
        self.lname = lname
        self.fname = fname
        found = False
        for i in range(len(self.user.llname)):
            if self.user.llname[i] == self.lname and self.user.lfname[i] == self.fname:
                self.msg = Label(self.master, bg='gray21', font=(None, 20))
                self.msg.place(x=40, y=140, width=400, height=200)

                self.poz = i
                self.new_lname = Label(self.master, text="New last name", bg='gray21', fg="orange",
                                       font=('times new roman', 16))
                self.new_lname.place(x=40, y=140)

                self.entry_new_lname = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
                self.entry_new_lname.place(x=170, y=143)

                self.change_button = Button(self.master, text="Change", bg='gray21', fg='green3', font=(None, 12),
                                            command=lambda: self.change_entry(self.entry_new_lname.get()))
                self.change_button.place(x=420, y=141)

                found = True

        if not found:
            self.msg = Label(self.master, bg='gray21', font=(None, 20))
            self.msg.place(x=40, y=193, width=600, height=300)

            self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                     command=self.close_window).place(x=530, y=240)

            self.message = Label(self.master, text="Sorry, the user is not in the list :( ", bg='gray21', fg="red",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=180)

    def change_entry(self, lastname):
        """
        Se schimba last name in fisierele user si order si mesaj
        :param lastname: entry_new_lname
        """
        self.user.llname[self.poz] = lastname
        write_file_user()
        for i in range(len(self.order.llastn)):
            if self.order.llastn[i] == self.lname and self.order.lfirstn[i] == self.fname:
                self.order.llastn[i] = lastname
                write_file_order()
        self.message = Label(self.master, text="Last name changed successfully! ", bg='gray21', fg="green3",
                             font=('times new roman', 20))
        self.message.place(x=40, y=220)


class DeleteUser:
    def __init__(self, master):
        self.user = User
        self.order = Order
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry('600x300')
        self.master.config(bg='gray21')
        self.master.title("Delete user")

        self.lname = Label(self.master, text="Last name", bg='gray21', fg="orange", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_lname = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
        self.entry_lname.place(x=150, y=43)

        self.fname = Label(self.master, text="First name", bg='gray21', fg="orange",
                           font=('times new roman', 16)).place(
            x=40, y=90)

        self.entry_fname = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
        self.entry_fname.place(x=150, y=93)

        self.delete_button = Button(self.master, text="Delete", bg='gray21', fg='green3', font=(None, 12),
                                    command=lambda: self.verify(self.entry_lname.get(), self.entry_fname.get()))
        self.delete_button.place(x=400, y=91)

        self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def verify(self, lname, fname):
        """
        Se cauta lname si fname in lista cu user, dc se gaseste se sterge si se cauta si in lista de order
        Dc se gaseste se sterge si din order
        Dc nu se gaseste un user, mesaj
        :param lname: entry_lname
        :param fname: entry_fname
        """
        found = False
        for i in range(len(self.user.llname)):
            if self.user.llname[i] == lname and self.user.lfname[i] == fname:
                found = True
                self.user.llname.pop(i)
                self.user.lfname.pop(i)
                self.delete_button.config(command=write_file_user)
                break
        if found:
            self.msg = Label(self.master, bg='gray21', font=(None, 20))
            self.msg.place(x=20, y=130, width=400, height=200)

            self.message = Label(self.master, text="User deleted successfully! ", bg='gray21', fg="green3",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=150)
            i = 0
            while i < len(self.order.llastn) - 1:
                if lname != self.order.llastn[i] or fname != self.order.lfirstn[i]:
                    i += 1

                else:
                    self.order.llastn.remove(lname)
                    self.order.lfirstn.remove(fname)
                    self.order.lorder.remove(self.order.lorder[i])
            if lname == self.order.llastn[-1] and fname == self.order.lfirstn[-1]:
                self.order.llastn.pop(-1)
                self.order.lfirstn.pop(-1)
                self.order.lorder.pop(-1)
            write_file_order()

        if not found:
            self.msg = Label(self.master, bg='gray21', font=(None, 20))
            self.msg.place(x=20, y=130, width=400, height=200)

            self.message = Label(self.master, text="Sorry, the user is not in the list :(", bg='gray21', fg="red",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=150)


class ShowUsers:
    def __init__(self, master):
        self.user = User
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.title("User list")

        t = Text(self.frame)
        for i in range(len(self.user.llname)):
            t.insert(END, self.user.llname[i] + ' ' + self.user.lfname[i] + '\n')
        t.grid()

        self.backButton = Button(self.frame, text="Back", font=(None, 12), command=self.close_window)
        self.backButton.grid(row=8, sticky=SE)

    def close_window(self):
        self.master.destroy()


class ShowOrders:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.order = Order
        self.master.title("Order list")

        t = Text(self.frame)
        for i in range(len(self.order.llastn)):
            t.insert(END, self.order.llastn[i] + ' ' + self.order.lfirstn[i] + ': ' + self.order.lorder[i] + '\n')
        t.grid()

        self.backButton = Button(self.frame, text="Back", font=(None, 12), command=self.close_window)
        self.backButton.grid(row=8, sticky=SE)

    def close_window(self):
        self.master.destroy()


class Help:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry('645x110')
        self.master.title("Help")

        t = Text(self.master, bg='light salmon', fg='black')
        t.insert(END, "If you want to add a user, choose ADD USER" + '\n' +
                 "If you want to change the last name to a user, choose CHANGE LAST NAME" + '\n' +
                 "If you want to delete a user, choose DELETE USER" + '\n' +
                 "If you want to see the list of users, choose SHOW USERS" + '\n' +
                 "If you want to see the list of orders, choose SHOW ORDERS")
        t.grid()

        self.backButton = Button(self.master, text="Back", font=(None, 10), command=self.close_window)
        self.backButton.place(x=600, y=80)

    def close_window(self):
        self.master.destroy()
