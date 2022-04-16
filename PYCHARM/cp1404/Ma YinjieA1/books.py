


def load_csv(filename):
    books = []
    for line in open(filename).readlines():
        line = line.strip()
        sp = line.split(',')
        book = [sp[0].strip(), sp[1].strip(), int(sp[2].strip()), sp[3].strip()]
        books.append(book)
    print(len(books), 'books loaded')
    return books

def save_csv(books, filename):
    fp = open(filename, 'w')
    for book in books:
        fp.write('%s,%s,%d,%s\n' % (book[0], book[1], book[2], book[3]))
    fp.close()
    print(len(books), 'books saved to', filename)

def show_menu():
    print('Menu:')
    print('L - List all books')
    print('A - Add new book')
    print('M - Mark a book as completed')
    print('Q - Quit')

def list_books(books):
    bs = 0
    pages = 0
    for i in range(len(books)):
        book = books[i]
        s = ''
        if book[3] == 'c':
            s += ' '
        else:
            s += '*'
            bs += 1
        s += '%d. ' % (i + 1)
        s += '%-40s' % book[0]
        s += '%-25s' % book[1]
        s += '%3d pages' % book[2]
        if book[3] != 'c':
            pages += book[2]
        print(s)
    print('You need to read %d pages in %d books.' % (pages, bs))

def get_title_input():
    while True:
        title = input('Title: ').strip()
        if len(title) == 0:
            print('Input can not be blank')
        else:
            return title

def get_author_input():
    while True:
        author = input('Author: ').strip()
        if len(author) == 0:
            print('Input can not be blank')
        else:
            return author

def get_pages_input():
    while True:
        pages = input('Pages: ').strip()
        if len(pages) == 0:
            print('Invalid input; enter a valid number')
            continue
        try:
            page = int(pages)
            if page > 0:
                return page
            else:
                print('Number must be > 0')
                continue
        except:
            print('Invalid input; enter a valid number')
            continue

def get_index_number_input(books):
    while True:
        number = input('Enter the number of a book to mark as completed\n>>> ').strip()
        if len(number) == 0:
            print('Invalid input; enter a valid number')
            continue
        try:
            number = int(number)
            if number <= 0:
                print('Number must be > 0')
                continue
            elif number > len(books):
                print('Invalid book number')
                continue
            else:
                return number
        except:
            print('Invalid input; enter a valid number')
            continue

def add_books(books):
    title = get_title_input()
    author = get_author_input()
    pages = get_pages_input()
    print('%s by %s, (%d pages) added to Reading Tracker' % (title, author, pages))
    books.append([title, author, pages, 'r'])

def all_marked(books):
    for book in books:
        if book[3] == 'r':
            return False
    return True

def mark_books(books):
    if all_marked(books):
        print('No required books')
        return
    list_books(books)
    index = get_index_number_input(books)
    if books[index - 1][3] == 'c':
        print('That book is already completed')
    else:
        books[index - 1][3] = 'c'
        print('%s by %s completed!' % (books[index - 1][0], books[index - 1][1]))

def main():
    print('Reading Tracker 1. 0 - by Lindsay Ward')
    books = load_csv('books.csv')
    while True:
        show_menu()
        cmd = input('>>> ').lower()
        if cmd == 'l':
            list_books(books)
        elif cmd == 'a':
            add_books(books)
        elif cmd == 'm':
            mark_books(books)
        elif cmd == 'q':
            break
        else:
            print('Invalid menu choice')
    save_csv(books, 'books.csv')
    print('So many books, so little time. Frank Zappa')

main()