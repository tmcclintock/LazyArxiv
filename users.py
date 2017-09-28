
class User():
    def __init__(self, lines):
        self.name  = lines[0]
        self.email = lines[1]
        self.parse_keywords(lines[2])

    def parse_keywords(self, kwline):
        """Get the keywords associated with this user.

        Args:
        kwline (array of strings): An array of keyword phrases.

        Returns:
        None
        """
        kwlist = kwline.split("\" \"")
        self.kwlist = [kw.strip("\"") for kw in kwlist]
        return

    def __repr__(self):
        return '%s\n%s\nKeyWords: %s\n' % (self.name, self.email, self.kwlist)

def load_all_users(fname="users.txt"):
    """Take in a user list and figure out the user's name, email, and keywords.

    Args:
    fname (string): name of the user list file. Default is users.txt

    Returns:
    user_list (array of Users): Contains user's information.
    """
    user_list = []
    with open(fname, "r") as infile:
        lines = infile.readlines()
        last = lines[-1]
        ulines = []
        for line in lines:
            if line.strip() is not "":
                ulines.append(line.strip())
            if line.strip() is "" or line is last: 
                user_list.append(User(ulines))
                ulines = []
    return user_list
    

if __name__ == "__main__":
    user_list = load_all_users("tests/example_users.txt")
    for user in user_list:
        print user
