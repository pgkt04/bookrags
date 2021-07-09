import re
from requests import Session
from bookrags.definitions import ProductType


class Product:
    def __init__(self, session: Session, link: str, type: ProductType):
        self.__link = link
        self.__session = session
        self.__type = type

    def get_link(self):
        return self.__link

    def get_type(self):
        return self.__type

    def get_pdf(self):
        """
        Gets the pdf down link
        """
        page_code = self.__session.get(self.__link).text
        link = re.search('http.*?mode=pdf', page_code).group()
        download = self.__session.get(
            link, allow_redirects=False).headers['location']
        return download

    def get_docx(self):
        """
        Get the word download link
        """
        page_code = self.__session.get(self.__link).text
        link = re.search('http.*?mode=doc', page_code).group()
        download = self.__session.get(
            link, allow_redirects=False).headers['location']
        return download

    def get_print(self):
        """
        Get the print
        """
        page_code = self.__session.get(self.__link).text
        link = re.search('http.*?mode=print', page_code).group()
        return link
