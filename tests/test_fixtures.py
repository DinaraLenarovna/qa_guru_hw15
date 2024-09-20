from selene import browser, be

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


def test_github_desktop(browser_management_desktop):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)


def test_github_mobile(browser_management_mobile):
    browser.open('/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)
