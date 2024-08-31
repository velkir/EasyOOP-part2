class Vet:
    animals = []
    space = 5
    waiting_list = []

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if Vet.space > 0:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            Vet.space -= 1
            return f"{animal_name} registered by {self.name}"
        else:
            Vet.waiting_list.append(animal_name)
            return f"Vet's space if full. {animal_name} added to the waiting list."

    def unregister_animal(self, animal_name):
        if animal_name in self.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            Vet.space += 1
            if len(Vet.waiting_list) != 0:
                print("Registering an animal from the waiting list")
                print(self.register_animal(Vet.waiting_list.pop(0)))
            return f"{animal_name} deregistered by {self.name}"
        else:
            return f"There's no animal named {animal_name}"

    def info(self):
        return (f"{self.name} takes care of {len(self.animals)} animals.\n"
                f"Vet's remaining space: {Vet.space}")


kate = Vet(name="Kate")
victoria = Vet(name="Victoria")

print(kate.register_animal("Forza"))
print(kate.register_animal("Gerda"))
print(victoria.register_animal("Dojdik"))
print(victoria.register_animal("Sharik"))
print(victoria.register_animal("Donkey"))
print(victoria.register_animal("Shrek"))

print(victoria.unregister_animal("Sharik"))
print(kate.info())
