import requests
import re

# Automatically navigate to the study guide page
# Query what pages there are


class BookRags:

    WEBSITE_URL = "http://www.bookrags.com/"
    SESSION_URL = "http://www.bookrags.com/questions/topics/popular"
    LOGIN_URL = "https://www.bookrags.com/qa/login.php?step=submit"
    LOGOUT_URL = "http://www.bookrags.com/qa/logout.php"
    ACCOUNT_URL = 'https://www.bookrags.com/my-account/'

    def __init__(self, username, password) -> None:
        self.__details = {
            'edEmailOrName': username,
            'edPW': password
        }
        self.__session = requests.Session()
        self.__login()

    def __login(self):
        ret = self.__session.post(
            self.LOGIN_URL,
            data=self.__details)

    def is_logged_in(self):
        check = self.__session.get(
            self.ACCOUNT_URL,
            allow_redirects=False)
        return len(check.text) > 1

    def logout(self):
        self.__session.get(self.LOGOUT_URL)

    def get_title(self, link):
        page_text = self.__session.get(link).text
        page_title = re.search('<title>(.*?)</title>', page_text).group(1)
        return page_title

    def get_study_pack(self, link):
        page_text = self.__session.get(link)
        # Regex:
        # <!-- BEGIN STUDY GUIDE BLOCK -->
        # <!-- END STUDY PACK BLOCK -->
        re.search('', page_text)

    def get_essays(self, link):
        """
        Fetch all download links for a given essa
        """
        page_text = self.__session.get(link)
        re.search('', page_text)
