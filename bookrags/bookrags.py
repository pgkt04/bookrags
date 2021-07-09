import re
import requests
from bookrags.definitions import Urls
from bookrags import product
from bookrags.lens import Lens
from bookrags.product import Product

# Automatically navigate to the study guide page
# Query what pages there are


class BookRags:
    """
    Interface class for communicating with the API
    """

    def __init__(self, username, password) -> None:
        self.__details = {
            'edEmailOrName': username,
            'edPW': password
        }
        self.__session = requests.Session()
        self.__login()

    def __login(self):
        """
        Authenticates the current session using the given details
        """
        self.__session.post(
            Urls.LOGOUT_URL,
            data=self.__details)

    def is_logged_in(self):
        """
        Checks if the current session is signed in
        """
        check = self.__session.get(
            Urls.ACCOUNT_URL,
            allow_redirects=False)
        return len(check.text) > 0

    def get_session(self):
        return self.__session

    def logout(self):
        """
        Signs out of the user account from the active session
        """
        self.__session.get(Urls.LOGOUT_URL)

    def resolve_type(self, link):
        """
        Given a link, it will return the product type
        """
        pass

    def resolve_product(self, link):
        """
        Given a link, it will resolve into the product page
        """
        pass

    def resolve_study_plan(self, link):
        """
        Given a link, it will resolve it into the study guide page
        """
        if not re.search('bookrags.com', link):
            print('bad link')
            return None

        print('link is valid')

        # read product type
        page = self.__session.get(link).text
        product_type = re.search('', page)

        # if we can't then this page isnt supported :c
        if not product_type:
            return None

        # we are already on the page
        if product_type == 'lens':
            return Lens()

        # visit page
        # read prodtype

    def search(self, query):
        """
        Perform a search query and return the results
        """
        pass
