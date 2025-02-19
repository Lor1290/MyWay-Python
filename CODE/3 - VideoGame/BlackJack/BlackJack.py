#Import
from random import randint
import secrets
import time
import sys
import curses
import keyboard
from curses import wrapper

#Definizione-'stdscr'   
def main(stdscr):

    #Immagini secondarie
    wallpaper = ["                   ▄▄▄▄▄▄▄▄████████▄  ",
                "   ▄▄▄████████████████████████   ████  ", 
                "  ███████████████████████████▌ ▐  ███▌ █████▀▀▀▀██  ",
                " ▐███████████████████████████  █▀  ██▌ █████▄  ▄██▌  ",
                "  ███████████████████████████  ██▄  ██ █████▌  ███▌  ",
                "  █████████████████  ▀███████▄████████ ▐█  █▌  ███▌  ",
                "  ████████████████     ▀██████████████ ▐█▄▄   ████  ",
                "  ▐█████████████▀        ▀████████████▌ ██████████  ",
                "   ███████████▀             ▀██████████ ██████████  ",
                "   ██████████                 ▀████████ ██████████  ",
                "   ████████▀                    ███████ ▐█████████  ",
                "    ███████                      ██████▌▐████████▌  ",
                "    ██████                       ██████▌ ████████▌  ",
                "     █████▌                     ▄███████ ████████▌  ",
                "     ███████▄                  ▄█████████ ████████  ",
                "     ██████████▄▄▄▄▄██   ████████████████ ▐███████  ",
                "      ███████████████     ▀██████████████▌ ███████  ",
                "       █████████████▀         ▀████████████ ███████  ",
                "       ████████████▄▄██████████████████████ ███████  ",
                "       ███▀▀███  ██████████████████████████ ▐██████  ",
                "       ▐██      ▐██████████████████████████▌▐█████▌  ",
                "       ▐███  █  ███████████████████████████▌ ▐████▌  ",
                "        ████    ███████████████████████████▀ █████  ",
                "        ████▌ ▄▄███████████████████▀▀▀▀▀▀▀ ▄██████  ",
                "         ▀▀██▀▀▀▀▀▀▀▀   ▄▄▄▄▄▄▄▄████████████████  ",
                "                                                 ",
                "                                                    " ]

    black_jack = [ "  ▐████▄▐█    ▐██   ████▄██  ▄█  ██    ▄▄     ▄███▄▐█▌  █▀ ",
                    " ▐█  ██▐█    ███▌ ██  ████ ██   ██   ████   ▐█▌ ▐███▌▄█▀  ",
                    " ▐█▄▄█▀▐█    █▌██ ██    ████    ██ ▄██████▄ ▐█▌   ▐███▌   ",
                    " ██  ██▐█   ▐█ ▐█ ██    ██▀██   ████████████▐█▌   ▐██▀█▄  ",
                    " ▐█  ████   ██▀▀█▌██  ████  █▌  ██▀████████▀▐█▌ ▐███▌ ██  ",
                    " ▐███▀▀▐█████▌  ▀█ ████▀██  ▀████     ██▌    ▀███▀▐█   ██ " ]

    #Carte da gioco
    ace_of_spades = [   "┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐",
                        "│                         │",
                        "│ A                       │",
                        "│ ♠                       │",
                        "│                         │",
                        "│                         │",
                        "│            w            │",
                        "│           www           │",
                        "│          wwwww          │",
                        "│         wwwwwww         │",
                        "│        wwwwwwwww        │",
                        "│         wwwwwww         │",
                        "│            w            │",
                        "│          wwwww          │",
                        "│                         │",
                        "│                         │",
                        "│                       A │",
                        "│                       ♠ │",
                        "│                         │",
                        "└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘" ]

    two_of_spades = [   "┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐",
                        "│                         │",
                        "│ 2          w            │",
                        "│ ♠         www           │",
                        "│          wwwww          │", 
                        "│         wwwwwww         │",
                        "│          wwwww          │",
                        "│            w            │",
                        "│           www           │",
                        "│                         │",
                        "│                         │",
                        "│           www           │",
                        "│            w            │",
                        "│          wwwww          │",
                        "│         wwwwwww         │",
                        "│          wwwww          │",
                        "│           www         ♠ │",
                        "│            w          2 │",
                        "│                         │",
                        "└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘" ]

    tree_of_spades = [  "┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐",
                        "│                         │",
                        "│ 3          w            │",
                        "│ ♠         www           │", 
                        "│          wwwww          │", 
                        "│            w            │",
                        "│           www           │",
                        "│                         │",
                        "│            w            │",
                        "│           www           │",
                        "│          wwwww          │",
                        "│            w            │",
                        "│           www           │",
                        "│                         │",
                        "│            w            │",
                        "│           www           │",
                        "│          wwwww          │",
                        "│            w          ♠ │",
                        "│           www         3 │",
                        "│                         │",
                        "└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘" ]

    four_of_spades = [  "┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐",
                        "│                         │",
                        "│ 4     w         w     4 │",
                        "│ ♠    www       www    ♠ │",  
                        "│     wwwww     wwwww     │", 
                        "│       w         w       │",
                        "│      www       www      │",
                        "│                         │",
                        "│                         │",
                        "│                         │",
                        "│                         │",
                        "│                         │",
                        "│                         │",
                        "│                         │",
                        "│      www       www      │",
                        "│       w         w       │",
                        "│     wwwww     wwwww     │",
                        "│ ♠    www       www    ♠ │",
                        "│ 4     w         w     4 │",
                        "│                         │",
                        "└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘" ]

    five_of_spades = [  "┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐",
                        "│                         │",
                        "│ 5     w         w     5 │",
                        "│ ♠    www       www    ♠ │",  
                        "│     wwwww     wwwww     │", 
                        "│       w         w       │",
                        "│      www       www      │",
                        "│                         │",
                        "│            w            │",
                        "│           www           │",
                        "│          wwwww          │",
                        "│            w            │",
                        "│           www           │",
                        "│                         │",
                        "│      www       www      │",
                        "│       w         w       │",
                        "│     wwwww     wwwww     │",
                        "│ ♠    www       www    ♠ │",
                        "│ 5     w         w     5 │",
                        "│                         │",
                        "└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘" ]

    six_of_spades = [   "┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐",
                        "│                         │",
                        "│ 6     w         w     6 │",
                        "│ ♠    www       www    ♠ │", 
                        "│     wwwww     wwwww     │", 
                        "│       w         w       │",
                        "│      www       www      │",
                        "│                         │",
                        "│       w         w       │",
                        "│      www       www      │",
                        "│     wwwww     wwwww     │",
                        "│       w         w       │",
                        "│      www       www      │",
                        "│                         │",
                        "│      www       www      │",
                        "│       w         w       │",
                        "│     wwwww     wwwww     │",
                        "│ ♠    www       www    ♠ │",
                        "│ 6     w         w     6 │",
                        "│                         │",
                        "└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘" ]

    seven_of_spades = [ "┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐",
                        "│                         │",
                        "│ 7     w         w     7 │",
                        "│ ♠    www       www    ♠ │",  
                        "│     wwwww     wwwww     │", 
                        "│       w    w    w       │",
                        "│      www  www  www      │",
                        "│          wwwww          │",
                        "│     w      w      w     │",
                        "│    www    www    www    │",
                        "│   wwwww         wwwww   │",
                        "│     w             w     │",
                        "│    www           www    │",
                        "│                         │",
                        "│      www       www      │",
                        "│       w         w       │",
                        "│     wwwww     wwwww     │",
                        "│ ♠    www       www    ♠ │",
                        "│ 7     w         w     7 │",
                        "│                         │",
                        "└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘" ]

    eight_of_spades = [ "┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐",
                        "│                         │",
                        "│ 8     w         w     8 │",
                        "│ ♠    www       www    ♠ │",  
                        "│     wwwww     wwwww     │", 
                        "│       w    w    w       │",
                        "│      www  www  www      │",
                        "│          wwwww          │",
                        "│     w      w      w     │",
                        "│    www    www    www    │",
                        "│   wwwww         wwwww   │",
                        "│     w     www     w     │",
                        "│    www     w     www    │",
                        "│          wwwww          │",
                        "│      www  www  www      │",
                        "│       w    w    w       │",
                        "│     wwwww     wwwww     │",
                        "│ ♠    www       www    ♠ │",
                        "│ 8     w         w     8 │",
                        "│                         │",
                        "└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘" ]

    nine_of_spades = [  "┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐",
                        "│                         │",
                        "│ 9   w      w      w   9 │",
                        "│ ♠  www    www    www  ♠ │",  
                        "│   wwwww  wwwww  wwwww   │", 
                        "│     w      w      w     │",
                        "│    www    www    www    │",
                        "│                         │",
                        "│     w      w      w     │",
                        "│    www    www    www    │",
                        "│   wwwww  wwwww  wwwww   │",
                        "│     w      w      w     │",
                        "│    www    www    www    │",
                        "│                         │",
                        "│    www    www    www    │",
                        "│     w      w      w     │",
                        "│   wwwww  wwwww  wwwww   │",
                        "│ ♠  www    www    www  ♠ │",
                        "│ 9   w      w      w   9 │",
                        "│                         │",
                        "└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘" ]

    ten_of_spades = [   "┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐",
                        "│                         │",
                        "│ 10  w      w      w  10 │",
                        "│ ♠  www    www    www  ♠ │",  
                        "│   wwwww  wwwww  wwwww   │", 
                        "│     w      w      w     │",
                        "│    www    www    www    │",
                        "│                         │",
                        "│     w      ♠      w     │",
                        "│    www           www    │",
                        "│   wwwww   TEN   wwwww   │",
                        "│     w             w     │",
                        "│    www     ♠     www    │",
                        "│                         │",
                        "│    www    www    www    │",
                        "│     w      w      w     │",
                        "│   wwwww  wwwww  wwwww   │",
                        "│ ♠  www    www    www  ♠ │",
                        "│ 10  w      w      w  10 │",
                        "│                         │",
                        "└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘" ]

    jack_of_spades = [  "┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐",
                        "│                         │",
                        "│           wwwwwwwwwwww  │",
                        "│           wwwwwwwwwwww  │",  
                        "│              wwwwww     │", 
                        "│              wwwwww     │",
                        "│              wwwwww     │",
                        "│    JACK      wwwwww     │",
                        "│              wwwwww     │",
                        "│     ♠♠       wwwwww     │",
                        "│              wwwwww     │",
                        "│              wwwwww     │",
                        "│              wwwwww     │",
                        "│              wwwwww     │",
                        "│              wwwwww     │",
                        "│  wwwwwwww    wwwwww     │",
                        "│    wwwww    wwwwwww     │",
                        "│     wwwww wwwwwww       │",
                        "│        wwwwwwwww        │",
                        "│                         │",
                        "└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘" ]

    queen_of_spades = [ "┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐",
                        "│                         │",
                        "│       wwwwwww    QUEEN  │",    
                        "│     wwwwwwwwwww         │",             
                        "│   wwww       wwww   ♠♠  │",         
                        "│  wwww         wwww      │",    
                        "│ wwww           wwww     │",        
                        "│ wwww           wwww     │",        
                        "│ wwww           wwww     │",        
                        "│ wwww           wwww     │",         
                        "│ wwww           wwww     │",         
                        "│ wwww           wwww     │",        
                        "│ wwww           wwww     │",
                        "│ wwww           wwww     │",
                        "│ wwww           wwww     │",
                        "│  wwww         wwww      │",
                        "│   wwww       wwwwwwww   │",
                        "│    wwwwwwwwwwww  wwww   │",
                        "│      wwwwwwww     wwww  │",
                        "│                         │",
                        "└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘" ]  

    king_of_spades = [  "┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐",
                        "│                         │",
                        "│ wwwwwwwww     wwwwwww   │",    
                        "│   wwwww        wwwww    │",             
                        "│   wwwww      wwwww      │",         
                        "│   wwwww    wwwww        │",    
                        "│   wwwww  wwwww          │",        
                        "│   wwwwwwww        KING  │",        
                        "│   wwwwwwww              │",         
                        "│   wwwww  wwwww      ♠♠  │",         
                        "│   wwwww    wwwww        │",         
                        "│   wwwww     wwwww       │",        
                        "│   wwwww     wwwww       │",
                        "│   wwwww      wwwww      │",
                        "│   wwwww       wwwww     │",
                        "│   wwwww       wwwww     │",
                        "│   wwwww        wwwww    │",
                        "│   wwwww        wwwww    │",
                        "│ wwwwwwwww     wwwwwww   │",
                        "│                         │",
                        "└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘" ]

    #Variabili
    players_list = []
    group_of_cards_1 = {11 : ace_of_spades,2 : two_of_spades,3 : tree_of_spades,4 : four_of_spades,5 : five_of_spades,6 : six_of_spades,7 : seven_of_spades,8 : eight_of_spades,9 : nine_of_spades,10 : ten_of_spades,10 : jack_of_spades,10 : queen_of_spades,10 : king_of_spades }  
    group_of_cards_2 = {1 : ace_of_spades,2 : two_of_spades,3 : tree_of_spades,4 : four_of_spades,5 : five_of_spades,6 : six_of_spades,7 : seven_of_spades,8 : eight_of_spades,9 : nine_of_spades,10 : ten_of_spades,10 : jack_of_spades,10 : queen_of_spades,10 : king_of_spades }  
    group_of_point = {}
    game_local = True
    rule_local = True
    player_game_1 = True

    #Testi
    text_1 = "Welcome to the new version of Black Jack: 'Black Jack 2.0' made by Lorenzo Poli. if you want to play, firstly, you have to select the game-mode: " 
    text_2 = "type '1' if you want to play a local game"
    text_3 = "type '2' if you want to play an online game"
    text_4 = "type '3' if you want to play a 'single' game (with bots)"
    text_5 = "You select the local game, so now, enter the number of the players... "
    text_6 = "...and then, the name of the players: "
    text_7 = "Rules: Blackjack hands are scored by their point total. The hand with the highest total wins as long as it doesn't exceed 21; a hand with a higher total than 21 is said to bust. Cards 2 through 10 are worth their face value, and face cards (jack, queen, king) are also worth 10."
    text_8 = "P.S. In this version of the game, we only have cards of spades, for time reason"         
    text_9 = "Ok, so the game start now!"
    text_10 = "Sorry, but you overrun"
    text_11 = "Ok, so your turn is over!"
    text_12 = "BlackJack!"
    text_13 = "Ok, the game is finished. Now see the resault: "
    text_14 = "Well, it was a good game. You want to re-play? press '1' for re-playing or press '2' for leaving: "
    text_15 = "Ok, Goodbye!"
    text_16 = "Ok, now, what you want to do? press '1' if you want to read the rules, press '2' if you want to play: "
    text_17 = "so, wich one you want to play? "

    #Definizioni
    def slowprint_1(text, delay, stdscr, newline=True):
        for i in text:
            stdscr.addstr(i)
            stdscr.refresh()
            time.sleep(delay)            
        if newline:
            stdscr.addstr("\n")

    def slowprint_2(text, delay, X, Y, stdscr, newline=False):
        for i in text:
            stdscr.addstr(Y, X, i)
            X += 1
            stdscr.refresh()
            time.sleep(delay)            
        if newline:
            stdscr.addstr("\n")
    
    def slowprint_3(text, delay, Y, X, stdscr, newline=True):
        for i in text:
            stdscr.addstr(Y, X, i)
            Y += 1
            stdscr.refresh()
            time.sleep(delay)            
        if newline:
            stdscr.addstr("\n")

        stdscr.clear()
        
        #Decisione modalità di gioco
        slowprint_3(wallpaper, 0.3, 50, 1)        
        slowprint_1(text_1, 0.05, stdscr)
        slowprint_1(text_2, 0.05, stdscr)
        slowprint_1(text_3, 0.05, stdscr)
        slowprint_1(text_4, 0.05, stdscr)
        slowprint_1(text_17, 0.05, stdscr)
        curses.echo()
        decision_1 = stdscr.getch()   
        stdscr.refresh()

        #Modalita di gioco: Locale
        if decision_1 == 49:
            stdscr.clear()

            while game_local:
                slowprint_1(text_5, 0.05, stdscr)
                stdscr.echo()
                players = stdscr.getch()
                slowprint_1(text_6, 0.05, stdscr)
                stdscr.refresh()
                
            
                #Ciclo 'for' giocatori
                for i in range(players - 48):
                    curses.echo()
                    player = stdscr.getstr()
                    players_list.append(player)

                #Regolamento
                while rule_local:
                    slowprint_2(text_16, 0.05, 0, 1, stdscr)
                    stdscr.echo()
                    decision_2 = stdscr.getch()
                    if decision_2 == 49:
                        slowprint_1(text_7, 0.05, stdscr)
                        slowprint_1(text_8, 0.05, stdscr)
                        stdscr.refresh()
                    if decision_2 == 50:
                        slowprint_1(text_9, 0.05, stdscr)
                        rule_local = False
                        stdscr.refresh()
                    stdscr.refresh()

                #Intro Partita del giocatore
                while player_game_1:
                    stdscr.clear()

                    for i in players_list:
                        player_game_2 = True
                        text_17 = f"{i} what you want to do now? take or stay? press '1' for taking, press '2' for staying: "
                        card_1 = randint(2, 11)
                        card_2 = randint(1, 10)
                        player_card = []
                        X_1 = 31
                        Y_1 = 1
                        X_2 = 0
                        Y_2 = 23
                        X_3 = 22
                        Y_3 = 0
                        card = 0
                        tot = 0
                        tot += card_1
                        tot += card_2
                        player_card.append(card_1)
                        player_card.append(card_2)
                        slowprint_3(group_of_cards_1[card_1], 0.1, 1, 1, stdscr)
                        slowprint_3(group_of_cards_2[card_2], 0.1, X_1, Y_1, stdscr)
                        card += 2
                        stdscr.refresh()
                        if tot == 21:
                            slowprint_3(black_jack, 0.2, 1, 22, stdscr)
                            group_of_point[i] = "BlackJack"
                            player_game_2 = False
                            stdscr.refresh()
                        else:

                            #Partita del giocatore
                            while player_game_2:
                                if card == 5:
                                    Y_1 += 22
                                    Y_2 += 22
                                    Y_3 += 22
                                    card = 0
                                if tot > 21:
                                    if player_card.count(11) == 1:
                                        tot -= 10
                                        player_card.remove(11)
                                if tot > 21:
                                    slowprint_2(text_10, 0.05, X_2, Y_2, stdscr)
                                    group_of_point[i] = tot
                                    player_game_2 = False
                                    break
                                slowprint_2(text_17, 0.05, X_3, Y_3, stdscr)
                                stdscr.echo()
                                decision_3 = stdscr.getch()
                                stdscr.refresh()
                                if decision_3 == 49:
                                    if tot > 10:
                                        X_1 += 30 
                                        card_3 = randint(1, 10)
                                        player_card.append(card_3)
                                        slowprint_3(group_of_cards_2[card_3], 0.1, X_1, Y_1, stdscr)
                                        tot += card_3
                                        card += 1
                                        stdscr.refresh()
                                    else:
                                        X_1 += 30
                                        card_3 = randint(2, 11)
                                        player_card.append(card_3)
                                        slowprint_3(group_of_cards_1[card_3], 0.1, X_1, Y_1, stdscr)
                                        tot += card_3
                                        card += 1
                                        stdscr.refresh()
                                        
                                else:
                                    slowprint_2(text_11, X_2, Y_2, stdscr)
                                    group_of_point[i] = tot
                                    player_game_2 = False
                                    stdscr.refresh()
                    player_game_1 = False
                    stdscr.refresh()

                #Finale-partita locale
                stdscr.clear()
                
                slowprint_2(text_13, 0.05, 0, 1, stdscr)
                stdscr.refresh()
                
                for i in players_list:
                    text_18 = f"{i} arrived at: {group_of_point[i]}"
                    slowprint_1(text_18, 0.05, stdscr)
                    stdscr.refresh()
                
                slowprint_1(text_14, 0.05, stdscr)
                decision_4 = stdscr.getch()
                stdscr.refresh()
                
                if decision_4 == 50:
                    slowprint_1(text_15, 0.1, stdscr)
                    game_local = False
                stdscr.refresh()
wrapper(main)
