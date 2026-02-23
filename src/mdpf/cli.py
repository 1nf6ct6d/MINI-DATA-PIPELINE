from .config import Config 
def main():
    config = Config.load("config.json")
    print(config)