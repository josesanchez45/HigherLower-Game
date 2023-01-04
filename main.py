import art
import data
import random

def get_random_account():
    """Randomly selects information from list of dictionaries"""
    return random.choice(data.data)

def format_account(account):
    """Formats dictionary info to be presentable to user"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

def check_answer(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == "a"
    else:
       return guess == "b"

def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)



def game():
  print(art.logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_account(account_a)}.")
    print(art.vs)
    print(f"Against B: {format_account(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(art.logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()
