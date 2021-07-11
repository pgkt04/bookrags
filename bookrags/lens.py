import re
from requests.sessions import Session


class Lens:
    """
    Special product type that contains references to all resources
    """

    def __init__(self, session: Session, link: str):
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
        ret = []
        get_study_block = ('<!-- BEGIN STUDY PACK BLOCK -->'
                           '(.*?)<!-- END STUDY PACK BLOCK -->')

        study_block = re.search(
            get_study_block, self._content, flags=re.DOTALL)

        if not study_block:
            print('study block not found')
            return ret

        print(study_block.group())

    def get_study_guides(self):
        """
        Return all study guide links
        """
        pass

    def get_encyclopedias(self):
        """
        Return all encyclopedia / gale links
        """
        pass

    def get_biographies(self):
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
