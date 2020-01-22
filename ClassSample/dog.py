import animal as animal
class dog(animal.animal):
    def say(self):
        return "ワン🐶"

if __name__ == "__main__":
    d = dog()
    d.say()
    d.move()
    
    