import random

thank_you = "Thank you.\n" if random.choice([True, False]) else ""

greetings = ["Hello",
             "Hey",
             "Good day",
             "Good morning"]

group_name = ["everybody",
              "team",
              "all"]

finish = ["And that's it",
          "And that's it for me",
          "That's all for me today",
          "That's it from my side",
          "It's all for me"]

encourage_next = ["go next",
                  "continue",
                  "carry on",
                  ""]

greeting_message = f"{thank_you}{random.choice(greetings)}, {random.choice(group_name)}."

with open("message.txt", "r") as file:
    work_done = file.read().strip()
with open("next.txt", "r") as file:
    next_person = file.read().strip()


encourage_next_choice = random.choice(encourage_next)
encouragement = next_person
if encourage_next_choice!= "":
    encouragement += ", please, " + encourage_next_choice
encouragement += "."




thank_you = "Thank you.\n" if random.choice([True, False]) else ""

print("┌─────────────")
main_message = f"{greeting_message}\n\n{work_done}\n\n{random.choice(finish)}.\n{encouragement}"
main_message = main_message.replace("\n", "\n│ ")
print(f"│ {main_message}")
print("└─────────────────")