while True:
    # Get user input and strip extra space chars and make case insensitive
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()


    if 'add' in user_action or 'new' in user_action:
         quest = user_action[4:]

         with open('files/quests.txt', 'r') as file:
              quests = file.readlines()

         quests.append(quest)

         with open('files/quests.txt', 'w') as file:
            file.writelines(quests)

    elif 'show' in user_action or 'display' in user_action:

        with open('files/quests.txt', 'r') as file:
            quests = file.readlines()


        for index, item in enumerate(quests):
            item = item.strip("\n")
            item = item.title()
            print(f"{index + 1}-{item}")

        if len(quests) == 1:
            print(f"You currently have 1 adventure ahead!")
        else:
            print(f"You currently have {len(quests)} adventures ahead!")
    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open('files/quests.txt', 'r') as file:
            quests = file.readlines()

        new_quest = input("Enter new quest: ")
        quests[number] = new_quest + "\n"

        with open('files/quests.txt', 'w') as file:
            file.writelines(quests)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('files/quests.txt', 'r') as file:
            quests = file.readlines()
        index = number - 1
        quest_to_remove = quests[index].strip('\n')
        quests.pop(index)

        with open('files/quests.txt', 'w') as file:
            file.writelines(quests)

        message = f"Quest {quest_to_remove} has been removed from the list. Great job, adventurer!"
        print(message)

    elif user_action == 'exit':
        break
    else:
        print("Unknown command entered. Please try again")

print('Bye!')


