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
        self._session = requests.Session()
        self._setup_cookies()
        self._login()

    def _setup_cookies(self):
        """
        Not required
        """
        self._session.cookies['layout'] = 'desktop'
        self._session.get(Urls.WEBSITE_URL)
        self._session.get(Urls.SESSION_URL)

    def _login(self):
        """
        Authenticates the current session using the given details
        """
        self._session.post(
            Urls.LOGIN_URL,
            data=self.__details)

    def is_logged_in(self):
        """
        Checks if the current session is signed in
        """
        check = self._session.get(
            Urls.ACCOUNT_URL,
            allow_redirects=False).text

        return len(check) > 0

    def get_session(self):
        return self._session

    def logout(self):
        """
        Signs out of the user account from the active session
        """
        self._session.get(Urls.LOGOUT_URL)

    def resolve_type(self, link: str):
        """
        Given a link, it will return the ProductType
        """
        if not re.search('bookrags.com', link):
            return ProductType.UNKNOWN
        try:
            page = self._session.get(link).text
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

        return Product(self._session, link, type)

    def resolve_study_plan(self, link: str):
        """
        Given a link, it will resolve it into the study guide page and return a Lens instance
        """
        type = self.resolve_type(link)

        if type == ProductType.UNKNOWN:
            return None

        if type == ProductType.LENS:
            return Lens(self._session, link)

        page = self._session.get(link).text

        study_guide = re.search("href=\'(.*?)\'", re.search(
            '<div id=\'contentSPUpsellBlock\'>(.*?)</div>', page, flags=re.DOTALL
        ).group()).group(1)

        return Lens(self._session, study_guide)

    def search(self, query: str):
        """
        Perform a search query and return the results
        """
        pass
