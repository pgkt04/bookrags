import re

class Book:
    def __init__(self) -> None:
        pass

    def get_title(self, link):
        page_text = self.__session.get(link).text
        page_title = re.search('<title>(.*?)</title>', page_text).group(1)
        return page_title

    def get_study_pack(self, link):
        """
        Returns all the pages for a study pack
        """
        page_text = self.__session.get(link)
        re.search(('<!-- BEGIN STUDY GUIDE BLOCK -->'
                '(.*?)<!-- BEGIN STUDY GUIDE BLOCK -->'),
                page_text)
