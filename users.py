
class User():
    def __init__(self, lines):
        print lines
        self.name  = lines[0]
        self.email = lines[1]
        self.parse_keywords(lines[2])

    def parse_keywords(self, kwline):
        kwlist = kwline.split("\ ")
        self.kwlist = [kw.strip("\"") for kw in kwlist]
        return
    """
        print kwlist
        self.kwlist = []
        # Gross for loop but it was the first way I could think of doing this
        for i in range(len(kwlist)):
            if kwlist[i][0] == '\"' and self.check_end__(kwlist[i]):
                self.kwlist.append(kwlist[i][1:-1])
            elif kwlist[i][0] == '\"':
                partialkw = kwlist[i][1:]+' '
                while not self.check_end__(kwlist[i]):
                    i+=1
                    if self.check_end__(kwlist[i]):
                        partialkw += kwlist[i][:-1]
                    else:
                        partialkw += kwlist[i]+' '
                self.kwlist.append(partialkw)
                """

    def check_end__(self, string):
        if string[-1] == '\"':
            return True
        return False


    def __repr__(self):
        return '%s\n%s\nKeyWords: %s\n' % (self.name, self.email, self.kwlist)

def load_all_users(fname="users.txt"):
    user_list = []
    with open(fname, "r") as infile:
        lines = infile.readlines()
        last = lines[-1]
        ulines = []
        for line in lines:
            if line.strip() is not "":
                ulines.append(line.strip())
            if line is "\n" or line is last: 
                user_list.append(User(ulines))
                uline = []

    print user_list

    return user_list
    

if __name__ == "__main__":
    user_list = load_all_users("tests/example_users.txt")
    for user in user_list:
        print user
