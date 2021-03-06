from model.group import Group
from random import randrange


def test_modify_group_name(app,db,check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups=db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="modyfikacja nazwy", header="modyfikacja naglowka", footer="modyfikacja stopki")
    group.id=old_groups[index].id
    app.group.modify_group_by_id(group)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        new_groups == app.group.get_group_list()
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_first_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(name="modyfikacja nazwy"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_first_group_heder(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="modyfikacja naglowka"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)