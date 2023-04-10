import random
import time



class default_client():
    def in_put(client):
        game = client.game
        lp = len(game.plate)
        pos = random.randint(0,lp-1)
        game.set_new_go(pos)

        return 0
    def show(client):
        game = client.game
        plate = game.plate
        # print(plate)
        # time.sleep(1)

    def win()