import pytest
from selene import browser, be, have

@pytest.fixture(scope="session")
def browser_settings():
    browser.config.base_url = 'https://google.com'
    browser.driver.set_window_size(1920,1080)
    yield
    browser.config.timeout = 9000.0
    browser.quit()
    print("Закрываем браузер")

def test_positive(browser_settings):
    browser.open('/')
    button = browser.element('#L2AGLb')
    if button.should(be.visible):
        button.click()
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_negative(browser_settings):
    browser.open('/')
    button = browser.element('#L2AGLb')
    if button.should(be.visible):
        button.click()
    browser.element('[name="q"]').should(be.blank).type('qds1та!дщasdi@#%').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу qds1та!дщasdi@#% ничего не найдено.'))