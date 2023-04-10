


class dva_go_front_cli():

    def show(client):
        print(client.game.plate)
        return 

    def get_view_model(client,vm):
        client.plate = vm


    def send(client,legal):
        # print('ll',legal)
        if(legal==0):
            print('此着非法，请重着')
        return

    def in_put(client):
        game = client.game

        # print('input')
        pos = int(input('input_a_go'))

        game.set_new_go(pos)

        return 0
    
    def __init__(client):

        pass