import numpy as np
import sys
sys.path.insert(0,'../')
import parsing_functions as pf
from bs4 import BeautifulSoup
import pytest


def test_load_title():
    with open("test_call.txt") as fp:
        soup = BeautifulSoup(fp, 'xml')
    title = pf.load_title(soup)
    assert title == "Sample title with searchable keywords such as photons!"
    return

def test_load_authors():
    with open("test_call.txt") as fp:
        soup = BeautifulSoup(fp, 'xml')
    author_list = pf.load_authors(soup)
    assert author_list == ["Matthew Kirby", "Tom McClintock"]
    return

def test_load_abstract():
    with open("test_call.txt") as fp:
        soup = BeautifulSoup(fp, 'xml')
    abstract = pf.load_abstract(soup)
    assert abstract == "Something, something positrons."
    return

def test_load_link():
    with open("test_call.txt") as fp:
        soup = BeautifulSoup(fp, 'xml')
    link = pf.load_link(soup)
    assert link == "http://arxiv.org"
    return

#def test_load_article():
#    with open("test_call.txt") as fp:
#        soup = BeautifulSoup(fp, 'xml')
#    truth = pf.Article()
#    truth.title = "Sample title with searchable keywords such as photons!"
#    truth.authors = ["Matthew Kirby", "Tom McClintock"]
#    truth.abstract = "Something, something positrons."
#    truth.link = "http://arxiv.org"
#    assert truth == load_article(soup)
#    return

def test_load_all_articles():
    with open("test_call.txt") as fp:
        soup = BeautifulSoup(fp, 'xml')
    truth = pf.Article()
    truth.title = "Sample title with searchable keywords such as photons!"
    truth.authors = ["Matthew Kirby", "Tom McClintock"]
    truth.abstract = "Something, something positrons."
    truth.link = "http://arxiv.org"
    truth2 = pf.Article()
    truth2.title = "Hi there!"
    truth2.authors = ["Erika Wagoner"]
    truth2.abstract = "In a couple words"
    truth2.link = "http://arxiv.org/isitnotanumberusually"
    article_list = [truth, truth2]
    assert article_list == pf.load_all_articles(soup)
    return






