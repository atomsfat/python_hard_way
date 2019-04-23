from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()


def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Une forma", rv.data)

    data = {'name': 'Tomas', 'greet': 'Hola'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert_in(b"Tomas", rv.data)
    assert_in(b"Hola", rv.data)
