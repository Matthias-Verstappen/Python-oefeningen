#oefening 13
pc_choice = "paper"
choice = str(input("What do you choose: paper, rock or scissors? "))

if choice == pc_choice:
    print("You chose", choice, "\nI chose", pc_choice, "\nIt's a tie!")

elif choice == "rock" and pc_choice == "scissors":
    print("You chose", choice, "\nI chose", pc_choice, "\nYou win :-)")

elif choice == "paper" and pc_choice == "rock":
    print("You chose", choice, "\nI chose", pc_choice, "\nYou win :-)")

elif choice == "scissors" and pc_choice == "paper":
    print("You chose", choice, "\nI chose", pc_choice, "\nYou win :-)")

elif choice == "rock" and pc_choice == "paper":
    print("You chose", choice, "\nI chose", pc_choice, "\nI win :-)")

elif choice == "scissors" and pc_choice == "rock":
    print("You chose", choice, "\nI chose", pc_choice, "\nI win :-)")

elif choice == "paper" and pc_choice == "scissors":
    print("You chose", choice, "\nI chose", pc_choice, "\nI win :-)")


