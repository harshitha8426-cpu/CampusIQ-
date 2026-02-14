
import random

def generate_data():
    return {
        "crowd": random.randint(30, 100),
        "waste": random.randint(40, 100),
        "runtime": random.randint(100, 500)
    }
