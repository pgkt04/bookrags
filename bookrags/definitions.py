from enum import Enum


class Urls:
    WEBSITE_URL = "http://www.bookrags.com/"
    SESSION_URL = "http://www.bookrags.com/questions/topics/popular"
    LOGIN_URL = "https://www.bookrags.com/qa/login.php?step=submit"
    LOGOUT_URL = "http://www.bookrags.com/qa/logout.php"
    ACCOUNT_URL = 'https://www.bookrags.com/my-account/'


class ProductType(Enum):
    UNKNOWN = 0
    STUDY_GUIDE = 1
    ENCYCLOPEDIA = 2
    EBOOK = 3
    BIOGRAPHY = 4
    ESSAY = 5
    LESSON_PLAN = 7,
    LENS = 8


CONVERT_TYPE = {
    'lens': ProductType.LENS,
    'lp': ProductType.LESSON_PLAN,
    'guides': ProductType.STUDY_GUIDE,
    'gale': ProductType.ENCYCLOPEDIA,
    'ebooks': ProductType.EBOOK,
    'bios': ProductType.BIOGRAPHY,
    'litcrit': ProductType.ESSAY
}

