def get_quests(filepath='files/quests.txt'):
    """ Read a text file and return the list of
    quest items.
    """
    with open(filepath, 'r') as file_local:
        quests_local = file_local.readlines()
    return quests_local


def write_quests(quests_arg, filepath='files/quests.txt'):
    """ Write the quest items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(quests_arg)