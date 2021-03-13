class Filme:
    lmovie = []
    lyear = []
    lrating = []
    lprice = []
    lactors = []

    def __init__(self, title, year, rating, price, actors):
        self.title = title
        self.year = year
        self.rating = rating
        self.price = price
        self.actors = actors

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        self.rating = rating

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_actors(self):
        return self.actors

    def set_actors(self, actors):
        self.actors = actors

    def __str__(self):
        return self.title + " " + self.year + " " + self.rating + " " + self.price + " " + self.actors


def read_file_movie():
    with open("filme.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            line_sep = line.split('/')
            filme = Filme(line_sep[0], line_sep[1], line_sep[2], line_sep[3], line_sep[4])
            filme.lmovie.append(line_sep[0])
            filme.lyear.append(line_sep[1])
            filme.lrating.append(line_sep[2])
            filme.lprice.append(line_sep[3])
            filme.lactors.append(line_sep[4])


def append_file_movie():
    filme = Filme
    with open("filme.txt", 'a') as f:
        f.write('\n')
        f.write(str(filme.lmovie[-1]) + "/" + str(filme.lyear[-1]) + "/" + str(filme.lrating[-1]) + "/" + str(
                filme.lprice[-1]) + "/" + str(filme.lactors[-1]) + "/")


def write_file_movie():
    filme = Filme
    with open("filme.txt", 'w') as f:
        for i in range(len(filme.lmovie)-1):
            f.write(str(filme.lmovie[i]) + "/" + str(filme.lyear[i]) + "/" + str(filme.lrating[i]) + "/" + str(
                filme.lprice[i]) + "/" + str(filme.lactors[i]) + "/")
            f.write('\n')
        f.write(str(filme.lmovie[-1]) + "/" + str(filme.lyear[-1]) + "/" + str(filme.lrating[-1]) + "/" + str(
                filme.lprice[-1]) + "/" + str(filme.lactors[-1]) + "/")
