import re
import json
import requests
from bookrags.definitions import Urls, ProductType, CONVERT_TYPE
from bookrags.product import Product
from bookrags.lens import Lens

# Automatically navigate to the study guide page
# Query what pages there are


class BookRags:
    """
    Interface class for communicating with the API
    """

    def __init__(self, username, password):
        self.__details = {
            'edEmailOrName': username,
            'edPW': password
        }
        self.__session = requests.Session()
        self.__setup_cookies()
        self.__login()

    def __setup_cookies(self):
        """
        Not required
        """
        self.__session.cookies['layout'] = 'desktop'
        self.__session.get(Urls.WEBSITE_URL)
        self.__session.get(Urls.SESSION_URL)

    def __login(self):
        """
        Authenticates the current session using the given details
        """
        self.__session.post(
            Urls.LOGIN_URL,
            data=self.__details)

    def is_logged_in(self):
        """
        Checks if the current session is signed in
        """
        check = self.__session.get(
            Urls.ACCOUNT_URL,
            allow_redirects=False).text

        return len(check) > 0

    def get_session(self):
        return self.__session

    def logout(self):
        """
        Signs out of the user account from the active session
        """
        self.__session.get(Urls.LOGOUT_URL)

    def resolve_type(self, link: str):
        """
        Given a link, it will return the ProductType
        """
        if not re.search('bookrags.com', link):
            return ProductType.UNKNOWN
        try:
            page = self.__session.get(link).text
            json_raw = re.search(
                '{.*?}', re.search('dataLayer.push\({"sku":.*?</script>',
                                   page).group()
            ).group()
            if not json_raw:
                return ProductType.UNKNOWN
            json_data = json.loads(json_raw)
            return CONVERT_TYPE[json_data['prodtype']]
        except:
            return ProductType.UNKNOWN

    def resolve_product(self, link: str):
        """
        Given a link, it will resolve into the product page
        """
        type = self.resolve_type(link)

        if type == ProductType.UNKNOWN or \
                type == ProductType.LESSON_PLAN or \
                type == ProductType.LENS:
            return None

        return Product(self.__session, link)


    def resolve_study_plan(self, link: str):
        """
        Given a link, it will resolve it into the study guide page and return a Lens instance
        """

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

    def search(self, query: str):
        """
        Perform a search query and return the results
        """
        pass
