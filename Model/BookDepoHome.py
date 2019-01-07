from Driver.WebElementHelper import WebElementHelper

class BookDepoHome(object):
    __url = "https://www.bookdepository.com"

    def __init__(self, brw):
        self._web = WebElementHelper(brw)

    def open(self):
        self._web.open(self.__url)
    
    def enter_book_name(self, book):
        _searchFld = self._web.get_web_element_by_xpath('//*[@id="book-search-form"]//input[@name="searchTerm"]')
        _searchFld.click()
        _searchFld.send_keys(book)
    
    def search_book(self):
        self._web.get_web_element_by_xpath('//*[@id="book-search-form"]//button[@aria-label="Search"]').click()

    def close(self):
        self._web.close()