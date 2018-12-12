# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.open_add_new_contact_page()
    app.fill_in_contact_form(Contact(firstname='First name', middlename='Middlename', lastname='Lastname'))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.open_add_new_contact_page()
    app.fill_in_contact_form(Contact(firstname='', middlename='', lastname=''))
    app.session.logout()


