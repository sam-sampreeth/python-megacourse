import json

with open('subfiles/questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)
for question in data:
    print(question["question"])
    for i, options in enumerate(question["options"]):
        print(i + 1, "-", options)
    choice = int(input("Enter your choice: "))
    question["user_choice"] = choice

score = 0
for i, question in enumerate(data):
    if question["user_choice"] == question["correct_ans"]:
        score += 1
        res = "Correct"
    else:
        res = "Incorrect"
    message = f"{i + 1}. Your answer: {question['user_choice']}, Correct answer: {question['correct_ans']} - {res}"
    print(message)
print("Your score: ", score, "/", len(data))

