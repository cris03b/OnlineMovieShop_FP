class User:
    llname = []
    lfname = []

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def __str__(self):
        return self.last_name + " " + self.first_name


def read_file_user():
    with open("user.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            line_sep = line.split('/')
            user = User(line_sep[0], line_sep[1])
            user.llname.append(line_sep[0])
            user.lfname.append(line_sep[1])


def append_file_user():
    user = User
    with open("user.txt", 'a') as f:
        f.write('\n')
        f.write(str(user.llname[-1]) + "/" + str(user.lfname[-1]) + "/")


def write_file_user():
    user = User
    with open("user.txt", 'w') as f:
        for i in range(len(user.llname) - 1):
            f.write(str(user.llname[i]) + "/" + str(user.lfname[i]) + "/")
            f.write('\n')
        f.write(str(user.llname[-1]) + "/" + str(user.lfname[-1]) + "/")


class Order(User):
    llastn = []
    lfirstn = []
    lorder = []

    def __init__(self, last_name, first_name, order):
        super().__init__(last_name, first_name)
        self.order = order

    def get_order(self):
        return self.order

    def set_order(self, order):
        self.order = order

    def __str__(self):
        return self.last_name + " " + self.first_name + " " + self.order


def read_file_order():
    with open("order.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            line_sep = line.split('/')
            ord = Order(line_sep[0], line_sep[1], line_sep[2])
            ord.llastn.append(line_sep[0])
            ord.lfirstn.append(line_sep[1])
            ord.lorder.append(line_sep[2])


def append_file_order():
    ord = Order
    with open("order.txt", 'a') as f:
        f.write('\n')
        f.write(str(ord.llastn[-1]) + "/" + str(ord.lfirstn[-1]) + "/" + str(ord.lorder[-1]) + "/")


def write_file_order():
    ord = Order
    with open("order.txt", 'w') as f:
        for i in range(len(ord.llastn) - 1):
            f.write(str(ord.llastn[i]) + "/" + str(ord.lfirstn[i]) + "/" + str(ord.lorder[i]) + "/")
            f.write('\n')
        f.write(str(ord.llastn[-1]) + "/" + str(ord.lfirstn[-1]) + "/" + str(ord.lorder[-1] + "/"))
