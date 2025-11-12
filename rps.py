#!/usr/bin/env python3
import random

OPTIONS = ["rock", "paper", "scissors"]

def decide(user, comp):
    if user == comp:
        return "tie"
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    return "user" if wins[user] == comp else "comp"

def main():
    user_score = 0
    comp_score = 0
    while True:
        u = input("Choose (rock/paper/scissors) or 'q' to quit: ").strip().lower()
        if u == "q":
            break
        if u not in OPTIONS:
            print("Invalid choice.")
            continue
        c = random.choice(OPTIONS)
        result = decide(u, c)
        if result == "tie":
            print(f"Both chose {u}. It's a tie.")
        elif result == "user":
            user_score += 1
            print(f"You: {u}  Computer: {c}  => You win!")
        else:
            comp_score += 1
            print(f"You: {u}  Computer: {c}  => Computer wins.")
        print(f"Score -> You: {user_score}  Computer: {comp_score}")
    print("Final score:", user_score, ":", comp_score)

if __name__ == "__main__":
    main()
