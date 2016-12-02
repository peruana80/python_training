import re
from model.contact import Contact


def test_contacts_on_home_page(app,db):
    home_page_contacts,db_contacts = sorted(app.contact.get_contact_list(),key=Contact.id_or_max),sorted(db.get_contact_list(),key=Contact.id_or_max)
    assert len(home_page_contacts)==len(db_contacts)
    for index in range(0,len(db_contacts)):
        assert db_contacts[index].first_name == home_page_contacts[index].first_name
        assert db_contacts[index].last_name == home_page_contacts[index].last_name
        assert db_contacts[index].address == home_page_contacts[index].address
        assert merge_emails_like_on_home_page([db_contacts[index].email, db_contacts[index].email2, db_contacts[index].email3]) == home_page_contacts[index].all_emails_from_home_page
        assert merge_phones_like_on_home_page([db_contacts[index].home_number, db_contacts[index].mobile_number,
                                               db_contacts[index].work_number, db_contacts[index].phone2])== home_page_contacts[index].all_phones_from_home_page


def merge_emails_like_on_home_page(list):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,list)))


def merge_phones_like_on_home_page(list):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: re.sub("[ -()]","",x),
                                filter(lambda x: x is not None,list))))