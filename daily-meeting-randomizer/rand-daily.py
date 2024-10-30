import configparser
import random

CONFIG_FILE_PATH = 'config.ini'

BOX_TOP_LEFT = "┌"
BOX_TOP_RIGHT = "┐"
BOX_BOTTOM_LEFT = "└"
BOX_BOTTOM_RIGHT = "┘"
BOX_HORIZONTAL = "─"
BOX_VERTICAL = "│"


def generate_greeting() -> str:
  greetings = ["Hello",
               "Hey",
               "Good day",
               "Good morning"]
  group_names = ["everybody",
                 "team",
                 "all"]
  thank_you = "Thank you.\n" if random.choice([True, False]) else ""
  return f"{thank_you}{random.choice(greetings)}, {random.choice(group_names)}."


def generate_encouragement(usual_next_person: str, next_person: str) -> str:
  encouragement = ""
  if usual_next_person and usual_next_person != next_person:
    encouragement += f"{usual_next_person} is not here.\n"
    transitions = ["So, ",
                   "Therefore, ",
                   "Hence, ",
                   "Thus, ",
                   ""]
    encouragement += random.choice(transitions)
  encourage_next = ["go next",
                    "continue",
                    "carry on",
                    ""]
  encourage_next_choice = random.choice(encourage_next)
  encouragement += next_person
  if encourage_next_choice:
    encouragement += f", please, {encourage_next_choice}"
  encouragement += "."
  return encouragement


def generate_ending() -> str:
  finish_phrases = ["And that's it",
                    "And that's it for me",
                    "That's all for me today",
                    "That's it from my side",
                    "It's all for me"]
  no_blockers = "\nNo blockers." if random.choice([True, False]) else ""
  return f"{random.choice(finish_phrases)}.{no_blockers}"


def put_in_box(string: str, closed_box: bool) -> str:
  lines = string.split("\n")
  max_length = max(len(line) for line in lines)
  box = f"{BOX_TOP_LEFT}{BOX_HORIZONTAL * (max_length + 2)}{BOX_TOP_RIGHT}\n"

  for line in lines:
    if closed_box:
      box += f"{BOX_VERTICAL} {line.ljust(max_length)} {BOX_VERTICAL}\n"
    else:
      box += f"{BOX_VERTICAL} {line}\n" if line else f"{BOX_VERTICAL}\n"

  box += f"{BOX_BOTTOM_LEFT}{BOX_HORIZONTAL * (max_length + 2)}{BOX_BOTTOM_RIGHT}"

  return box


def main() -> None:
  config = configparser.ConfigParser()
  try:
    config.read(CONFIG_FILE_PATH)
    work_done = config["app"]["message"]
    next_person = config["app"]["next"]
    usual_next_person = config["app"]["usual_next"]
    closed_box = config.getboolean('app', 'closed_output')
  except (configparser.Error, KeyError) as e:
    print(f"Error reading config file: {e}")
    return

  greeting_message = generate_greeting()
  encouragement_message = generate_encouragement(usual_next_person, next_person)
  finish_message = generate_ending()

  main_message = f"{greeting_message}\n\n{work_done}\n\n{finish_message}\n{encouragement_message}"

  print(put_in_box(main_message, closed_box))


if __name__ == "__main__":
  main()
