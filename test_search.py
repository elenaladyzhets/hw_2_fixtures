import pytest
from selene import browser, be, have

def test_successful_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('html').should(have.text('Places'))

def test_unsuccessful_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('fghutgufhdjghdf54474!').press_enter()
    browser.element('html').should(have.text('did not match any documents'))