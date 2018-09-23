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
        response = requests.head(url, allow_redirects=True, timeout=1)
        return response.ok
    except requests.RequestException:
        return False


def get_domain_expiration_date(url):
    domain = urllib.parse.urlsplit(url).hostname
    try:
        exp_date = whois.whois(domain).expiration_date
        return exp_date[0] if isinstance(exp_date, list) else exp_date
    except whois.parser.PywhoisError:
        return None


def is_expire_in(interval, exp_date):
    if not exp_date:
        return None
    return exp_date.date() < (
        datetime.date.today() + datetime.timedelta(days=interval)
        )


def print_status(url, is_alive, is_expire):
    is_alive = 'Yes' if is_alive else 'No'
    is_expire = 'N/A' if is_expire is None else 'Yes' if is_expire else 'No'
    print('{0:6} {1:6} {2}'.format(is_alive, is_expire, url))


if __name__ == '__main__':
    try:
        urls = set(load_urls4check(sys.argv[1]))
    except IndexError:
        exit('Please specify path to URL list')
    except FileNotFoundError:
        exit('File not found')
    interval = 30
    print('Alive Expire  URL')
    for url in urls:
        print_status(
            url, is_server_respond_with_ok(url),
            is_expire_in(interval, get_domain_expiration_date(url))
        )
