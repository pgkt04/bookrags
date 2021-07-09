import re
from enum import Enum


class ProductType(Enum):
    UNKNOWN = 0
    STUDY_GUIDE = 1
    GALE = 2
    EBOOK = 3
    BIOGRAPHY = 4
    ESSAY = 5
    NOTE = 6


class Product:
    def __init__(self, link) -> None:
        self.__link = link
        self.__type = ProductType.UNKNOWN

    def get_link(self):
        return self.__link

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

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
