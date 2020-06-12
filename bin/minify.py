
import requests
import json
import prettytable
import sys
import argparse

def parse_arguments():
    argparser = argparse.ArgumentParser(description='minify')

    argparser.add_argument('-a', '--add', help='dodaj link', action='store_true')
    # nargs="+" znaci da ocekuje vise inputa
    argparser.add_argument('-u', '--url', help='url', default='')
    argparser.add_argument('-l', '--list', help='show urls', action='store_true')

    r = argparser.parse_args()
    # Da se lista stringova spoji u jedan
    if not r.add and not r.list:
        argparser.print_help()
        sys.exit()

    return r


def add_url(url):
    res = requests.put(f'http://localhost:8802/api/shorten-url', data={
        'url': str(url)
    })
    if res.status_code == 200:
        res = json.loads(res.text)
        print('Response: ', res)

    else:
        res = json.loads(res.text)
        print('error:', res)


def main():
    p = parse_arguments()

    if p.add:
        if not p.url:
            print("All fields are required! -u (--url)")
            return

        add_url(p.url)

if __name__ == "__main__":
    main()
































