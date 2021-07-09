import requests
from bookrags import urls
from bookrags.book import Book
from bookrags.lens import Lens

# Automatically navigate to the study guide page
# Query what pages there are


class BookRags:

    def __init__(self, username, password) -> None:
        self.__details = {
            'edEmailOrName': username,
            'edPW': password
        }
        self.__session = requests.Session()
        self.__login()

    def __login(self):
        self.__session.post(
            urls.LOGIN_URL,
            data=self.__details)

    def is_logged_in(self):
        check = self.__session.get(
            urls.ACCOUNT_URL,
            allow_redirects=False)
        return len(check.text) > 1

    def logout(self):
        """
        Signs out of the user account from the active session
        """
        self.__session.get(urls.LOGOUT_URL)

    def search(self, query):
        """
        Perform a search query and return the results
        """
        pass
