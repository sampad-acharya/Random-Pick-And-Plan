import random
input = int(input("""1. Cusines\n2. Dishes\nPick your choice [1, 2]:"""))
# List of options
cuisines = [
    "Taiwanese", "Japanese", "Indian", "Georgian", "Korean",
    "Mediterranean", "Thai", "Polish", "Cantonese"
]

dishes = [
    "dumplings", "mezze", "pierogis", "hand rolls/sushi",
    "curry", "pad Thai", "dim sum", "momos", "dan dan noodles"
]

areas = ["LES", "UES", "Midtown", "Kips Bay", "FiDi", "West Village", "UWS","Astoria", "Noho", "Nomad", "Little Italy", "Greenpoint", "Williamsburg", "Bushwick", "Ridgewood", "Bed Stuy", "Crown Heights", "Jackson Heights", "Hells Kitchen", "Flushing", "Forest Hills","SoHo", "Dumbo"]
# Randomly select one from each
place = random.choice(areas)
if input == 1:
    random_cuisine = random.choice(cuisines)
    
    print(f"🎲 How about trying some {random_cuisine} today at {place}?")
elif input == 2:
    random_dish = random.choice(dishes)
    print(f"🎲 How about trying some {random_dish} at {place} today?")
    

