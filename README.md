# Sites Monitoring Utility

Check whether site is alive and its domain will not expire soon.

## How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

## Quick Start

Pass `text` file with URLs as argument.

```bash
$ python check_sites_health.py urls.txt
Alive Expire  URL
True   False  https://www.python.org
True   False  https://devman.org
False  False  http://melevir.com
False  N/A    https://xgithubx.com
```

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
