import re
from bookrags.definitions import ProductType


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

    def get_pdf(self):
        """
        Gets the pdf down link
        """
        pass

    def get_docx(self):
        """
        Get the word download link
        """
        pass
