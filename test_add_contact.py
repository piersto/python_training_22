# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from contact import Contact
from application import Application


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.open_add_new_contact_page()
        self.app.fill_in_contact_form(Contact(firstname='First name', middlename='Middlename', lastname='Lastname'))

    def test_add_empty_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.open_add_new_contact_page()
        self.app.fill_in_contact_form(Contact(firstname='', middlename='', lastname=''))


    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
