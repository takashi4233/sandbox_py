import cat as cat
import dog as dog

class zoo:
    def show(self):
        c2.say()
        c2.move()

    def put_dog(self):
        d1 = dog.dog()
        return d1
    
    def put_cat(self):
        c1 = cat.cat()
        return c1


if __name__ == "__main__":
    z = zoo()
    c1 = z.put_cat()
    print (f"__name__:{c1.say()}")