import re

from requests.sessions import Session


class Lens:
    """
    Special product type that contains references to all resources
    """

    def __init__(self, session: Session, link: str):
        self.__session = session
        self.__link = link

    def get_title(self):
        page_text = self.__session.get(self.__link).text
        page_title = re.search('<title>(.*?)</title>', page_text).group(1)
        return page_title

    def get_study_pack(self):
        """
        Returns all the pages for a study pack
        """
        page_text = self.__session.get(self.__link).text

        study_block = re.search(('<!-- BEGIN STUDY GUIDE BLOCK -->'
                                '(.*?)<!-- BEGIN STUDY GUIDE BLOCK -->'),
                                page_text)
        print(study_block)

    def get_studypack(self):
        """
        Returns all the links in the studypack
        """
        pass

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
