import animal as animal
class cat(animal.animal):
    def say(self):
        return "にゃー😺"

if __name__ == "__main__":
    c = cat()
    c.say()
    c.move()