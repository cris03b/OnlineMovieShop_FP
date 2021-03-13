from tkinter import *
from Filme import Filme, append_file_movie, write_file_movie


class MovieMenu:

    def __init__(self, master):
        self.filme = Filme
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry("800x500")
        self.master.config(bg='gray21')
        self.master.title("Movie menu")

        self.title = Label(self.master, text="MOVIE MENU", bg='gray21', fg="sienna2",
                           font=('times new roman bold', 28)).place(x=300, y=40)

        self.add_movie_button = Button(self.master, text="Add movie", bg='gray21', fg="green3", width=15, height=1,
                                       font=('times new roman', 15), command=self.add_movie_window).place(x=110, y=200)

        self.chg_price_button = Button(self.master, text="Change price", bg='gray21', fg="green3", width=15, height=1,
                                       font=('times new roman', 15), command=self.change_price_window).place(x=110,
                                                                                                             y=300)

        self.movie_list_button = Button(self.master, text="Show movies", bg='gray21', fg="green3", width=15, height=1,
                                        font=('times new roman', 15), command=self.show_movies_window).place(x=540,
                                                                                                             y=250)

        self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.close_window).place(x=730, y=450)

        self.quitButton = Button(self.master, text="Quit", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.frame.quit).place(x=70, y=450)

        self.helpButton = Button(self.master, text="Help", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.help_window).place(x=20, y=450)

    def close_window(self):
        self.master.destroy()

    def help_window(self):
        self.help = Toplevel(self.frame)
        app = Help(self.help)

    def add_movie_window(self):
        self.add_movie = Toplevel(self.frame)
        app = AddMovie(self.add_movie)

    def change_price_window(self):
        self.change_price = Toplevel(self.frame)
        app = ChangePrice(self.change_price)

    def show_movies_window(self):
        self.show_movies = Toplevel(self.frame)
        app = ShowMovies(self.show_movies)


