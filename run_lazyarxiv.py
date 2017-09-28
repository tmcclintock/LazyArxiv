import users
import parsing_functions as pf
from bs4 import BeautifulSoup

def main():
    # NEEDS TO BE IMPLEMENTED. DATE AND TIME OF LAST SCRAPE
    # NEED THIS TO AVOID DUPLICATES
    date = 1.0#pf.load_last_scrape()

    # Pull down new arxiv content
    # Saves to a local file
    #pf.pull_from_arxiv()

    #Load arxiv content and user list
    user_list = users.load_all_users('tests/example_users.txt')
    with open("tests/test_call.txt") as fp:
        soup = BeautifulSoup(fp, 'xml') 
    article_list = pf.load_all_articles(soup)

    # For each user, generate a list of interesting articles
    for user in user_list:
        print"######################################################"
        print user
        interesting = pf.match_keywords(user.kwlist, article_list)
        pf.print_all_articles(interesting)




if __name__ == "__main__":
    main()
