from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import *
import threading
from multiprocessing import Process


class ChargeTestCase(TestCase):
    def setUp(self):
        c = Client()
        self.users = []
        self.credits = []
        for i in range(45):
            new_user = User.objects.create(
                username=f"navid{str(i)}", password="1234")
            self.users.append(new_user)
            new_credit = Credit.objects.create(account_owner=new_user, value=250)
            self.credits.append(new_credit)

    def test_Response(self):
        client = Client()
        for user in self.users:
            response1 = self.client.get(f'/credit/getvalue/{user.id}/')
            response2 = self.client.get(f'/credit/chargecredit/{user.id}/')
            response3 = self.client.get(f'/credit/buy/{user.id}/')
            self.assertEqual(response1.status_code, 200)
            self.assertEqual(response2.status_code, 405)
            self.assertEqual(response3.status_code, 405)

    def test_charge_credit(self):
        c = Client()
        for user in self.users:
            c.post(f'/credit/chargecredit/{user.id}/', {'value': 220, 'account_owner': user})
            self.assertEqual(user.credit_set.get().value, 470)


    def test_buy_credit(self):
        c = Client()
        for user in self.users:
            c.post(f'/credit/buy/{user.id}/', {'value': 220, 'account_owner': user})
            self.assertEqual(user.credit_set.get().value, 30)

    def test_empty_buy_credit(self):
        c = Client()
        for user in self.users:
            c.post(f'/credit/buy/{user.id}/', {'value': 250, 'account_owner': user})
            self.assertEqual(user.credit_set.get().value, 0)

        for user in self.users:
            value = user.credit_set.get().value
            x = c.post(f'/credit/buy/{user.id}/', {'value': 250, 'account_owner': user})
            self.assertEqual(user.credit_set.get().value, value)


    def charge_for_user(self, user, value):
        c = Client()
        c.post(f'/credit/chargecredit/{user.id}/', {'value': value, 'account_owner': user})s