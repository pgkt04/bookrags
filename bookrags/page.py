import re


class Page:
    def __init__(self, link) -> None:
        self.__link = link

    def get_link(self):
        return self.__link

    def set_link(self, link):
        self.__link = link

    def get_pdf(self, link):
        """
        Gets the pdf link from the page
        """
        pass

    def get_word(self, link):
        """
        Get the word link from the page
        """
        pass
