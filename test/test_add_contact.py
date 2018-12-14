# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_add_new_contact_page()
    app.contact.fill_in_contact_form(Contact(firstname='First name', middlename='Middlename', lastname='Lastname'))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_add_new_contact_page()
    app.contact.fill_in_contact_form(Contact(firstname='', middlename='', lastname=''))
    app.session.logout()


