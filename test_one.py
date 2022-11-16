from main import URLmethods

test_url = 'https://www.youtube.com/'
test_str = 'testtest'


def test_URLmethods():
    assert URLmethods(test_url) == {'GET': 200, 'HEAD': 200, 'POST': 400, 'PUT': 400}



