from Driver.WebElementHelper import WebElementHelper
from Utils.logger import Logger

class SearchResults(object):
    def __init__(self, brw):
        self._web = WebElementHelper(brw)

    def get_found_books(self, book):
        _xpath = "//*[@class='tab search']//*[@class='book-item']//*[@alt='{}']".format(book)
        Logger.write_to_console(_xpath)
        _books = self._web.get_web_elements_by_xpath(_xpath)
        if len(_books) > 0:
            return True
        else:
            return False