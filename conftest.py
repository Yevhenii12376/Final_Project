from playwright.sync_api import sync_playwright
from pytest import fixture

from Final_Project.pageObject.makeupPageObject import MakeUp
@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def desktop_makeup (get_playwright):
    makeup = MakeUp(get_playwright)
    yield makeup
    makeup.close()