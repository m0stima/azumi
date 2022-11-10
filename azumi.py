import os

def banner():
    text = r"""
    /\                        (_)
   /  \    _____   _ _ __ ___  _
  / /\ \  |_  / | | | '_ ` _ \| |
 / ____ \  / /| |_| | | | | | | |
/_/    \_\/___|\__,_|_| |_| |_|_|
---------------------------------
   A simple text file scanner.
---------------------------------
https://twitter.com/_m0stima_
https://github.com/m0stima/azumi
    """
    print(text)

def show_menu(options):
    print()
    print('Select if you want to scan a single file or files within a directory:')
    for k in sorted(options):
        print(f' {k}) {options[k][0]}')


def read_option(options):
    while (a := input('\nOption: ')) not in options:
        print('Not an option.\n')
    return a


def exec_option(option, options):
    options[option][1]()


def gen_menu(options, option_out):
    option = None
    while option != option_out:
        show_menu(options)
        option = read_option(options)
        exec_option(option, options)
        print(2 * "\n")


def main_menu():
    global keyword 
    keyword = input('Enter the keyword: ')
    options = {
        '1': ('Text file', txt_scan),
        '2': ('Text files within directory', dir_scan),
        '3': ('Change keyword', chg_keyword),
        '4': ('Exit', exit_scan)
    }
    gen_menu(options, '4')


def txt_scan():
    i = 0
    if (file := input('\nEnter text file (full path): ')).endswith(('.txt','.log')):
        print()
        f = open(file, encoding="utf8")
        for l_no, line in enumerate(f):
            if keyword in line:
                i += 1
                print('[', i, ']')
                print('File: ', file)
                print('Line Number: ', l_no)
                print('Content: ', line)
        print('\nTotal results: ', i)
        print('Keyword: ', keyword)
    else:
        print('\nNot a valid file.')


def dir_scan():
    i = 0
    j = 0
    dir = input('\nEnter the directory where the text files are: ')
    if (os.path.isdir(dir)) == True:
        for file in os.listdir(dir):
            if (file.endswith(('.txt','.log'))):
                j += 1
                with open(os.path.join(dir, file), encoding="utf8") as f:
                    for l_no, line in enumerate(f):
                        if keyword in line:
                            print('[', i, ']')
                            i += 1
                            print('File: ', file)
                            print('Line Number: ', l_no)
                            print('Content: ', line)
    else:
        print('\nNot a directory.')
    
    print('\nTotal results: ', i)
    print('Files searched: ', j)
    print('Keyword: ', keyword)


def chg_keyword():
    global keyword 
    keyword = input('\nEnter the new keyword: ')


def exit_scan():
    print('\nExiting...')


if __name__ == '__main__': 
    banner()
    main_menu()

