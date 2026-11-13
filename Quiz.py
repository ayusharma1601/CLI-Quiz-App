QUESTIONS = [
    {
        "question": "How long does sunlight take to reach Earth?",
        "answers": {"8 minutes and 20 seconds", "8 minutes 20 seconds", "8 minutes"},
    },
    {
        "question": "Who is Peter Parker?",
        "answers": {"spider-man", "spiderman"},
    },
    {
        "question": "What gun is known to be the most reliable in the army?",
        "answers": {"ak-47", "ak47"},
    },
    {
        "question": "What is Ohm's law?",
        "answers": {"v=ir", "v = ir"},
    },
    {
        "question": "What does Captain America say in the climax of Avengers: Endgame?",
        "answers": {"i can do this all day"},
    },
]


def main():
    print("WELCOME TO THE QUIZ GAME\n")
    print("LET'S SEE HOW GOOD YOU ARE!\n")

    score = 0
    for number, item in enumerate(QUESTIONS, start=1):
        print(f"Question {number}: {item['question']}")
        answer = input("Enter your answer: ").strip().casefold()
        if answer in item["answers"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer. Better luck next time.")
        print("-----------------------\n")

    print(f"You scored {score} out of {len(QUESTIONS)} points.")
    print("Thank you for playing!")


if __name__ == "__main__":
    main()
