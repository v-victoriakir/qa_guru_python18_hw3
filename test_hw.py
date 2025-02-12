from selene import browser, be, have


def test_google_search_(browser_actions):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Selene: User-Oriented Web UI Browser Tests in Python'))


def test_google_search_unsuccessful(browser_actions):
    browser.element('[name="q"]').should(be.blank).type('автокпмифмдфцлшомт ырв334').press_enter()
    browser.element('html').should(have.text('результаты не найдены'))
