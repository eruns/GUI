from tkinter import *
import tkinter as tk
from Game import *


class Root(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("GoFIsh")
        self.geometry("900x600")

class MainMenu(tk.Menu):

    def __init__(self, root, *args, **kwargs):
        tk.Menu.__init__(self, root, *args, **kwargs)

        file_menu = FileMenu(self, tearoff= 0)
        self.add_cascade(label="File", menu=file_menu)

        root.config(menu=self)

class FileMenu(tk.Menu):
    """Creates File menu."""

    def __init__(self, root, *args, **kwargs):
        tk.Menu.__init__(self, root, *args, **kwargs)

        self.add_command(label="Exit", command=root.quit)


class GoFish(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)

        self.player_select_window()


    def player_select_window(self):
        self.master.title("Go fish")

        self.pack(fill=tk.BOTH, expand=1)

        self.button_list = []


        quitbutton = tk.Button(self, text="quit", command=quit)

        quitbutton.place(x=0, y=0)


        var1 = tk.IntVar()
        tk.Checkbutton(self, text='blah1', variable=var1)
        var2 = tk.IntVar()
        tk.Checkbutton(self, text='blah2', variable=var2)
        players = ( 2, 3, 4)
        xx = 200
        for player in players:
            b = tk.Button(self.master, text= str(player) + ' Players',
                          command=lambda player=player: self.set_player_count(player))
            self.button_list.append(b)
            xx = xx + 85
            b.place(x=xx, y=255)




    def set_player_count(self, player_count):
        self.player_count = player_count
        self.submit_request()

    def submit_request(self):
        tk.Frame.pack_forget(self)
        for button in self.button_list:
            button.destroy()
        self.init_window()



    def init_window(self):

        self.pack(fill="both", expand=1)
        self.players = self.player_select_window
        self.reveal_button()
        # self.player_turn()
        self.player_score()
        # self.game = Game(hand_size=5, hand_count=self.player_count, max_hand_size=52, discard_type=Visibility.INVISIBLE,
        #             ace_rank=Rank.ACELOW)
        self.choose_player()
        self.choose_rank()
        # self.player_hand()



    def reveal_button(self):
        revealbutton = tk.Button(self, text="reveal", command=self.reveal)
        revealbutton.place(x=350, y=570)

    # def player_turn(self):
    #     player = "p1"
    #     if player == "p1":
    #         turn = tk.Label(self, text="player 1", relief=tk.SUNKEN)
    #         turn.place(x=300, y=575)
    #     elif player == "p2":
    #         turn = tk.Label(self, text="player 2", relief=tk.SUNKEN)
    #         turn.place(x=300, y=575)
    #     elif player == "p3":
    #         turn = tk.Label(self, text="player 3", relief=tk.SUNKEN)
    #         turn.place(x=300, y=575)
    #     elif player == "p4":
    #         turn = tk.Label(self, text="player 4", relief=tk.SUNKEN)
    #         turn.place(x=300, y=575)
    #     else:
    #         pass


    # def player_hand(self):
    #     for hand in Game.hands:
    #         player = Game.hands[hand][0]
    #     print(player)
        # player = "p2"
        # if player == "p1":
        #     hand = [1, 2, 3, 4, 5]
        #     hnd = tk.Label(self, text=hand, relief=tk.RAISED)
        #     hnd.place(x=300, y=600)
        # elif player == "p2":
        #     hand = [2, 2, 2, 2, 2]
        #     hnd = tk.Label(self, text=hand, relief=tk.RAISED)
        #     hnd.place(x=300, y=600)
        # elif player == "p3":
        #     hand = [8, 8, 9, 6, 7]
        #     hnd = tk.Label(self, text=hand, relief=tk.RAISED)
        #     hnd.place(x=300, y=600)
        # elif player == "p4":
        #     hand = [7, 7, 7, 7, 7]
        #     hnd = tk.Label(self, text=hand, relief=tk.RAISED)
        #     hnd.place(x=300, y=600)
        # else:
        #     pass

    def choose_player(self):

        selected_player = tk.StringVar()
        selected_player.set("L")  # initialize
        nx = 300
        for i in range(0, self.player_count):
            player = i
            b = tk.Button(self, text="player " + str(i+1), command=lambda player=player: self.submit_player(player))

            nx = nx + 75
            b.place(x=nx, y=150)


    def submit_player(self, p_value):
        self.selected_player = p_value
        print(self.selected_player)
        self.rank_button_state(state=NORMAL)
        # self.choose_hand(hand)
        return(self.selected_player)

    def choose_rank(self):

        rank_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
        select_rank = tk.StringVar()
        select_rank.set(rank_list[0])
        self.rank_button_list = []
        nx = 275
        for rank in rank_list:
            b = tk.Button(self, text=rank,  command=lambda rank=rank: self.submit_rank(rank))
            nx = nx + 35
            b.place(x=nx, y=200)
            self.rank_button_list.append(b)
        self.rank_button_state()

    def rank_button_state(self, state=DISABLED):
        for button in self.rank_button_list:
            button.config(state=state)


    def submit_rank(self, r_value):
        self.selected_rank = r_value
        print(self.selected_rank)
        return(self.selected_rank)


    def selected_suit(self, value):
        print(value)

    def player_score_title(self):
        title = tk.Label(self, text="Player's Scores:", font=("Helvetica", 16))
        title.place(x=300, y=50)

    def player_score(self):
        title = tk.Label(self, text=self.player_count, font=("Helvetica", 16))
        title.place(x=300, y=50)

        players = 2

        if players == 2:
            player_1_points = 1
            player_2_points = 1

            player_1 = tk.Label(self, text="player 1: " + str(player_1_points), relief=tk.RAISED)
            player_1.place(x=300, y=100)
            player_2 = tk.Label(self, text="player 2: " + str(player_2_points), relief=tk.RAISED)
            player_2.place(x=450, y=100)

        elif players == 3:
            player_1_points = 1
            player_2_points = 1
            player_3_points = 1

            player_1 = tk.Label(self, text="player 1:" + str(player_1_points), relief=tk.RAISED)
            player_1.place(x=300, y=100)
            player_2 = tk.Label(self, text="player 2: " + str(player_2_points), relief=tk.RAISED)
            player_2.place(x=450, y=100)
            player_3 = tk.Label(self, text="player 3: " + str(player_3_points), relief=tk.RAISED)
            player_3.place(x=600, y=100)

        elif players == 4:
            player_1_points = 1
            player_2_points = 1
            player_3_points = 1
            player_4_points = 1

            player_1 = tk.Label(self, text="player 1: " + str(player_1_points), relief=tk.RAISED)
            player_1.place(x=300, y=100)
            player_2 = tk.Label(self, text="player 2: " + str(player_2_points), relief=tk.RAISED)
            player_2.place(x=450, y=100)
            player_3 = tk.Label(self, text="player 3: " + str(player_3_points), relief=tk.RAISED)
            player_3.place(x=600, y=100)
            player_4 = tk.Label(self, text="player 4: " + str(player_4_points), relief=tk.RAISED)
            player_4.place(x=750, y=100)
        else:
            pass

    # def play_game(self):
    #

    def reveal(self):
        self.player_hand()

    def quit(self):
        exit()


if __name__ == "__main__":
    root = Root()
    menu = MainMenu(root)
    gofish = GoFish(root)
    root.mainloop()
