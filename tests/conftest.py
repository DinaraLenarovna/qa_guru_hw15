import pytest
from selene import browser


@pytest.fixture(scope="function", params=[(1920, 1080), (2560, 1440), (1440, 1080)],
                ids=("FHD", "QHD", "HDV 1080i"))
def browser_management_desktop(request):
    browser.config.base_url = 'https://github.com/'
    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width

    yield
    browser.quit()


@pytest.fixture(scope="function", params=[(390, 844), (412, 915), (360, 740)],
                ids=("iPhone 12 Pro", "Pixel 7", "Samsung Galaxy S8+"))
def browser_management_mobile(request):
    browser.config.base_url = 'https://github.com/'
    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width


    yield
    browser.quit()


@pytest.fixture(scope="function", params=[(1920, 1080), (2560, 1440), (390, 844), (412, 915)],
                ids=("FHD", "QHD", "iPhone 12 Pro", "Pixel 7"))
def browser_management(request):
    browser.config.base_url = 'https://github.com/'
    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width

    if width >= 800:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()