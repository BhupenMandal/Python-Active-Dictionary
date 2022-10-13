class Group:
    def __init__(self, name):
        self.name = name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    if user == group.get_name():
        return True
    else:
        if user in group.get_users():
            return True

    for i in group.get_groups():
        return is_user_in_group(user, i)
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Should print False for the test 2 and 4, all other tests should print True

print("Test 1: ", "True" if is_user_in_group("sub_child_user", parent) else "False")

print("Test 2: ", "True" if is_user_in_group("", child) else "False")

print("Test 3: ", "True" if is_user_in_group("child", child) else "False")

print("Test 4: ", "True" if is_user_in_group("user", parent) else "False")

print("Test 5: ", "True" if not is_user_in_group("user", parent) else "False")
