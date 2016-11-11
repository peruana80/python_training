from model.contact import Contact
import re

class ContactHelper:


    def __init__(self, app):
        self.app = app


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def delete_first_contact(self):
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        # accept popup window
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_main_page()
        self.select_contact_by_index(index)
        self.open_contact_to_edit_by_index(index)
        #fill contact form
        self.fill_contact_form(new_contact_data)
        #update form
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        self.select_contact_by_index(index)
        table_row = wd.find_elements_by_name("entry")[index]
        cell = table_row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        self.select_contact_by_index(index)
        table_row = wd.find_elements_by_name("entry")[index]
        cell = table_row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_number = wd.find_element_by_name("home").get_attribute("value")
        mobile_number = wd.find_element_by_name("mobile").get_attribute("value")
        work_number = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, id=id, address= address,
                       email=email, email2=email2, email3= email3,
                       home_number=home_number, mobile_number=mobile_number, work_number=work_number, phone2=phone2)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_main_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                text1 = cells[1].text
                text2 = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(first_name=text2, last_name=text1, id=id, address=address, all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_number = re.search("H: (.*)", text).group(1)
        mobile_number = re.search("M: (.*)", text).group(1)
        work_number = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_number=home_number, mobile_number=mobile_number, work_number=work_number, phone2=phone2)


    def change_filed_value(self, filed_name, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element_by_name(filed_name).click()
            wd.find_element_by_name(filed_name).clear()
            wd.find_element_by_name(filed_name).send_keys(text)


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_filed_value("firstname", contact.first_name)
        self.change_filed_value("middlename", contact.middle_name)
        self.change_filed_value("lastname", contact.last_name)
        self.change_filed_value("nickname", contact.nickname)
        self.change_filed_value("title", contact.title)
        self.change_filed_value("company", contact.company)
        self.change_filed_value("address", contact.address)
        self.change_filed_value("home", contact.home_number)
        self.change_filed_value("mobile", contact.mobile_number)
        self.change_filed_value("work", contact.work_number)
        self.change_filed_value("fax", contact.fax)
        self.change_filed_value("email", contact.email)
        self.change_filed_value("email2", contact.email2)
        self.change_filed_value("email3", contact.email3)
        self.change_filed_value("homepage", contact.homepage)
        self.change_filed_value("byear", contact.byear)
        self.change_filed_value("ayear", contact.ayear)
        self.change_filed_value("address2", contact.address_2)
        self.change_filed_value("phone2", contact.phone2)
        self.change_filed_value("notes", contact.notes)


        # fill homepage
        #wd.find_element_by_name("homepage").click()
        #wd.find_element_by_name("homepage").clear()
        #wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
        #    wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[15]").is_selected():
        #    wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[15]").click()

        # fill Birthday
        #wd.find_element_by_name("byear").click()
        #wd.find_element_by_name("byear").clear()
        #wd.find_element_by_name("byear").send_keys(contact.byear)
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[13]").is_selected():
        #    wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[13]").click()
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[8]").is_selected():
        #    wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[8]").click()

        # fill anniversary
        #wd.find_element_by_name("ayear").click()
        #wd.find_element_by_name("ayear").clear()
        #wd.find_element_by_name("ayear").send_keys(contact.ayear)

    def open_main_page(self):
        wd = self.app.wd
        if not (wd.current_url == self.app.base_url):
            wd.find_element_by_xpath("//*[@id='nav']/ul/li[1]/a").click()

    def open_new_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith(self.app.base_url) and len(wd.find_elements_by_name("Enter")) > 0):
            wd.find_element_by_link_text("add new").click()


    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.contact_cache = None


    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new")
        return len(wd.find_elements_by_name("selected[]"))



