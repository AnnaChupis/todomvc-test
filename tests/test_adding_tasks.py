from selene import have
from selene.support.shared import browser


def test_active_completed():
    browser.open('http://todomvc.com/examples/emberjs/')
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.elements('#todo-list li').should(have.exact_texts('a','b','c'))

    browser.element('li:nth-of-type(2) .toggle').click()
    browser.element('#todo-count').should(have.exact_text('2 items left'))
    browser.element('#todo-list li:nth-of-type(2)').should(have.css_class('completed'))
    browser.element('#todo-list li:nth-of-type(1)').should(have.no.css_class('completed'))
    browser.element('#todo-list li:nth-of-type(3)').should(have.no.css_class('completed'))