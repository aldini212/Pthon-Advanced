from tensorflow.python.keras.engine.data_adapter import select_data_adapter


class Vertebrate:
    def __init__(self,backbone=True):
        self.backbone = backbone

    def vertebrate_info(self):
        print("Vetebrates have a backbone")



class Aquatic:
    def __init__(self, habitat ="water"):
        self.habitat = habitat

    def aquatic_info(self):
        print("Aquatic animals live in water")

class Fish(vertebrate,Aquatic):
    def __init__(self,species,backbone=True,habitat="water"):
        super().__init__(backbone=backbone)
        self.habitat = habitat
        self.species = species

    def fish_info(self):
        print(f"The {self.species} Is a type a fish found in {self.habitat}")

    def swim(self):
        print("The fish is swiming.")

goldfish = Fish("Goldfish")
print(goldfish.backbone)
print(goldfish.habitat)

goldfish.vertebrate_info()
goldfish.aquatic_info()
goldfish.swim()
goldfish.fish_info()