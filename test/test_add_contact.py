# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", middle_name="", last_name="", nickname="", title="", company="",
                    address="", home_number="", mobile_number="", work_number="", fax="",
                    email="", email2="", email3="", homepage="", byear="", ayear="",
                    address_2="", phone2="", notes="")] + [
        Contact(first_name=random_string("first_name",5), middle_name=random_string("middle_name",5), last_name=random_string("last_name",5),
                nickname=random_string("nickname", 5),title=random_string("title",5),company=random_string("company",5),
                address=random_string("address", 5),home_number=random_string("home_number",5),mobile_number=random_string("mobile_number",5),
                work_number=random_string("work_number", 5),fax=random_string("fax",5),email=random_string("email",5),
                email2=random_string("email2", 5),email3=random_string("email3",5),homepage=random_string("homepage",5),byear=random_string("byear",5),
                ayear=random_string("ayear", 5),address_2=random_string("address_2",5),phone2=random_string("phone2",5),notes=random_string("notes",5))
        for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




