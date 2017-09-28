import users
import urllib
import parsing_functions as pf
from bs4 import BeautifulSoup
import datetime as dt

def main():
    # NEEDS TO BE IMPLEMENTED. DATE AND TIME OF LAST SCRAPE
    # NEED THIS TO AVOID DUPLICATES dt.timedelta(days=1)
    lastdate = (dt.date.today() - dt.timedelta(days=1)).strftime("%Y%m%d")
    currentdate = dt.date.today().strftime("%Y%m%d")
    query = pf.write_query(lastdate, currentdate)

    # Pull down new arxiv content
    xmlcontent = urllib.urlopen(query).read()

    #Load arxiv content and user list
    user_list = users.load_all_users('user_list.txt')
    soup = BeautifulSoup(xmlcontent, 'xml')
    #with open("tests/test_call.txt") as fp:
    #    soup = BeautifulSoup(fp, 'xml') 
    article_list = pf.load_all_articles(soup)
    print len(article_list), "articles loaded"

    # For each user, generate a list of interesting articles
    for user in user_list:
        print"######################################################"
        print user
        interesting = pf.match_keywords(user.kwlist, article_list)
        pf.print_all_articles(interesting)




if __name__ == "__main__":
    main()
