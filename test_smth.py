from selene import browser, be, have

def test_google_search_(browser_config):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Об этой странице'))

def test_google_search_unsuccessful(browser_config):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('fffnslagnrvam;erirvhnf nrejw;').press_enter()
    browser.element('html').should(have.text('Похоже, по вашему запросу нет полезных результатов'))