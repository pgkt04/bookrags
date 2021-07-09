from enum import Enum

WEBSITE_URL = "http://www.bookrags.com/"
SESSION_URL = "http://www.bookrags.com/questions/topics/popular"
LOGIN_URL = "https://www.bookrags.com/qa/login.php?step=submit"
LOGOUT_URL = "http://www.bookrags.com/qa/logout.php"
ACCOUNT_URL = 'https://www.bookrags.com/my-account/'


class ProductType(Enum):
    UNKNOWN = 0
    STUDY_GUIDE = 1
    GALE = 2
    EBOOK = 3
    BIOGRAPHY = 4
    ESSAY = 5
    NOTE = 6
    LESSON_PLAN = 7


PRODTYPES = {
    'lp': ProductType.LESSON_PLAN
}
