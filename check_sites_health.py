import sys
import datetime
import urllib.parse
import whois
import requests


def load_urls4check(path):
    with open(path) as file_handler:
        return file_handler.read().splitlines()


def is_server_respond_with_ok(url):
    try:
        response = requests.head(url, timeout=1)
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return False
    return response.ok


def get_domain_expiration_date(url):
    domain = urllib.parse.urlsplit(url).hostname
    exp_date = whois.whois(domain).expiration_date
    return exp_date[0] if type(exp_date) is list else exp_date


def is_expire_in(interval, exp_date):
    return exp_date.date() < (
        datetime.date.today() + datetime.timedelta(days=interval)
        )

if __name__ == '__main__':
    try:
        urls = load_urls4check(sys.argv[1])
    except IndexError:
        exit('Please specify path to URL list')
    except FileNotFoundError:
        exit('File not found')
    interval = 30
    print('Alive Expire  URL')
    for url in urls:
        if is_server_respond_with_ok(url):
            print('{1!s:6} {0!s:6} {2}'.format(
                is_expire_in(interval, get_domain_expiration_date(url)),
                True, url)
            )
        else:
            print('Failed to establish connection to {}'.format(url))
