from bookrags.definitions import ProductType, CONVERT_TYPE
from requests import Session
import json
import re


def is_product(type: ProductType):
    if type == ProductType.UNKNOWN or \
        type == ProductType.LESSON_PLAN or \
            type == ProductType.LENS:
        return False
    return True


def resolve_type(session: Session, link: str):
    """
    Given a link, it will return the ProductType
    """
    if not re.search('bookrags.com', link):
        return ProductType.UNKNOWN
    try:
        page = session.get(link).text
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
