


import dva_go_front_pygame
import dva_go
import dva_go_front_cli



class test_dva_go():

    def __init__(self):
        show_game = 0
        
        game = dva_go.dva_go()
        game.colunmn_quantity = 19
        game.row_quantity = 19

        if(show_game):
            front = dva_go_front_pygame.dva_go_front_pygame()
            front.colunmn_quantity = game.colunmn_quantity
            front.row_quantity = game.row_quantity
            # show = front.show
            client = front
        else:
            # show = lambda:0
            cli = dva_go_front_cli.dva_go_front_cli()
            client = cli
        client.game = game # client 就是前端，game 就是后端

        # game.client = client





        # game.show = show

        game.run()

        return
    

if __name__ == "__main__":
    test_dva_go()