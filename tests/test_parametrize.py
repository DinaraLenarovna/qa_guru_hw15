"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, be

desktop_only = pytest.mark.parametrize("browser_management",
                                       [(1920, 1080), (2560, 1440)], indirect=True,
                                       ids=["FHD", "QHD"])
mobile_only = pytest.mark.parametrize("browser_management",
                                      [(390, 844), (412, 915)], indirect=True,
                                      ids=["iPhone 12 Pro", "Pixel 7"])


@desktop_only
def test_github_desktop(browser_management):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)


@mobile_only
def test_github_mobile(browser_management):
    browser.open('/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)