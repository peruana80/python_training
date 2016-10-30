# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(first_name="imie", middle_name="drugie imie", last_name="nazwisko", nickname="ksywa", title="tytul",
                               company="firma", address="adres", home_number="telefon domowy", mobile_number="telefon komorkowy",
                               work_number="telefon sluzbowy", fax="fax", email="email", email2="email2", email3="email3",
                               homepage="strona domowa", byear="1990", ayear="2000", address_2="drugi adres", phone2="dom",
                               notes="notatki"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)




def test_add_new_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(first_name="", middle_name="", last_name="", nickname="",
                               title="", company="", address="",
                               home_number="", mobile_number="",
                               work_number="", fax="", email="", email2="",
                               email3="", homepage="", byear="", ayear="",
                               address_2="", phone2="", notes=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
