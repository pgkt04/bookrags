import re
from requests import Session
from bookrags.definitions import ProductType


class Product:
    def __init__(self, session: Session, link: str, type: ProductType):
        self._link = link
        self._session = session
        self._type = type
        self._content = self._session.get(self._link).text

    def get_link(self):
        return self._link

    def get_type(self):
        return self._type

    def get_pdf(self):
        """
        Gets the pdf down link
        """
        link = re.search('http.*?mode=pdf', self._content).group()
        download = self._session.get(
            link, allow_redirects=False).headers['location']
        return download

    def get_docx(self):
        """
        Get the word download link
        """
        page_code = self._session.get(self._link).text
        link = re.search('http.*?mode=doc', page_code).group()
        download = self._session.get(
            link, allow_redirects=False).headers['location']
        return download

    def get_print(self):
        """
        Get the print
        """
        page_code = self._session.get(self._link).text
        link = re.search('http.*?mode=print', page_code).group()
        return link
