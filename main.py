import requests
import validators


def validaterURL(link):
    validate = validators.url(link)
    if validate:
        return link
    else:
        print(f'Строка {link} не является ссылкой')


def URLmethods(url):
    check_code = {}
    check = requests.get(url)
    if check.status_code != 405:
        check_code['GET'] = check.status_code
    check = requests.head(url)
    if check.status_code != 405:
        check_code['HEAD'] = check.status_code
    check = requests.post(url)
    if check.status_code != 405:
        check_code['POST'] = check.status_code
    check = requests.put(url)
    if check.status_code != 405:
        check_code['PUT'] = check.status_code
    check = requests.delete(url)
    if check.status_code != 405:
        check_code['DELETE'] = check.status_code
    check = requests.options(url)
    if check.status_code != 405:
        check_code['OPTIONS'] = check.status_code
    check = requests.patch(url)
    if check.status_code != 405:
        check_code['PATCH'] = check.status_code
    return check_code


def list_url_search(link):
    result = {}
    for i in link:
        if validaterURL(i):
            result[i] = URLmethods(i)
    print(result)


if __name__ == "__main__":
    list_link = open('test\\test.txt').read().split('\n')
    list_url_search(list_link)
