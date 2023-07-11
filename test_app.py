from question5 import app
import json

def test_get():
    with app.test_client() as client:

        response = client.get('/')
        assert response.status_code == 200
        assert response.get_data() == b'"Hello world"\n'

def test_post():
    with app.test_client() as client:
        response = client.post('/posts', json={"username":"bharat@123", "id":5, "likes": 0, "comments":[], "caption":"hello"})

        assert response.status_code == 200
        assert response.get_data() == b'"data added successfully"\n'


def test_delete():
    with app.test_client() as client:
        response = client.delete('/delete/5')


        assert response.status_code == 200
        assert response.get_data() == b'"Item deleted successfully"\n'

