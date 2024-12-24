import random
import art
import game_data

def random_name_assigner():
    return random.choice(game_data.data)


# Building random logic
comparison_1 = random_name_assigner()
comparison_2 = random_name_assigner()
follower_count_1 = comparison_1["follower_count"]
follower_count_2 = comparison_2["follower_count"]
wins = 0

try:
    if comparison_1 == comparison_2:
        print("Same comparison. Retrying again!")
    else:
        while True:
            print(art.logo)
            print(f"Compare A: {comparison_1['name']}, a {comparison_1['description']}, from {comparison_1['country']}")
            print(art.vs)
            print(f"Against B: {comparison_2['name']}, a {comparison_2['description']}, from {comparison_2['country']}")
            follower_compare = input("Who has more followers? Type 'A' or 'B': ").upper()

            if (follower_compare == 'A' and follower_count_1 > follower_count_2) or \
                    (follower_compare == 'B' and follower_count_2 > follower_count_1):
                wins += 1  # Increment the win counter
                print(f"You're right! Current score: {wins}")
                # Update for the next roundA
                comparison_1 = comparison_2
                comparison_2 = random_name_assigner()
                follower_count_1 = follower_count_2
                follower_count_2 = comparison_2["follower_count"]
            else:
                print(f"Sorry, that's wrong! Final score: {wins}")
                break
except Exception as e:
    print(f"An error occurred: {e}")
    # Here you might decide to retry or do something else
    comparison_1 = random_name_assigner()
    comparison_2 = random_name_assigner()