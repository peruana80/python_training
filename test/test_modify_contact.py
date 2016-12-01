from model.contact import Contact
from random import randrange


def test_modify_contact_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="Zmodyfikuj imie", middle_name="Zmodyfikuj drugie imie", last_name="Zmodyfikuj nazwisko", nickname="Zmodyfikuj ksywe", title="Zmodyfikuj tytul",
                                        company="Zmodyfikuj firme", address="Zmodyfikuj adres", home_number="Zmodyfikuj_telefon_domowy", mobile_number="Zmodyfikuj_telefon_komorkowy",
                                        work_number="Zmodyfikuj_telefon_sluzbowy", fax="Zmodyfikuj fax", email="Zmodyfikuj email", email2="Zmodyfikuj email2", email3="Zmodyfikuj email3",
                                        homepage="Zmodyfikuj strone domowa", byear="1990", ayear="2000", address_2="Zmodyfikuj drugi adres", phone2="Zmodyfikuj_telefon domowy 2",
                                       notes="Zmodyfikuj notatki")
    contact.id=old_contacts[index].id
    app.contact.modify_contact_by_id(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = app.contact.get_contact_list()
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_first_contact_first_name(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(first_name="zmodyfikuj imie"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_first_contact_email(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(last_name="Zmodyfikuj nazwisko"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)