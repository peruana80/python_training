# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="new", header="new", footer="new"))


def test_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

