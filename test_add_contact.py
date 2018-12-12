# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from contact import Contact

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.login(username="admin", password="secret")
        self.open_add_new_contact_page()
        self.fill_in_contact_form(Contact(firstname='First name', middlename='Middlename', lastname='Lastname'))

    def test_add_empty_contact(self):
        wd = self.wd
        self.login(username="admin", password="secret")
        self.open_add_new_contact_page()
        self.fill_in_contact_form(Contact(firstname='', middlename='', lastname=''))

    def return_on_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def submit_contact_form(self):
        wd = self.wd
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def fill_in_contact_form(self, contact):
        wd = self.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        self.submit_contact_form()
        self.return_on_home_page()



    def open_add_new_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def login(self, username, password):
        wd = self.wd
        self.open_login_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_login_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
