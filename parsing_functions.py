import numpy as np
from bs4 import BeautifulSoup

class Article():
    def __init__(self):
        pass

    def __repr__(self):
        if len(self.authors) > 1:
            return """%s\nAuthors: %s et al.\nAbstract: %s\n%s\n""" % (self.title, self.authors[0], self.abstract, self.link)
        if len(self.authors) == 1:
            return """%s\nAuthors: %s\nAbstract: %s\n%s\n""" % (self.title, self.authors[0], self.abstract, self.link)

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


if __name__ == "__main__":
    with open("tests/test_call.txt") as fp:
        soup = BeautifulSoup(fp, 'xml')

    article_list = load_all_articles(soup)
    print_all_articles(article_list)

