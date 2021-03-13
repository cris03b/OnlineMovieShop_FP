from tkinter import *
from User import User, Order, append_file_order
from Filme import Filme


class MainMenu:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry("800x500")
        self.master.config(bg='gray21')
        self.master.title("Main menu")

        self.title = Label(self.master, text="MAIN MENU", bg='gray21', fg="sienna2",
                           font=('times new roman bold', 28)).place(x=300, y=40)

        self.place_order_button = Button(self.master, text="Place order", bg='gray21', fg="green3", width=15, height=1,
                                         font=('times new roman', 15), command=self.order_window).place(x=110, y=200)

        self.total_price_button = Button(self.master, text="Total", bg='gray21', fg="green3", width=15, height=1,
                                         font=('times new roman', 15), command=self.total_window).place(x=110, y=300)

        self.rating_search_button = Button(self.master, text="Search by rating", bg='gray21', fg="green3", width=15,
                                           height=1, font=('times new roman', 15), command=self.rating_window).place(x=540, y=200)

        self.actor_search_button = Button(self.master, text="Search by actor", bg='gray21', fg="green3", width=15,
                                          height=1, font=('times new roman', 15), command=self.actor_window).place(x=540, y=300)

        self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.close_window).place(x=730, y=450)

        self.quitButton = Button(self.master, text="Quit", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.frame.quit).place(x=70, y=450)

        self.helpButton = Button(self.master, text="Help", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.help_window).place(x=20, y=450)

    def order_window(self):
        self.order = Toplevel(self.frame)
        app = PlaceOrder(self.order)

    def total_window(self):
        self.total = Toplevel(self.frame)
        app = Total(self.total)

    def rating_window(self):
        self.rating = Toplevel(self.frame)
        app = Rating(self.rating)

    def actor_window(self):
        self.actor = Toplevel(self.frame)
        app = Actor(self.actor)

    def help_window(self):
        self.help = Toplevel(self.frame)
        app = Help(self.help)

    def close_window(self):
        self.master.destroy()


class PlaceOrder:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.user = User
        self.order = Order
        self.filme = Filme
        self.master.geometry('600x300')
        self.master.config(bg='gray21')
        self.master.title("Place order")

        self.lname = Label(self.master, text="Last name", bg='gray21', fg="orange", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_lname = Entry(self.master,  bg='gray21', fg='white', font=('times new roman', 15))
        self.entry_lname.place(x=150, y=43)

        self.fname = Label(self.master, text="First name", bg='gray21', fg="orange", font=('times new roman', 16)).place(
                x=40, y=90)

        self.entry_fname = Entry(self.master,  bg='gray21', fg='white', font=('times new roman', 15))
        self.entry_fname.place(x=150, y=93)

        self.enter_button = Button(self.master, text="Enter", bg='gray21', fg='green3', font=(None, 12),
                                   command=lambda: self.user_verify(self.entry_lname.get(), self.entry_fname.get()))
        self.enter_button.place(x=400, y=91)

        self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def user_verify(self, lname, fname):
        """
        Se cauta lname si fname in lista cu user, dc nu se gasesc, mesaj:
        Dc se gaseste, se creeaza entry_title pt film si se config. enter_button legat de functia movie_verify
        :param lname: entry_lname
        :param fname: entry_fname
        """
        self.lname = lname
        self.fname = fname
        user_found = False

        for i in range(len(self.user.llname)):
            if self.user.llname[i] == self.lname and self.user.lfname[i] == fname:
                user_found = True
                break
        if user_found:
            self.msg = Label(self.master, bg='gray21', font=(None, 20))
            self.msg.place(x=40, y=130, width=400, height=200)

            self.title = Label(self.master, text="Movie title", bg='gray21', fg="orange",
                                font=('times new roman', 16)).place(x=40, y=140)

            self.entry_title = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
            self.entry_title.place(x=150, y=139)

            self.enter_button.configure(command=lambda: self.movie_verify(self.entry_title.get()))

        if not user_found:
            self.msg = Label(self.master, bg='gray21', font=(None, 20))
            self.msg.place(x=40, y=140, width=600, height=200)

            self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                     command=self.close_window).place(x=530, y=240)

            self.message = Label(self.master, text="Sorry, the user is not in the list :(",  bg='gray21', fg="red",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=150)

    def movie_verify(self, movie):
        """
        Se cauta movie in lista cu filme, dc nu se gaseste, mesaj
        Dc se gaseste, se creeaza add_button
        :param movie: entry_title
        """
        self.movie = movie

        if self.movie not in self.filme.lmovie:
            self.msg = Label(self.master, bg='gray21', font=(None, 20))
            self.msg.place(x=40, y=240, width=600, height=100)

            self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                     command=self.close_window).place(x=530, y=240)

            self.message = Label(self.master, text="Sorry, the movie is not in the list :( ", bg='gray21', fg="red",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=200)

        if self.movie in self.filme.lmovie:
            self.msg = Label(self.master, bg='gray21', font=(None, 20))
            self.msg.place(x=40, y=200, width=400, height=400)

            self.add_button = Button(self.frame, text="Place order",
                                     command=self.add_entry(self.entry_lname.get(), self.entry_fname.get(),
                                                            self.entry_title.get()))
            self.add_button.place(x=400, y=139)

    def add_entry(self, lname, fname, movie):
        """
        Se adauga in liste si fisier lname, fname si movie, mesaj
        :param lname: entry_lname
        :param fname: entry_fname
        :param movie: entry_title
        """
        self.order.llastn.append(lname)
        self.order.lfirstn.append(fname)
        self.order.lorder.append(movie)
        append_file_order()
        self.message = Label(self.master, text="Order placed! ", bg='gray21', fg="green3",
                                 font=('times new roman', 20))
        self.message.place(x=40, y=200)


