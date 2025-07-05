import time

class BasicStrategy:
    def __init__(self):
        self.split_chart = {}
        self.soft_chart = {}
        self.hard_chart = {}

        self.tens = ['10', 'J', 'Q', 'K']

        self.split_row_keys = ["A,A","10,10","9,9","8,8","7,7","6,6","5,5","4,4","3,3","2,2"]
        self.soft_row_keys = ['A,9','A,8','A,7','A,6','A,5','A,4','A,3','A,2']
        self.hard_row_keys = [21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4]
        self.upcards  = ['2','3','4','5','6','7','8','9','10',"A"]

        self.split_raw = None
        self.soft_total_raw = None
        self.hard_total_raw = None

        self.function_map = {
            'H':'_hit',
            'D': '_double_down',
            'S': '_stand',
            'Sur': '_surrender'
        }

        self.custom_strategy()
        self.make_charts()


    def custom_strategy(self):
        self.split_raw = [
            # A,A
            [True, True, True, True, True, True, True, True, True, True, True],
            # T,T
            [False, False, False, False, False, False, False, False, False, False, False],
            # 9,9
            [True, True, True, True, True, False, True, True, False, False, False],
            # 8,8
            [True, True, True, True, True, True, True, True, True, True, True],
            # 7,7
            [True, True, True, True, True, True, False, False, False, False, False],
            # 6,6
            [True, True, True, True, True, False, False, False, False, False, False],
            # 5,5
            [False, False, False, False, False, False, False, False, False, False, False],
            # 4,4
            [False, False, False, True,  True,  False, False, False, False, False, False],
            # 3,3
            [True, True, True, True, True, True, False, False, False, False, False],
            # 2,2
            [True, True, True, True, True, True, False, False, False, False, False],
        ]

        self.soft_total_raw = [
            # A,9
            ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            # A,8
            ["S", "S", "S", "S", "D", "S", "S", "S", "S", "S"],
            # A,7
            ["D", "D", "D", "D", "D", "S", "S", "H", "H", "H"],
            # A,6
            ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"],
            # A,5
            ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"],
            # A,4
            ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"],
            # A,3
            ['H', 'H', 'H', 'D', 'D', "H", "H", "H", "H", "H"],
            # A,2
            ['H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H']
        ]

        self.hard_total_raw = [
            # 21
            ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            # 20
            ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            # 19
            ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            # 18
            ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            # 17
            ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            # 16
            ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
            # 15
            ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
            # 14
            ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
            # 13
            ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
            # 12
            ['H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
            # 11
            ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
            # 10
            ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H'],
            # 9
            ['H', 'D', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],
            # 8
            ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
            # 7
            ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
            # 6
            ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
            # 5
            ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
            # 4
            ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        ]


    def make_charts(self):
        for key, row in zip(self.split_row_keys, self.split_raw):
            self.split_chart[key] = {
                up: cell
                for up, cell in zip(self.upcards, row)
            }

        for key, row in zip(self.soft_row_keys, self.soft_total_raw):
            self.soft_chart[key] = {
                up: cell
                for up, cell in zip(self.upcards, row)
            }

        for key, row in zip(self.hard_row_keys, self.hard_total_raw):
            self.hard_chart[key] = {
                up: cell
                for up, cell in zip(self.upcards, row)
            }

    def bot_choice(self, hand, dealer_hand, methods):
        methods.pop("_exit_game", None)

        dealer_uphand = dealer_hand.value[1][0]
        if dealer_uphand in self.tens:
            dealer_uphand = '10'
        player_hand = ','.join([x[0] for x in hand.value])

        # splits
        if player_hand[0] == player_hand[2]:
            # converts 10, J, Q, K to T's
            if player_hand[0] in self.tens:
                player_hand = '10,10'
            if self.split_chart[player_hand][dealer_uphand]: # returns True or False
                return methods['_split']
        
        if player_hand[-1] == 'A':
            a,b = player_hand.split(',')
            player_hand = f'{b},{a}'

        # softs    
        if "A" in player_hand:
            if hand.score[-1] < 21 and len(player_hand) > 3:
                a = player_hand[0]
                cards = player_hand.split(',')
                b = None
                for x in cards:
                    b += int(x)
                player_hand = f'{a}+{b}'

            choice = self.soft_chart[player_hand][dealer_uphand]
            return methods[self.function_map[choice]]
            
        # hards
        else:
            player_score = hand.score[0]
            print(player_score)
            choice = self.hard_chart[player_score][dealer_uphand]
            return methods[self.function_map[choice]]


    def pair_splitting(self):
        pass
    
    def soft_totals(self):
        pass

    def hard_totals(self):
        pass


if __name__ == "__main__":
    basic_strat = BasicStrategy()