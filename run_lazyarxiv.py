import users
import urllib
import parsing_functions as pf
from bs4 import BeautifulSoup
import datetime as dt
import email_matches as email
import sys

def main():
    # Date range to search (last day)
    lastdate = (dt.date.today() - dt.timedelta(days=1)).strftime("%Y%m%d")
    currentdate = dt.date.today().strftime("%Y%m%d")
    query = pf.write_query(lastdate, currentdate)

    # Pull down new arxiv content
    xmlcontent = urllib.urlopen(query).read()

    #Load arxiv content and user list
    user_list = users.load_all_users('user_list.txt')
    soup = BeautifulSoup(xmlcontent, 'xml')
    article_list = pf.load_all_articles(soup)
    print len(article_list), "articles loaded"

    # Initialize email server
    server=email.initialize_email_server()
    fromaddr='calvin.job.done@gmail.com'

    # For each user, generate a list of interesting articles
    for user in user_list:
        interesting = pf.match_keywords(user.kwlist, article_list)
        pf.print_all_articles(interesting)

        if len(sys.argv) == 1:
            print interesting
        else:
            email_output = pf.generate_email_output(interesting)
            email.send_email(server, fromaddr, user.email, email_output)

    email.shutdown_email_server(server)


if __name__ == "__main__":
    main()
