from src.ui.ui import UI
from src.controller.functionalities.functionalities import Controller
# f = open("repository/sentences.txt", "w")
ui = UI(Controller("repository/sentences.txt"))
ui.start()



# anna has apples
# patricia has pears
# cars are fast
# planes are quick
# the quick brown fox jumps over the lazy dog