class AddMovie:

    def __init__(self, master):
        self.filme = Filme
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry('600x300')
        self.master.config(bg='gray21')
        self.master.title("Add movie")

        self.title = Label(self.master, text="Title", bg='gray21', fg="orange", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_title = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
        self.entry_title.place(x=110, y=43)

        self.add_button = Button(self.master, text="Add", bg='gray21', fg='green3', font=(None, 12),
                                 command=lambda: self.verify(self.entry_title.get()))
        self.add_button.place(x=400, y=41)

        self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def verify(self, movie):
        """
        Se cauta movie in lista cu filme, dc nu se gaseste se formeaza entry_*proprietati film*, add_actors_button
        pt a adauga actori
        Dc se gaseste, mesaj
        :param movie: entry_title
        """
        if movie in self.filme.lmovie:
            self.message = Label(self.master, text="Sorry, the movie already exists :( ", bg='gray21', fg="red",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=120)

        if movie not in self.filme.lmovie:
            self.msg = Label(self.master, bg='gray21', font=(None, 20))
            self.msg.place(x=40, y=120, width=400, height=200)

            self.year = Label(self.master, text="Year", bg='gray21', fg="orange", font=('times new roman', 16)).place(
                x=40, y=90)
            self.entry_year = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
            self.entry_year.place(x=110, y=93)

            self.rating = Label(self.master, text="Rating", bg='gray21', fg="orange",
                                font=('times new roman', 16)).place(x=40, y=140)
            self.entry_rating = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
            self.entry_rating.place(x=110, y=139)

            self.price = Label(self.master, text="Price", bg='gray21', fg="orange", font=('times new roman', 16)).place(
                x=40, y=185)
            self.entry_price = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
            self.entry_price.place(x=110, y=187)

            self.actors = Label(self.master, text="Actors", bg='gray21', fg="orange",
                                font=('times new roman', 16)).place(x=40, y=235)

            self.entry_actors = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
            self.entry_actors.place(x=110, y=238)

            self.actor_string = ""
            self.add_actors_button = Button(self.master, text="Enter", bg='gray21', fg='green3', font=(None, 10),
                                            command=lambda: self.add_actor(self.entry_actors.get())).place(x=340, y=240)


            self.add_button.configure(
                command=lambda: self.add_entry(self.entry_title.get(), self.entry_year.get(), self.entry_rating.get(),
                                               self.entry_price.get()))

    def add_entry(self, movie, year, rating, price):
        """
        se adauga *propr. film* la liste si la fisier, mesaj
        :param movie: entry_title
        :param year: entry_year
        :param rating: entry_rating
        :param price: entry_price
        """
        self.filme.lmovie.append(movie)
        self.filme.lyear.append(year)
        self.filme.lrating.append(rating)
        self.filme.lprice.append(price)
        self.filme.lactors.append(self.actor_string)
        append_file_movie()
        self.message = Label(self.master, text="Movie added successfully! ", bg='gray21', fg="green3",
                             font=('times new roman', 18))
        self.message.place(x=340, y=138)

    def add_actor(self, actor):
        self.actor_string += actor
        self.actor_string += ", "


class ChangePrice:
    def __init__(self, master):
        self.filme = Filme
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.geometry('600x300')
        self.master.config(bg='gray21')
        self.master.title("Change price")

        self.title = Label(self.master, text="Title", bg='gray21', fg="orange", font=('times new roman', 16)).place(
            x=40, y=40)

        self.entry_title = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
        self.entry_title.place(x=150, y=43)

        self.enter_button = Button(self.master, text="Enter", bg='gray21', fg='green3', font=(None, 12),
                                   command=lambda: self.verify(self.entry_title.get()))
        self.enter_button.place(x=400, y=41)

        self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                 command=self.close_window).place(x=530, y=240)

    def close_window(self):
        self.master.destroy()

    def verify(self, movie):
        """
        Se cauta movie in lista cu filme
        Dc se gaseste se creeaza entry_new_price
        Dc nu se gaseste, mesaj
        :param movie: entry_title
        :return:
        """
        found = False
        for i in range(len(self.filme.lmovie)):
            if movie == self.filme.lmovie[i]:
                self.msg = Label(self.master, bg='gray21', font=(None, 20))
                self.msg.place(x=40, y=120, width=400, height=200)

                self.poz = i
                self.new_price = Label(self.master, text="New price", bg='gray21', fg="orange",
                                       font=('times new roman', 16)).place(x=40, y=90)
                self.entry_new_price = Entry(self.master, bg='gray21', fg='white', font=('times new roman', 15))
                self.entry_new_price.place(x=150, y=93)

                self.change_button = Button(self.master, text="Change", bg='gray21', fg='green3', font=(None, 12),
                                            command=lambda: self.change_entry(self.entry_new_price.get()))
                self.change_button.place(x=400, y=93)

                found = True

        if not found:
            self.msg = Label(self.master, bg='gray21', font=(None, 20))
            self.msg.place(x=40, y=93, width=600, height=400)

            self.backButton = Button(self.master, text="Back", bg='gray17', fg='tomato2', font=(None, 12),
                                     command=self.close_window).place(x=530, y=240)

            self.message = Label(self.master, text="Sorry, the movie is not in the list :( ", bg='gray21', fg="red",
                                 font=('times new roman', 20))
            self.message.place(x=40, y=180)

    def change_entry(self, price):
        """
        Se inlocuieste pretul vechi cu cel nou in fisier si liste
        :param price: entry_new_price
        """
        self.filme.lprice[self.poz] = price
        write_file_movie()

        self.message = Label(self.master, text="Price changed successfully! ", bg='gray21', fg="green3",
                                     font=('times new roman', 20))
        self.message.place(x=40, y=180)

class ShowMovies:
    def __init__(self, master):
        self.filme = Filme
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.master.title("Movie list")

        t = Text(self.frame)
        for i in range(len(self.filme.lmovie)):
            t.insert(END, self.filme.lmovie[i] + ',' + self.filme.lyear[i] + "," + self.filme.lrating[i] + "," +
                     self.filme.lprice[i] +
                     "," + self.filme.lactors[i] + '\n')
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
        self.master.geometry('530x100')
        self.master.config(bg='gray21')
        self.master.title("Help")

        t = Text(self.master, bg='light salmon', fg='black')
        t.insert(END,
                 "If you want to add a movie, choose ADD MOVIE" + '\n' +
                 "If you want to change the price to a movie, choose CHANGE PRICE" + '\n' +
                 "If you want to see the list of movies, choose SHOW MOVIES")

        t.grid()
        self.backButton = Button(self.master, text="Back", font=(None, 10), command=self.close_window)
        self.backButton.place(x=480, y=65)

    def close_window(self):
        self.master.destroy()
