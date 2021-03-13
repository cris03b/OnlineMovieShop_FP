from tkinter import *
import FilmeContainer, UserContainer, MainContainer, User, Filme

fcont = FilmeContainer
ucont = UserContainer
mcont = MainContainer
movie_menu = fcont.MovieMenu
user_menu = ucont.UserMenu
main_menu = mcont.MainMenu
User.read_file_user()
User.read_file_order()
Filme.read_file_movie()


class Main:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.title("ONLINE MOVIE-SHOP")

        self.title = Label(self.master, text="WELCOME!", bg='gray21', fg="green4", font=('times new roman bold', 30)).place(x=300,
                                                                                                               y=40)

        self.subtitle = Label(self.master, text="What do you want to do...", bg='gray21', fg="sienna2",
                              font=('times new roman', 23)).place(x=260, y=110)

        self.button_user_menu = Button(self.master, text="USER MENU", bg='gray21', fg="green3", width=15, height=1,
                                       font=('times new roman', 15), command=self.user_window).place(x=65, y=240)

        self.button_main_menu = Button(self.master, text="MAIN MENU", bg='gray21', fg="green3", width=15, height=1,
                                       font=('times new roman', 15), command=self.main_window).place(x=325, y=240)

        self.button_movie_menu = Button(self.master, text="MOVIE MENU", bg='gray21', fg="green3", width=15, height=1,
                                        font=('times new roman', 15), command=self.movie_window).place(x=585, y=240)

        self.quit_button = Button(self.master, text="QUIT", bg='gray17', fg='tomato2', font=(None, 12),
                                  command=self.close_window).place(x=730, y=450)

    def close_window(self):
        self.master.destroy()

    def user_window(self):
        self.user_window = Toplevel(self.frame)
        app = user_menu(self.user_window)

    def main_window(self):
        self.main_window = Toplevel(self.frame)
        app = main_menu(self.main_window)

    def movie_window(self):
        self.movie_window = Toplevel(self.frame)
        app = movie_menu(self.movie_window)


root = Tk()
root.config(bg='gray21')
root.geometry("800x500")
main = Main(root)
root.mainloop()
