from selene import have
from selene.support.shared import browser


def test_active_completed():
    browser.open('http://todomvc.com/examples/emberjs/')

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.elements('#todo-list li').should(have.exact_texts('a','b','c'))

    browser.element('li:nth-of-type(2) .toggle').click()
    browser.all('#todo-list li.completed').should(have.exact_texts('b'))
    browser.all('#todo-list li:not(.completed)').should(have.exact_texts('a','c'))
