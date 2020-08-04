from django.test import TestCase
from user import models as usr

class UserTestCase(TestCase):
    def setUp(self):
        usr.User.objects.create(first_name="Lionel",
                                last_name="Lenoil",
                                password="123",
                                status=1)
        usr.User.objects.create(first_name="Catherine",
                                last_name = "Enirehtac",
                                password="456",
                                status=0)

    def test_users_are_users(self):
        """User are correctly identified"""
        lionel = usr.User.objects.get(first_name="Lionel",
                                last_name="Lenoil",
                                password="123",
                                status=1)
        catherine = usr.User.objects.get(first_name="Catherine",
                                last_name="Enirehtac",
                                password="456",
                                status=0)
        self.assertEqual("Bla", "Bla")

# if __name__ == '__main__':
#    unittest.main()
