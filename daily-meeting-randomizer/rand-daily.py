import random

MESSAGE_FILE = 'message.txt'
NEXT_FILE = 'next.txt'

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

def generate_encouragement(next_person: str) -> str:
  encourage_next = ["go next",
                    "continue",
                    "carry on",
                    ""]
  encourage_next_choice = random.choice(encourage_next)
  encouragement = next_person
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

def read_file(file_name: str) -> str:
  with open(file_name, "r") as file:
    return file.read().strip()

def put_in_box(string: str, closed_box: bool) -> str:
  lines = string.split("\n")
  max_length = max(len(line) for line in lines)
  box = "┌" + "─" * (max_length + 2) + "┐\n"

  for line in lines:
    if closed_box:
      box += f"│ {line.ljust(max_length)} │" + "\n"
    else:
      if len(line) == 0:
        box += "│\n"
      else:
        box += f"│ {line}" + "\n"

  box += "└" + "─" * (max_length + 2) + "┘"

  return box

def main() -> None:
  work_done = read_file(MESSAGE_FILE)
  next_person = read_file(NEXT_FILE)

  greeting_message = generate_greeting()
  encouragement_message = generate_encouragement(next_person)
  finish_message = generate_ending()

  main_message = f"{greeting_message}\n\n{work_done}\n\n{finish_message}\n{encouragement_message}"

  print(put_in_box(main_message, False))

if __name__ == "__main__":
  main()
