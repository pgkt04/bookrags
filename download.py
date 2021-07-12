import os
import re
import requests
from slugify import slugify
from bookrags.bookrags import BookRags


def extract_name(link):
    """
    Gets the file name given a download link
    """
    name = re.search('.*\/(.*pdf)', link).group(1)
    return name.group(1)


def main():
    instance = BookRags('username', 'password')

    if not instance.is_logged_in():
        print('Failed to log in')
        return

    link = input('Enter a link to download ')
    study_plan = instance.resolve_study_plan(link)

    if not study_plan:
        print('Invalid link')
        return

    print('What would you like to download?')
    print('1. All')
    print('2. Study Guides')
    print('3. Encyclopedia')
    print('4. Ebooks')
    print('5. Essays')
    print('6. Biographies')

    choice = input('> ')

    print('Preparing to download...')

    downloads = []

    if choice == '1':
        downloads.append(study_plan.get_study_pack())
    elif choice == '2':
        downloads.append(study_plan.get_study_guides())
    elif choice == '3':
        downloads.append(study_plan.get_encyclopedias())
    elif choice == '4':
        downloads.append(study_plan.get_ebooks())
    elif choice == '5':
        downloads.append(study_plan.get_essays())
    elif choice == '6':
        downloads.append(study_plan.get_biographies())
    else:
        print('Unknown choice - please try again...')
        return

    download_folder = slugify(study_plan.get_title())

    if not os.path.exist(download_folder):
        os.makedirs(download_folder)

    progress = 0
    for i in downloads:
        progress += 1
        file_name = extract_name(i.get_pdf())
        pdf_file = requests.get(i)
        with open(download_folder + '/' + file_name, 'wb') as fh:
            fh.write(pdf_file.content)
        print('Progress:', progress, '/', len(downloads))

    print('Done!')


if __name__ == '__main__':
    main()
