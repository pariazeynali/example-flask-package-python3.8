from unittest import TestCase
from app import app
from data.users import UserModel
from flask_security.utils import login_user

class UserTest(TestCase):
   def setUp(self):
       self.app = app
       self.client = self.app.test_client()
       self._ctx = self.app.test_request_context()
       self._ctx.push()

       db.create_all()

   def tearDown(self):
       if self._ctx is not None:
           self._ctx.pop()

       db.session.remove()
       db.drop_all()

   def test_user_authentication():
       # (the test case is within a test request context)
       user = UserModel
       db.session.add(user)
       db.session.commit()
       login_user(user)

       # current_user here is the user
       print(current_user)

       # current_user within this request is an anonymous user
       r = test_client.get('/user')