import functions

while True:
    # Get user input and strip extra space chars and make case insensitive
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()


    if user_action.startswith("add"):
        quest = user_action[4:]

        quests = functions.get_quests()

        quests.append(quest + '\n')

        functions.write_quests(quests)

    elif user_action.startswith("show"):

        quests = functions.get_quests()


        for index, item in enumerate(quests):
            item = item.strip("\n")
            item = item.title()
            print(f"{index + 1}-{item}")

        if len(quests) == 1:
            print(f"You currently have 1 adventure ahead!")
        else:
            print(f"You currently have {len(quests)} adventures ahead!")
    elif user_action.startswith('edit') or user_action.startswith('replace'):
        try:
            number = int(user_action[5:])
            number = number - 1

            quests = functions.get_quests()

            new_quest = input("Enter new quest: ")
            quests[number] = new_quest + "\n"

            functions.write_quests(quests)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete') or user_action.startswith('remove'):
        try:
            number = int(user_action[9:])

            quests = functions.get_quests()
            index = number - 1
            quest_to_remove = quests[index].strip('\n')
            quests.pop(index)

            functions.write_quests(quests)

            message = f"Quest {quest_to_remove} has been removed from the list. Great job, adventurer!"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action == 'exit':
        break
    else:
        print("Unknown command entered. Please try again")

print('Bye!')


