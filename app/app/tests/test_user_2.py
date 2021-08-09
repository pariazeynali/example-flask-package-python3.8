import json
import unittest.mock
# noinspection PyUnresolvedReferences
import pytest

from flask import Response

from data import users
from tests.test_client import flask_app, client

test_app = flask_app.test_client()


# def test_example():
#     print("test example ...")
#     assert 2 + 1 == 3


def test_register_validation_when_valid(client):
    data ={
        "username": "user2",
        "password": "1234"
    }

    target = 'services/user_services/find_user_by_username'
    find_user = unittest.mock.patch(target, return_value=None)
    target = 'services/user_services/create_user'
    create_user = unittest.mock.patch(target, return_value=users.UserModel())
    request = flask_app.test_request_context(path='/register', data=data)

    with find_user, create_user, request:
        response: Response = test_app.post('/register', headers={"Content-Type": "application/json"}, data=data)

    assert response.status_code == 201
