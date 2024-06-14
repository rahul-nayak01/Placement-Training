class Bird:
    def intro(self):
        print("There are many types of birds")
    
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("sparrows can fly")

class ostrich(Bird):

    def flight(self):
        print("ostrich cannot fly")

ob_bird=Bird()
ob_spr=sparrow()
ob_ostrich=ostrich()

ob_bird.intro()
ob_bird.flight()

ob_spr.intro()
ob_spr.flight()

ob_ostrich.intro()
ob_ostrich.flight()