class Total:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.user = User
        self.order = Order
        self.filme = Filme
        self.master.geometry('600x300')
        self.master.config(bg='gray21')
        self.master.title("Total order")

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
                                   command=lambda: self.user_verify(self.entry_lname.get(), self.entry_fname.get()))
        self.enter_button.place(x=400, y=91)

        self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def user_verify(self, lname, fname):
        """
        Se cauta lname si fname in lista cu order
        Dc nu se gasesc, se cauta in lista cu user
        Dc nu se gasesc in lista cu user, mesaj *User nu exista*
        Dc se gasesc in lista cu user, mesaj *User nu a facut nicio comanda*
        Dc se gasesc in lista cu order, se arata totalul
        :param lname: entry_lname
        :param fname: entry_fname
        """
        self.lname = lname
        self.fname = fname
        order_found = False
        user_found = False
        total = 0

        for i in range(len(self.order.llastn)):
            if self.order.llastn[i] == self.lname and self.order.lfirstn[i] == fname:
                order_found = True
                break

        if order_found:
            self.msg = Label(self.master, bg='gray21', font=(None, 20))
            self.msg.place(x=20, y=130, width=400, height=200)

            for i in range(len(self.order.llastn)):
                if self.order.llastn[i] == self.lname and self.order.lfirstn[i] == self.fname:
                    movie = self.order.lorder[i]
                    for j in range(len(self.filme.lmovie)):
                        if self.filme.lmovie[j] == movie:
                            total += float(self.filme.lprice[j])
            t = Text(self.master, bg='gray21', fg='green3', font=('times new roman', 18))
            t.insert(END, "Total: " + str(total))
            t.place(x=100, y=170)

            self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                     command=self.close_window).place(x=530, y=240)

        if not order_found:
            self.msg = Label(self.master, bg='gray21', font=(None, 20))
            self.msg.place(x=40, y=140, width=600, height=200)

            self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                     command=self.close_window).place(x=530, y=240)

            for i in range(len(self.user.llname)):
                if self.user.llname[i] == self.lname and self.user.lfname[i] == fname:
                    user_found = True
                    break
            if user_found:
                self.message = Label(self.master, text="The user didn't place any order", bg='gray21', fg="red",
                                     font=('times new roman', 20))
                self.message.place(x=40, y=150)
            else:
                self.message = Label(self.master, text="Sorry, the user is not in the list :(", bg='gray21', fg="red",
                                     font=('times new roman', 20))
                self.message.place(x=40, y=150)


