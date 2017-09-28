import numpy as np
import re
from bs4 import BeautifulSoup

class Article():
    def __init__(self):
        pass

    def __repr__(self):
        if len(self.authors) > 1: authors = self.authors #Can do something special here
        else: authors = self.authors
        return """Title: %s\nAuthors: %s \nAbstract: %s\n%s\n""" % (self.title, authors, self.abstract, self.link)

def load_title(entry):
    return entry.title.string

def load_authors(entry):
    author_list_dirty = entry.find_all('author')
    author_list = [ad.find('name').string for ad in author_list_dirty]
    return author_list

def load_abstract(entry):
    return entry.summary.string.lstrip()

def load_link(entry):
    return entry.id.string

def load_article(entry):
    article = Article()
    article.title = load_title(entry)
    article.authors = load_authors(entry)
    article.abstract = load_abstract(entry)
    article.link = load_link(entry)
    return article

def load_all_articles(soup):
    entry_list = soup.find_all('entry')
    article_list = [load_article(entry) for entry in entry_list]
    return article_list

def print_all_articles(alist):
    for article in alist:
        print article
    return

def find_word(kw):
    return re.compile(r'\b({0})\b'.format(kw), flags=re.IGNORECASE).search

def check_authors(kw, authors):
    for auth in authors:
        if kw == auth:
            return True
    return False

def remove_duplicates(articles):
    return list(set(articles))

def match_keywords(kwlist, article_list):
    interesting = []
    for article in article_list:
        for kw in kwlist:
            if find_word(kw)(article.title) is not None:
                interesting.append(article)
            elif find_word(kw)(article.abstract) is not None:
                interesting.append(article)
            elif check_authors(kw, article.authors):
                interesting.append(article)

    interesting = remove_duplicates(interesting)
    return interesting

def write_query(lastdate, currentdate):
    base = "http://export.arxiv.org/api/query?search_query=%28astro-ph.GA+OR+astro-ph.CO+OR+astro-ph.EP+OR+astro-ph.HE+OR+astro-ph.IM+OR+astro-ph.SR%29+AND+submittedDate:["
    query = base + lastdate + '0000+TO+' + currentdate + '0000]&max_results=500&sortBy=submittedDate&sortOrder=descending'
    return query


if __name__ == "__main__":
    with open("tests/test_call.txt") as fp:
        soup = BeautifulSoup(fp, 'xml')

    article_list = load_all_articles(soup)
    print_all_articles(article_list)

