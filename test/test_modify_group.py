from model.group import Group

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="modyfikacja nazwy", header="modyfikacja naglowka", footer="modyfikacja stopki"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="modyfikacja nazwy"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_first_group_heder(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="modyfikacja naglowka"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)