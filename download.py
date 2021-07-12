import os
from slugify import slugify
from bookrags.bookrags import BookRags


def main():
    instance = BookRags('username', 'password')

    if not instance.is_logged_in():
        print('failed to log in')
        return

    link = input('enter a link to download ')
    study_plan = instance.resolve_study_plan(link)

    if not study_plan:
        print('invalid link')
        return

    print('what would you like to download?')
    print('1. All')
    print('2. Study Guides')
    print('3. Encyclopedia')
    print('4. Ebooks')
    print('5. Essays')
    print('6. Biographies')

    choice = input('> ')
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
    
    print('selected:')
    print(downloads)

if __name__ == "__main__":
    main()
