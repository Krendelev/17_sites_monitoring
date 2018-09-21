import sys
import datetime
import urllib.parse
import whois
import requests


def load_urls4check(path):
    with open(path) as file_handler:
        return file_handler.read().splitlines()


def is_server_respond_with_200(url):
    return requests.head(url).ok


def get_domain_expiration_date(url):
    domain = urllib.parse.urlsplit(url).hostname
    return whois.query(domain).expiration_date


def is_expire_soon(exp_date):
    soon = 30
    return exp_date.date() < (
        datetime.date.today() + datetime.timedelta(days=soon)
        )

if __name__ == '__main__':
    try:
        urls = load_urls4check(sys.argv[1])
    except IndexError:
        exit('Please specify path to URL list')
    except FileNotFoundError:
        exit('File not found')
    print('Alive Expire  URL')
    for url in urls:
        print('{0!s:6} {1!s:6} {2}'.format(
            is_server_respond_with_200(url),
            is_expire_soon(get_domain_expiration_date(url)),
            url)
        )
