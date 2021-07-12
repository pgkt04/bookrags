import re
from requests.sessions import Session
from bookrags.product import Product
from bookrags.helper import resolve_type, is_product
from typing import List


class Lens:
    """
    Special product type that contains references to all resources
    """

    def __init__(self, session: Session, link: str) -> None:
        self._session = session
        self._link = link
        self._content = session.get(link).text

    def get_link(self) -> str:
        return self._link

    def get_title(self) -> str:
        page_title = re.search('<title>(.*?)</title>', self._content)
        return page_title.group(1)

    def get_study_pack(self) -> List[Product]:
        """
        Returns all the pages for a study pack
        """
        ret = []
        ret.append(self.get_study_guides())
        ret.append(self.get_encyclopedias())
        ret.append(self.get_ebooks())
        ret.append(self.get_biographies())
        ret.append(self.get_essays())
        ret.append(self.get_notes())
        return ret

    def _extract_links(self, expression) -> List[Product]:
        ret = []
        block_code = re.search(expression, self._content, flags=re.DOTALL)
        if not block_code:
            return ret
        links = re.findall("href='(.*?)'", block_code.group())

        for i in links:
            type = resolve_type(self._session, i)
            if is_product(type):
                ret.append(Product(self._session, i, type))

        return ret

    def get_study_guides(self) -> List[Product]:
        """
        Return all study guide Product products
        """
        return self._extract_links(
            '<!-- BEGIN STUDY GUIDE BLOCK -->(.*?)<!-- END STUDY GUIDE BLOCK -->'
        )

    def get_encyclopedias(self) -> List[Product]:
        """
        Return all encyclopedia / gale products
        """
        return self._extract_links(
            '<!-- BEGIN ENCYCLOPEDIA BLOCK -->(.*?)<!-- END ENCYCLOPEDIA BLOCK -->'
        )

    def get_ebooks(self) -> List[Product]:
        """
        Get all ebook products
        """
        return self._extract_links(
            '<!-- BEGIN EBOOKS BLOCK -->(.*?)<!-- #topicEBooksBlock -->'
        )

    def get_biographies(self) -> List[Product]:
        """
        Get all biography products
        """
        self._extract_links(
            '<!-- BEGIN BIOGRAPHY BLOCK -->(.*?)<!-- END BIOGRAPHY BLOCK -->'
        )

    def get_essays(self) -> List[Product]:
        """
        Get all essay products
        """
        return self._extract_links(
            '<!-- BEGIN ESSAYS BLOCK -->(.*?)<!-- END ESSAYS BLOCK -->'
        )

    def get_notes(self) -> List[Product]:
        """
        Get all note links
        Not supported, they are included in the study guide
        """
        return self._extract_links(
            '<!-- BEGIN NOTES BLOCK -->(.*?)<!-- END NOTES BLOCK --'
        )
