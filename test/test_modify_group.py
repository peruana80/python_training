from model.group import Group

def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="modyfikacja nazwy", header="modyfikacja naglowka", footer="modyfikacja stopki"))


def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="modyfikacja nazwy"))


def test_modify_first_group_heder(app):
    app.group.modify_first_group(Group(header="modyfikacja naglowka"))