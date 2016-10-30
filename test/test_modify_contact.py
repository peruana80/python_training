from model.contact import Contact

def test_modify_first_contact(app):
    if app.group.count() == 0:
        app.contact.create(Contact(first_name="test"))
    app.contact.modify_first_contact(Contact(first_name="Zmodyfikuj imie", middle_name="Zmodyfikuj drugie imie", last_name="Zmodyfikuj nazwisko", nickname="Zmodyfikuj ksywe", title="Zmodyfikuj tytul",
                                        company="Zmodyfikuj firme", address="Zmodyfikuj adres", home_number="Zmodyfikuj telefon domowy", mobile_number="Zmodyfikuj telefon komorkowy",
                                        work_number="Zmodyfikuj telefon sluzbowy", fax="Zmodyfikuj fax", email="Zmodyfikuj email", email2="Zmodyfikuj email2", email3="Zmodyfikuj email3",
                                        homepage="Zmodyfikuj strone domowa", byear="1990", ayear="2000", address_2="Zmodyfikuj drugi adres", phone2="Zmodyfikuj telefon domowy 2",
                                        notes="Zmodyfikuj notatki"))


def test_modify_first_contact_first_name(app):
    if app.group.count() == 0:
        app.contact.create(Contact(first_name="test"))
    app.contact.modify_first_contact(Contact(first_name="Zmodyfikuj imie"))


def test_modify_first_contact_last_name(app):
    if app.group.count() == 0:
        app.contact.create(Contact(first_name="test"))
    app.contact.modify_first_contact(Contact(last_name="Zmodyfikuj nazwisko"))