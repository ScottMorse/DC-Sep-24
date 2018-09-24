
class Restaurant:
    
    def __init__(self,name,cuisine):
        self._name = name
        self._cuisine = cuisine
        self._is_open = False
    
    @property
    def name(self):
        return self._name

    @property
    def cuisine(self):
        return self._cuisine

    @property
    def description(self):
        return f"{self.name}: {self.cuisine}"

    @property
    def is_open(self):
        return self._is_open
    
    def open_restaurant(self):
        self._is_open = True
    
    def __repr__(self):
        return f"<{self.description}>"

fish_market = Restaurant("Fish Market","seafood")
print(fish_market.name)
print(fish_market.cuisine)
print(fish_market.description)
fish_market.open_restaurant()
print(fish_market.is_open)