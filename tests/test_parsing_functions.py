import numpy as np
import sys
sys.path.insert(0,'../')
import parsing_functions as pf
from bs4 import BeautifulSoup
import pytest

def test_load():
    with open("test_call.txt") as fp:
        soup = BeautifulSoup(fp)
    test_load_title(soup)
    test_load_authors(soup)
    test_load_abstract(soup)
    test_load_link(soup)
    return

@pytest.mark.skip
def test_load_title(soup):
    title = pf.load_title(soup)
    assert title == "Sample title with searchable keywords such as photons!"
    return

@pytest.mark.skip
def test_load_authors(soup):
    author_list = pf.load_authors(soup)
    assert author_list == ["Matthew Kirby", "Tom McClintock"]
    return

@pytest.mark.skip
def test_load_abstract(soup):
    abstract = pf.load_abstract(soup)
    assert abstract == "Something, something positions."
    return

@pytest.mark.skip
def test_load_link(soup):
    link = pf.load_link(soup)
    assert link == "http://arxiv.org"
    return
