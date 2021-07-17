import os
import re
import requests
from slugify import slugify
from bookrags.bookrags import BookRags


def extract_name(link):
    """
    Gets the file name given a download link
    """
    return re.search('.*\/(.*pdf)', link).group(1)


def main():
    instance = BookRags('username', 'password')

    if not instance.is_logged_in():
        print('Failed to log in')
        return

    link = input('Enter a link to download: ')
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
        downloads.extend(study_plan.get_study_pack())
    elif choice == '2':
        downloads.extend(study_plan.get_study_guides())
    elif choice == '3':
        downloads.extend(study_plan.get_encyclopedias())
    elif choice == '4':
        downloads.extend(study_plan.get_ebooks())
    elif choice == '5':
        downloads.extend(study_plan.get_essays())
    elif choice == '6':
        downloads.extend(study_plan.get_biographies())
    else:
        print('Unknown choice - please try again...')
        return

    if len(downloads) < 1:
        print('No content found!')
        return

    download_folder = slugify(study_plan.get_title())

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    progress = 0
    for i in downloads:
        progress += 1
        pdf_link = i.get_pdf()
        if pdf_link:
            file_name = extract_name(pdf_link)
            download_path = download_folder + '/' + file_name
            if not os.path.exists(download_path):
                pdf_file = requests.get(pdf_link)
                with open(download_path, 'wb') as fh:
                    fh.write(pdf_file.content)
                print('Progress:', progress, '/', len(downloads))
            else:
                print(file_name, 'already exists, skipping...')
        else:
            print('PDF link broken! skipping...')

    print('Done!')


if __name__ == '__main__':
    main()
