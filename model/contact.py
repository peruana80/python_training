from sys import maxsize

class Contact:


    def __init__(self, first_name=None, middle_name=None, last_name=None, id=None, nickname=None, title=None, company=None, address=None, home_number=None, mobile_number=None, work_number=None, fax=None,
                 email=None, email2=None, email3=None, homepage=None, byear=None, ayear=None, address_2=None, phone2=None, notes=None, all_emails_from_home_page=None, all_phones_from_home_page=None):
        self.first_name=first_name
        self.middle_name=middle_name
        self.last_name=last_name
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.home_number=home_number
        self.mobile_number=mobile_number
        self.work_number=work_number
        self.fax=fax
        self.email=email
        self.email2=email2
        self.email3=email3
        self.homepage=homepage
        self.byear=byear
        self.ayear=ayear
        self.address_2=address_2
        self.phone2=phone2
        self.notes=notes
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_emails_from_home_page=all_emails_from_home_page
        self.id=id


    def __repr__(self):
        return "%s:%s;%s;%s;%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (self.id, self.first_name, self.middle_name, self.last_name, self.nickname, self.title, self.company,
                                                                         self.address, self.home_number, self.mobile_number, self.work_number, self.fax, self.email, self.email2, self.email3,
                                                                         self.homepage, self.byear, self.ayear, self.address_2, self.phone2, self.notes, self.all_phones_from_home_page,
                                                                         self.all_emails_from_home_page, self.id)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize