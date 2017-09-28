
class User():
    def __init__(self, line):
        self.fname = line[0]
        self.lname = line[1]
        self.email = line[2]
        self.parse_keywords(line[3:])
        #print "line", line[3:]
        #print "Did it work?", self.kwlist

    def parse_keywords(self, kwlist):
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

    def check_end__(self, string):
        if string[-1] == '\"':
            return True
        return False


    def __repr__(self):
        return '%s %s\n%s\n%s\n' % (self.fname, self.lname, self.email, self.kwlist)

def load_all_users(fname="users.txt"):
    lines = [line.rstrip('\n') for line in open(fname)]
    user_list = [User(line.split()) for line in lines]
    return user_list
    

if __name__ == "__main__":
    user_list = load_all_users("tests/example_users.txt")
    for user in user_list:
        print user
