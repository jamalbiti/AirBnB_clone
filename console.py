#!/usr/bin/python3
"""This module provides a command-line interface for managing
objects in the HBnB clone"""

import cmd
import models
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):

    """command HBNBC."""

    prompt = "(hbnb) "

    def default(self, line):
        """
        listning"""
        self._precmd(line)

    def _precmd(self, line):
        """check the command preCMD"""
        equal = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not equal:
            return line
        itemName = equal.group(1)
        method = equal.group(2)
        args = equal.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(itemName, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        order = method + " " + itemName + " " + uid + " " + attr_and_value
        self.onecmd(order)
        return order

    def update_dict(self, classname, uid, s_dict):
        """
        should update dict"""
        selectItem = s_dict.replace("'", '"')
        loadItem = json.loads(selectItem)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in loadItem.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_EOF(self, line):
        """
        should handle end of fille"""
        print()
        return True

    def do_quit(self, line):
        """
        should exit from the app"""
        return True

    def emptyline(self):
        """
        in empty line sould do nothing"""
        pass

    def do_create(self, line):
        """
        should create new items"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            item = storage.classes()[line]()
            item.save()
            print(item.id)

    def do_show(self, line):
        """
        should display and show the result"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            items = line.split(' ')
            if items[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(items) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(items[0], items[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """
        should delete and destroy the target"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            items = line.split(' ')
            if items[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(items) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(items[0], items[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """
        should return all itmes"""
        item = line.split()
        store = models.storage.all()
        create_new_list = []

        if len(item) == 0:
            for obj in store.values():
                create_new_list.append(obj.__str__())
            print(create_new_list)
        elif item[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in store.values():
                if obj.__class__.__name__ == item[0]:
                    create_new_list.append(obj.__str__())
            print(create_new_list)

    def do_count(self, line):
        """
        should return the total counter"""
        items = line.split(' ')
        if not items[0]:
            print("** class name missing **")
        elif items[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    items[0] + '.')]
            print(len(matches))

    def do_update(self, line):
        """
        should update the item targeted"""
        if line == "" or line is None:
            print("** class name missing **")
            return

        regix = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        equal = re.search(regix, line)
        itemName = equal.group(1)
        uid = equal.group(2)
        attribute = equal.group(3)
        value = equal.group(4)
        if not equal:
            print("** class name missing **")
        elif itemName not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(itemName, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[itemName]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
