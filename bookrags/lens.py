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

    def get_link(self):
        return self._link

    def get_title(self):
        page_title = re.search('<title>(.*?)</title>', self._content)
        return page_title

    def get_study_pack(self):
        """
        Returns all the pages for a study pack
        wait i just realised how fucking stupid this function is LOL
        """
        pass

    def get_study_guides(self) -> List[Product]:
        """
        Return all study guide Product objects
        """
        ret = []
        get_sg = '<!-- BEGIN STUDY GUIDE BLOCK -->(.*?)<!-- END STUDY GUIDE BLOCK -->'
        study_guides_raw = re.search(get_sg, self._content, flags=re.DOTALL)

        if not study_guides_raw:
            return ret

        study_guides = re.findall("href='(.*?)'", study_guides_raw.group())

        for i in study_guides:
            type = resolve_type(self._session, i)
            if is_product(type):
                ret.append(Product(self._session, i, type))

        return ret

    def get_encyclopedias(self) -> List[Product]:
        """
        Return all encyclopedia / gale links
        """
        ret = []
        get_enc = '<!-- BEGIN ENCYCLOPEDIA BLOCK -->(.*?)<!-- END ENCYCLOPEDIA BLOCK -->'
        study_guides_raw = re.search(get_enc, self._content, flags=re.DOTALL)

        if not study_guides_raw:
            return ret

        study_guides = re.findall("href='(.*?)'", study_guides_raw.group())
        existing = {}

        for i in study_guides:
            if i not in existing:
                existing[i] = True
            else:
                continue

            type = resolve_type(self._session, i)
            if is_product(type):
                ret.append(Product(self._session, i, type))

        return ret

    def get_biographies(self) -> List[Product]:
        """
        Get all biography linkes
        """
        pass

    def get_essays(self):
        """
        Get all essay links
        """
        pass

    def get_notes(self):
        """
        Get all note links
        Not supported, they are included in the study guide
        """
        pass
