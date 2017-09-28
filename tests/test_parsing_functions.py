import numpy as np
import sys
sys.path.insert(0,'../')
import parsing_functions as pf
from bs4 import BeautifulSoup
import pytest


def test_load_title():
    with open("test_call.txt") as fp:
        soup = BeautifulSoup(fp, 'xml')
    title = pf.load_title(soup.entry)
    assert title == "Sample title with searchable keywords such as photons!"
    return

def test_load_authors():
    with open("test_call.txt") as fp:
        soup = BeautifulSoup(fp, 'xml')
    author_list = pf.load_authors(soup.entry)
    assert author_list == ["Matthew Kirby", "Tom McClintock"]
    return

def test_load_abstract():
    with open("test_call.txt") as fp:
        soup = BeautifulSoup(fp, 'xml')
    abstract = pf.load_abstract(soup.entry)
    assert abstract == "Something, something positrons."
    return

def test_load_link():
    with open("test_call.txt") as fp:
        soup = BeautifulSoup(fp, 'xml')
    link = pf.load_link(soup.entry)
    assert link == "http://arxiv.org"
    return


