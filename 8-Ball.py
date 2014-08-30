import random



print("Ask the 8-ball:")
question = input("> ")
print(question)

awnsers = [
    "Yes",
    "No",
    "Sines point to yes",
    "Reply hazy,try agian",
    "Without a doubt",
    "As I see it, yes",
]
while True:
    question = input (">")
    awnser = random.choice(awnsers)
    print(awnser)