class Rating:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.filme = Filme
        self.master.geometry('600x300')
        self.master.config(bg='gray21')
        self.master.title("Search movie by rating")

        self.rating_label = Label(self.master, text="Rating", bg='gray21', fg="orange", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_rating = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
        self.entry_rating.place(x=150, y=43)

        self.search_button = Button(self.master, text="Search", bg='gray21', fg='green3', font=(None, 12), command=lambda: self.search(self.entry_rating.get()))
        self.search_button.place(x=400, y=41)

        self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def search(self, rating):
        """
        Se cauta filmele cu rating-ul mai mare decat entry_rating
        Mesaj dc nu sunt filme cu rating mai mare decat entry_rating
        :param rating: entry_rating
        """
        self.rating = rating
        movie_found = False
        list_movies = []
        for i in range(len(self.filme.lrating)):
            if float(self.filme.lrating[i]) > float(self.rating):
                list_movies.append(self.filme.lmovie[i])
                movie_found = True
        if movie_found:
            t = Text(self.master, bg='gray21', fg='green3', font=('times new roman', 15))
            for i in range(len(list_movies)):
                t.insert(END, list_movies[i] + '\n')
            t.place(x=40, y=110)

            self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                     command=self.close_window).place(x=530, y=240)

        else:
            t = Text(self.master, bg='gray21', fg='red', font=('times new roman', 18))
            t.insert(END, "Sorry, but there's no movie with a rating over " + str(self.rating) + " :(")
            t.place(x=40, y=110)

            self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                     command=self.close_window).place(x=530, y=240)


class Actor:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.filme = Filme
        self.master.geometry('600x300')
        self.master.config(bg='gray21')
        self.master.title("Search movie by actor")

        self.actor_label = Label(self.master, text="Actor: ", bg='gray21', fg="orange", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_actor = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
        self.entry_actor.place(x=150, y=43)

        self.search_button = Button(self.master, text="Search", bg='gray21', fg='green3', font=(None, 12), command=lambda: self.search(self.entry_actor.get()))
        self.search_button.place(x=400, y=41)

        self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def search(self, actor):
        """
        Se cauta entry_actor in lista cu actori, dc nu se gseste, mesaj
        :param actor: entry_actor
        """
        self.actor = actor
        movie_found = False
        list_movies = []
        for i in range(len(self.filme.lactors)):
            actors = str(self.filme.lactors[i]).split(', ')
            for j in range(len(actors)):
                if actors[j] == self.actor:
                    list_movies.append(self.filme.lmovie[i])
                    movie_found = True

        if movie_found:
            t = Text(self.master, bg='gray21', fg='green3', font=('times new roman', 15))
            for i in range(len(list_movies)):
                t.insert(END, list_movies[i] + '\n')
            t.place(x=40, y=110)

            self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                     command=self.close_window).place(x=530, y=240)

        else:
            t = Text(self.master, bg='gray21', fg='red', font=('times new roman', 18))
            t.insert(END, "Sorry, but there's no movie with " + str(self.actor) + " in it :(")
            t.place(x=40, y=110)

            self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                     command=self.close_window).place(x=530, y=240)


class Help:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry('645x110')
        self.master.title("Help")

        t = Text(self.master, bg='light salmon', fg='black')
        t.insert(END, "If you want to place an order, choose PLACE ORDER" + '\n' +
                 "If you want to see the total cost of your order, choose TOTAL" + '\n' +
                 "If you want to see the movies with a rating over ..., choose SEARCH BY RATING" + '\n' +
                 "If you want to see the movies with actor ... in them, choose SEARCH BY ACTOR")
        t.grid()

        self.backButton = Button(self.master, text="Back", font=(None, 10), command=self.close_window)
        self.backButton.place(x=600, y=80)

    def close_window(self):
        self.master.destroy()
