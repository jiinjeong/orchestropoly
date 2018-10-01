"""
 *****************************************************************************
   FILE: game.py

   AUTHOR: Jiin Jeong

   ASSIGNMENT: Final Project - Final Version (Game)

   DATE: December 3, 2017

   DESCRIPTION: This program creates a visual Monopoly board game,
   specifically an Orchestropoly, for three players.
   For further information, read the instructions after running the program.

   The following rules are implemented:

   1) ROLL DICE
   2) DOUBLES : Rolls again when you get a double.
   Three doubles sends player to jail.
   3) SWITCH PLAYER : Players can be switched.

   4) GO TO JAIL : Goes to jail when it lands on jail tile.
   5) TAX : Pays tax on the tax tiles.
   6) COLLECT SALARY : Collects $200 every time player passes "go."
   7) FREE PARKING : Player on "free parking" cannot collect rent even if
   other player lands on his property.

   8) BUY : Players can buy properties.
   Bought property and player cash can be seen on player's property box.
   9) HIRE : Player can hire musicians and section leaders.
   10) PAY RENT : Player pays rent to owner, depending on
   the # of musicians/leader hired, and # of Facility/Music Hall owned.

   11) DRAW : Player can draw a random Chest or Chance card from the stack.
   Exact functions for each card are not yet implemented.

   12) NEW GAME / INSTRUCTIONS : Player can start a new game and read the
   instructions of Orchestropoly. (Slight bug in NEW GAME - will not
   remove the musicians/section leaders from the board.)
   13) END GAME / WINNER : When a player becomes bankrupt, the player
   is removed from the game. Declares last remaining player as the winner.

   * BID is not yet implemented.

 *****************************************************************************
"""

import random
from cs110graphics import *
import json


class Game():
    """ Game. """

    def __init__(self, win):

        self._win = win

        # CITE : Professor Perkins
        # DESC : Helped understand how to import data from a json file.
        tile_dic = read_data()
        self._tile_list = tile_dic['tiles']
        self._chestcard_list = tile_dic['chestcards']
        self._chancecard_list = tile_dic['chancecards']

        # Creates all the tiles in the Monopoly board.
        for piece in self._tile_list:
            Tile(win, piece['file'], piece['width'],
                 piece['height'], piece['location'])

        # Designs details of the Monopoly board.
        design = [Image(win, "./img/monopoly.jpg",
                        450, 280, (800, 420)),  # logo
                  Image(win, "./img/chest.jpg",
                        200, 180, (640, 220)),  # chest
                  Image(win, "./img/chance.jpg",
                        200, 180, (960, 570)),  # chance
                  Image(win, "./img/author.jpg",
                        175, 40, (1280, 745))]  # author
        for elements in design:
            self._win.add(elements)

        # Creates two graphic dice with pips.
        self._die1 = Die(win, (1250, 370))
        self._die2 = Die(win, (1325, 370))

        # Places players in different starting positions since to not overlap.
        start_x, start_y = self._tile_list[0]['location']
        self._start_pos1 = (start_x, start_y)
        self._start_pos2 = (start_x - 10, start_y + 20)
        self._start_pos3 = (start_x - 10, start_y - 20)

        # Creates players for the game.
        self._player1 = Player(self, win, 1, "Beethoven",
                               "./img/beethoven.jpg",
                               self._start_pos1, (200, 150))
        self._player2 = Player(self, win, 2, "Mozart", "./img/mozart.jpg",
                               self._start_pos2, (200, 400))
        self._player3 = Player(self, win, 3, "Socrates", "./img/socrates.jpg",
                               self._start_pos3, (200, 650))
        self._player_list = [self._player1, self._player2, self._player3]

        # Player 1 starts.
        self._cur_player = self._player_list[0]

        # Makes an icon at the right bottom of the page
        # that displays which player is current player.
        self._win.add(Text(win, "Current player: ",
                           center=(1286, 663), size=12))
        self._show_cur_plyr = Image(win, self._cur_player._file,
                                    30, 38, (1280, 700))
        self._win.add(self._show_cur_plyr)

        # Creates visual buttons for the game.
        NewGame(self, win, "New Game", 130, 40, (1288, 100), "crimson")
        Instructions(self, win, "Instructions",
                     130, 40, (1288, 160), "crimson")
        HireButton(self, win, "Hire", 100, 40, (1288, 240), "salmon")
        RollButton(self, win, "Roll", 100, 40, (1288, 300), "salmon")

        # Instead of your turn ending automatically after you roll a dice,
        # you use an end turn button to end your turn since later on,
        # you might want to build/sell/etc your properties during your turn.
        EndTurn(self, win, "End Turn", 100, 40, (1288, 440), "salmon")

        # Adds a status box which will display status of the game.
        self._status = "Start the game!"
        self._status_box = Rectangle(self._win, 130, 70, (1285, 565))
        self._status_txt = Text(self._win, self._status,
                                center=(1285, 565), size=12)
        self._win.add(self._status_box)
        self._win.add(self._status_txt)

    def switch(self):
        """ Switches the players. """

        # Removes current player icon since we need a new current player icon.
        self._win.remove(self._show_cur_plyr)

        # This will work even with >2 players.
        for i in range(len(self._player_list)):
            if self._cur_player == self._player_list[i]:
                self._cur_player = self._player_list[(i + 1) %
                                                     len(self._player_list)]

                # Replaces current player icon with the new current player.
                self._show_cur_plyr = Image(self._win, self._cur_player._file,
                                            30, 38, (1280, 700))
                self._win.add(self._show_cur_plyr)

                # CITE : Teaching Assistant Sam
                # DESC : Suggested using a return statement
                # to break out of the for loop.
                return self._cur_player

    def double(self):
        """ Checks if the two values on the dice are the same. """

        jail_x, jail_y = self._tile_list[10]['location']

        # Adds one to double counter.
        if self._die1.get_value() == self._die2.get_value():
            self._cur_player._double += 1

            # Sends player to jail when they get double.
            if self._cur_player._double == 3:
                self._cur_player._body.move_to((jail_x, jail_y))
                self._cur_player._index = 10
                self._status = "  3 Doubles! \n You go to jail."
                self.update_status()
            else:
                self._status = "   Double! \n Roll again."
                self.update_status()
        else:
            self._status = "End turn."
            self.update_status()

    def update_status(self):
        self._status_txt.set_text(self._status)


class Tile():
    """ Constructs the tiles of the Monopoly board. """

    def __init__(self, win, file, width, height, center):

        self._win = win
        self._file = file
        self._width = width
        self._height = height

        # Have to get x and y individually since json converts a tuple
        # into [] list formatting and cs110graphics requires
        # a tuple for a center.
        self._x, self._y = center

        # Creates the tiles with appropriate boundary and images.
        self._body = Rectangle(win, width, height, (self._x, self._y))
        self._image = Image(win, file, width - 2, height - 2,
                            (self._x, self._y))
        self._win.add(self._body)
        self._win.add(self._image)


# CITE : Professor Campbell
# DESC : Code for creating a visual die with pips.
class Die():
    """ Creates a die. """

    # Number of sides of the die.
    SIDES = 6
    # Positions for the pips of the die.
    POSITIONS = [None,
                 [(0, 0), None, None, None, None, None],
                 [(-.25, .25), (.25, -.25), None, None, None, None],
                 [(-.25, .25), (.25, -.25), (0, 0), None, None, None],
                 [(-.25, .25), (.25, -.25), (.25, .25),
                  (-.25, -.25), None, None],
                 [(-.25, .25), (.25, -.25), (.25, .25),
                  (-.25, -.25), (0, 0), None],
                 [(-.25, .25), (.25, -.25), (.25, .25),
                  (-.25, -.25), (-.25, 0), (.25, 0)]]

    def __init__(self, win, center, width=50):
        """ Constructor. """

        self._win = win
        self._center = center
        self._width = width

        # Sets the default rolled number to 1.
        self._rollnum = 1

        # Makes the red square body of the die.
        self._square = Square(win, width, center)
        self._square.set_fill_color("red")
        self._square.set_depth(20)

        # Makes the white pips of the die.
        self._pips = []
        for _ in range(Die.SIDES):
            pip = Circle(win, round(width / 20), center)
            pip.set_fill_color("white")
            pip.set_border_color("white")
            pip.set_depth(20)
            self._pips.append(pip)

        # Adds the dice graphic to the window.
        self.addTo(win)

    def addTo(self, win):
        """ Adds the square body and the pips to the graphics window. """

        win.add(self._square)
        for pip in self._pips:
            win.add(pip)

    def roll(self):
        """ Resets the die's value randomly. """

        self._rollnum = random.randint(1, Die.SIDES)
        self.update()

    def get_value(self):
        """ Gets the value of the rolled number. """

        return self._rollnum

    def update(self):
        """ Updates the pips and the number rolled. """

        # Checks the rolled number and determines the pips to display.
        positions = Die.POSITIONS[self._rollnum]
        cx, cy = self._center
        for i in range(len(positions)):
            if positions[i] is None:
                self._pips[i].set_depth(25)
            else:
                self._pips[i].set_depth(15)
                dx, dy = positions[i]
                self._pips[i].move_to((round(cx + dx * self._width),
                                       round(cy + dy * self._width)))


class TileCard(EventHandler):
    """ Creates TileCard to pop up when player lands on the tile. """

    def __init__(self, game, win, tile):

        EventHandler.__init__(self)

        self._game = game
        self._win = win
        self._tile = tile

        # Makes the card.
        self._card = Rectangle(self._win, 512, 312, (800, 500))
        self._win.add(self._card)
        self._info = []

        # Divides the card into two sections (left/right).
        self._infobox = Rectangle(self._win, 242, 312, (665, 500))
        self._win.add(self._infobox)

        # X button to close the window.
        self._xbutton = Image(self._win, "./img/x.jpg", 20, 20, (1040, 360))
        self._win.add(self._xbutton)
        self._xbutton.add_handler(self)

        # Creates instrument info cards.
        if self._tile['type'] == 'instruments':
            self._label = Rectangle(self._win, 242, 50, (665, 369))
            self._win.add(self._label)
            self._label.set_fill_color(tile['color'])

            self._info = [Text(win, tile['name'],
                               center=(664, 370), size=18),  # name
                          Text(win, "Pay $%s" % tile['pay'],
                               center=(660, 420), size=14),
                          Text(win, "With 1 musician $%s" % tile['pay_1hire'],
                               center=(660, 460), size=12),
                          Text(win, "With 2 musician $%s" % tile['pay_2hire'],
                               center=(660, 490), size=12),
                          Text(win, "With 3 musician $%s" % tile['pay_3hire'],
                               center=(660, 520), size=12),
                          Text(win, "With 4 musician $%s" % tile['pay_4hire'],
                               center=(660, 550), size=12),
                          Text(win, "With section leader $%s" %
                               tile['pay_leader'], center=(660, 580), size=12),
                          Text(win, "Musicians cost $%s each" %
                               tile['price_hire'], center=(662, 630), size=14),
                          Text(win, "Welcome to \n <%s>!" % tile['name'],
                               center=(920, 440), size=16)]  # Welcomes users.

        # Creates music hall info cards.
        elif self._tile['type'] == 'musichalls':
            self._label = Rectangle(self._win, 242, 50, (665, 369))
            self._win.add(self._label)
            self._label.set_fill_color("silver")

            self._info = [Text(win, self._tile['name'],
                               center=(664, 370), size=18),  # name
                          Image(win, "./img/musichall.jpg",
                                90, 65, (664, 440)),
                          Text(win, "PAY $%s" % tile['pay'],
                               center=(660, 500), size=14),
                          Text(win, "When 2 m.h's are owned   $%s" %
                               (self._tile['pay'] * 2),
                               center=(660, 530), size=12),
                          Text(win, "When 3 m.h's are owned   $%s" %
                               (self._tile['pay'] * 4),
                               center=(662, 560), size=12),
                          Text(win, "When 4 m.h's are owned   $%s" %
                               (tile['pay'] * 8), center=(662, 590), size=12),
                          Text(win, "Welcome to \n <%s>!" % tile['name'],
                               center=(920, 440), size=16)]

        # Creates facilities info cards.
        elif self._tile['type'] == 'facilities':
            self._label = Rectangle(self._win, 242, 50, (665, 369))
            self._win.add(self._label)
            self._label.set_fill_color("silver")

            # Cannot use \n since this line break character messes up
            # with the indentation of the text displayed.
            self._info = [Text(win, self._tile['name'],
                               center=(664, 370), size=18),  # name
                          Text(win, "If one Facility is owned,",
                               center=(660, 420), size=12),
                          Text(win, "rent is 4 times",
                               center=(660, 445), size=12),
                          Text(win, "amount shown on dice",
                               center=(660, 470), size=12),
                          Text(win, "If both Facilities are owned,",
                               center=(660, 515), size=12),
                          Text(win, "rent is 10 times",
                               center=(660, 540), size=12),
                          Text(win, "amount shown on dice.",
                               center=(660, 565), size=12),
                          Text(win, "Welcome to \n <%s>!" % tile['name'],
                               center=(920, 440), size=16)]

        # Creates jail info card.
        elif self._tile['type'] == 'jail':
            self._info = [Text(win, "Uh-oh!", center=(660, 370), size=22),
                          Text(win, "You are in jail.",
                               center=(660, 420), size=18),
                          Image(win, "./img/jail.jpg", 200, 110, (660, 550))]

        # Creates chest and chance info cards.
        elif self._tile['type'] == 'chest' or self._tile['type'] == 'chance':
            self._info = [Text(win, "Test your luck!",
                               center=(664, 370), size=20),
                          Image(win, "./img/luck.jpg", 220, 150, (660, 480)),
                          Text(win, "        Follow \n the instructions",
                               center=(660, 590), size=14),
                          Text(win, "on the card.",
                               center=(660, 627), size=14)]

            self._drawbutton = DrawButton(self, game, win, "Draw",
                                          150, 50, (920, 420), "teal")

        # Allows player to buy instruments, musichalls, and facilities
        # by creating a buy/bid button. Bid button is not implemented.
        if self._tile['type'] == 'instruments' or \
           self._tile['type'] == 'musichalls' \
           or self._tile['type'] == 'facilities':

            # Checks if property if already bought.
            if not self._tile['bought_status']:

                # Checks if player has enough money.
                if self._game._cur_player._cash >= tile['price_buy']:
                    self._buybutton = BuyButton(game, win, "Buy",
                                                150, 50, (920, 520), "teal")
                    self._bidbutton = Button(game, win, "Auction",
                                             150, 50, (920, 580), "teal")

                # Cash warning.
                elif self._game._cur_player._cash < tile['price_buy']:
                    self._info.append(Text(win, "You don't have enough cash.",
                                           center=(920, 500), size=14))

            # Already bought warning.
            elif self._tile['bought_status']:
                self._info.append(Text(win, "This property is already bought.",
                                       center=(920, 500), size=14))

        # TileCard for "go."
        if self._tile['id'] == 0:
            self._info = [Image(win, "./img/gologo.jpg", 150, 90, (660, 405)),
                          Image(win, "./img/go.jpg", 200, 150, (660, 540)),
                          Text(win, "Collect $200 \nas you pass.",
                               center=(920, 510), size=18)]

        # TileCard for "free parking."
        if self._tile['id'] == 20:
            self._info = [Image(win, "./img/parking.jpg",
                                200, 280, (660, 500)),
                          Text(win, "Free resting place",
                               center=(920, 420), size=18),
                          Text(win, "Cannot receive money,",
                               center=(920, 500), size=14),
                          Text(win, "property, or reward.",
                               center=(920, 530), size=14)]

        for i in self._info:
            self._win.add(i)

    def remove(self):
        """ Removes the card from the screen. """

        self._win.remove(self._card)
        self._win.remove(self._xbutton)
        self._win.remove(self._infobox)

        for i in self._info:
            self._win.remove(i)

        # Only removes the things you added to the win.
        if self._tile['type'] == 'instruments' or \
           self._tile['type'] == 'musichalls' or \
           self._tile['type'] == 'facilities':
            self._win.remove(self._label)

            if not self._tile['bought_status']:
                if self._game._cur_player._cash >= self._tile['price_buy']:
                    self._win.remove(self._buybutton._body)
                    self._win.remove(self._buybutton._text)
                    self._win.remove(self._bidbutton._body)
                    self._win.remove(self._bidbutton._text)

        elif self._tile['type'] == 'chest' or self._tile['type'] == 'chance':
            self._win.remove(self._drawbutton._body)
            self._win.remove(self._drawbutton._text)

    def handle_mouse_press(self, _):
        """ Removes the card and the info on it when pressed. """

        self.remove()


class Player():
    """ Creates players for this game. """

    # CITE : Teaching Assistant Paul
    # DESC : Suggested calling this class in game and passing game (self)
    # as a parameter to use the attributes stored in game.
    def __init__(self, game, win, idnum, name, file, center, pbcenter,
                 width=30, height=38, index=0):

        self._game = game
        self._win = win
        self._id = idnum
        self._name = name
        self._file = file
        self._x, self._y = center[0], center[1]

        # Visually creates the player.
        self._body = Image(win, file, width, height, (self._x, self._y))
        self._win.add(self._body)

        # Keeps track of the position of the player on the board.
        self._index = index

        # Counter for number of doubles rolled.
        self._double = 0

        self._die1 = game._die1
        self._die2 = game._die2
        self._tile_list = game._tile_list

        # Material properties of the player.
        self._cash = 1500  # Starts with $1500 default cash.
        self._ownedprop = []
        self._facilities = 0
        self._musichalls = 0
        self._jail_cards = 0  # Not yet implemented.
        self._jail_turns = 0  # Not yet implemented.

        # Creates playerbox that keeps track of properties and cash.
        self._pbx, self._pby = pbcenter[0], pbcenter[1]
        self._playerbox = PlayerBox(self, win)

    def move(self):
        """ Moves the token to a position. """

        self._index = (self._index + self._die1.get_value() +
                       self._die2.get_value())

        # Receives $200 in salary when player passes the "Go" tile.
        if self._index >= 40:
            self._cash += 200
            self._index -= 40
            # Updates the playerbox.
            self._playerbox.update()

        self._tile_landed = self._tile_list[self._index]
        new_x, new_y = self._tile_landed['location']
        self._body.move_to((new_x, new_y))

        # Pays tax.
        if self._index == self._tile_list[4]['id']:
            self._cash -= 200
            self._playerbox.update()
        elif self._index == self._tile_list[38]['id']:
            self._cash -= 75
            self._playerbox.update()

        # Sends the token to jail when it lands on jail.
        elif self._index == self._tile_list[30]['id']:
            jail_x, jail_y = self._tile_list[10]['location']
            self._body.move_to((jail_x, jail_y))

        else:
            # Opens the TileCard.
            self._cur_propcard = TileCard(self._game,
                                          self._win, self._tile_landed)

        if self._tile_landed['type'] == 'instruments' or \
           self._tile_landed['type'] == 'musichalls' or \
           self._tile_landed['type'] == 'facilities':

            # Gets a list of the names of tiles in the player's
            # owned property.
            tile_name = []
            for tile in self._ownedprop:
                tile_name.append(tile['name'])

            # If the name of landed tile is not in the list of
            # names of player's owned property, and the tile is bought,
            # the player should pay rent to the owner.
            if self._tile_landed['bought_status']:
                if self._tile_landed['name'] not in tile_name:
                    self.pay_rent()

    def buy(self):
        """ Buys the property. """

        self._tile_landed['bought_status'] = True
        self._ownedprop.append(self._tile_landed)
        self._cash -= self._tile_landed['price_buy']
        self._playerbox.update()

        # Counter for facilities and music halls
        # so we can know how much rent to charge.
        if self._tile_landed['type'] == 'facilities':
            self._facilities += 1
        elif self._tile_landed['type'] == 'musichalls':
            self._musichalls += 1

        # Have to remove one by one since remove only works on graphic objects,
        # and BuyButton is an object with an Eventhandler.
        self._win.remove(self._cur_propcard._buybutton._body)
        self._win.remove(self._cur_propcard._buybutton._text)
        self._win.remove(self._cur_propcard._bidbutton._body)
        self._win.remove(self._cur_propcard._bidbutton._text)

        # Displays a congratulations message!
        self._congrats = Text(self._win,
                              " Congratulations! :D \n You bought %s!"
                              % (self._tile_landed['name']),
                              center=(920, 540), size=14)
        self._win.add(self._congrats)
        # Appends to the info attribute of the appropriate property card
        # since we want to remove it from the screen along with other info.
        self._cur_propcard._info.append(self._congrats)

    def pay_rent(self):
        """ Pays rent. """

        self._rollednum = self._die1.get_value() + self._die2.get_value()
        self._owner = self.get_owner()

        # If the owner is in 20 (free parking), he can't receive rent.
        if self._owner._index != 20:

            # Rent differs depending on how many musicians there are.
            if self._tile_landed['type'] == 'instruments':
                if self._tile_landed['musician'] == 0:
                    self._cash -= self._tile_landed['pay']
                    self._owner._cash += self._tile_landed['pay']
                elif self._tile_landed['musician'] == 1:
                    self._cash -= self._tile_landed['pay_1hire']
                    self._owner._cash += self._tile_landed['pay_1hire']
                elif self._tile_landed['musician'] == 2:
                    self._cash -= self._tile_landed['pay_2hire']
                    self._owner._cash += self._tile_landed['pay_2hire']
                elif self._tile_landed['musician'] == 3:
                    self._cash -= self._tile_landed['pay_3hire']
                    self._owner._cash += self._tile_landed['pay_3hire']
                elif self._tile_landed['musician'] == 4:
                    self._cash -= self._tile_landed['pay_4hire']
                    self._owner._cash += self._tile_landed['pay_4hire']
                elif self._tile_landed['leader'] == 1:
                    self._cash -= self._tile_landed['pay_leader']
                    self._owner._cash += self._tile_landed['pay_leader']

            elif self._tile_landed['type'] == 'facilities':

                # When one facility is owned, rent is 4 times
                # the number rolled on dice.
                if self._owner._facilities == 1:
                    self._cash -= self._rollednum * self._tile_landed['pay_1']
                    # Have to use line break because even though arithmetic
                    # usually works without one, this gave me an indent error.
                    self._owner._cash += self._rollednum * \
                                         self._tile_landed['pay_1']

                # When two is owned, rent is 10 times rolled number.
                elif self._owner_facitilies == 2:
                    self._cash -= self._rollednum * self._tile_landed['pay_2']
                    self._owner._cash += self._rollednum *\
                                         self._tile_landed['pay_2']

            # When one music hall is owned, rent is $25 * 1 = $25.
            # When two is owned, rent is $25 * 2^1 = $50. When three is owned,
            # rent: $25 * 2^2 = $100. Four owned, rent: $25 * 2^3 = $200.
            elif self._tile_landed['type'] == 'musichalls':
                self._cash -= self._tile_landed['pay'] *\
                              (2 ** (self._owner._musichalls - 1))
                self._owner._cash += self._tile_landed['pay'] *\
                                (2 ** (self._owner._musichalls - 1))

        # Update player and the owners' playerboxes to reflect changes.
        self._playerbox.update()
        self._owner._playerbox.update()

    def my_property(self):
        """ Visually shows the player's property. """

        self._clickable = []

        # Puts a circle on the center of every tile a player possesses.
        for tile in self._ownedprop:
            self._x, self._y = tile['location']
            self._clickable.append(Clickable(self, self._win, 10,
                                             (self._x, self._y),
                                             "springgreen"))

    def hide_my_property(self):
        """ Hides the player's property. """

        for circle in self._clickable:
            self._win.remove(circle._body)

    def get_owner(self):
        """ Returns the owner of a property. """

        # Looks through the owned property of every players
        # and returns the player (owner) who has it.
        for player in self._game._player_list:
            for tile in player._ownedprop:
                if self._tile_landed == tile:
                    return player

    def check_bankruptcy(self):
        """ Checks for bankruptcy. """

        # If cash is less than 0, player is bankrupt.
        if self._cash < 0:
            if len(self._game._player_list) == 3:
                del self._game._player_list[(self._id - 1)]

            # Finds the index of the bankrupt player,
            # and since there is only one player left,
            # displays the EndGame screen.
            elif len(self._game._player_list) == 2:
                for i in self._game._player_list:
                    if i == self:
                        index = self._game._player_list.index(i)
                        del self._game._player_list[index]
                        self._winner = self._game._player_list[0]

                        # EndGame screen.
                        self._endscreen = Rectangle(self._win,
                                                    1000, 750,
                                                    (700, 400))
                        self._endscreen.set_fill_color("olive")
                        self._endscreen.set_border_color("olive")
                        self._win.add(self._endscreen)
                        self._win.add(Text(self._win, "Player %s" %
                                           (self._winner._id),
                                           center=(700, 350),
                                           size=40))
                        self._win.add(Text(self._win, "won the game!",
                                           center=(700, 420),
                                           size=40))

            # Sets the game's current player to next person.
            self._game._cur_player = \
                self._game._player_list[self._id %
                len(self._game._player_list)]

            # Graphically removes player from the board.
            self._win.remove(self._body)

            # Displays bankruptcy message.
            self._playerbox._title.set_text("Player %s is bankrupt."
                                            % self._id)

            # Unbuys all the player's owned property.
            for tile in self._ownedprop:
                tile['bought_status'] = False


class PlayerBox():
    """ Make it in player. """

    def __init__(self, player, win):

        self._win = win
        self._player = player
        self._x, self._y = player._pbx, player._pby

        # Creates a playerbox for the player.
        self._body = Rectangle(win, 300, 200, (self._x, self._y))
        self._win.add(self._body)
        self._label = Rectangle(win, 300, 50, (self._x, self._y - 100))
        self._label.set_fill_color("peru")
        self._win.add(self._label)
        self._title = Text(win, "Player %s: " % self._player._id +
                           self._player._name, center=(self._x, self._y - 100),
                           size=15)
        self._win.add(self._title)

        # Displays which properties and how much cash a player has.
        self._propname = ""

        self._propdisplay = Text(win, "Property: %s" % (self._propname),
                                 center=(self._x, self._y), size=12)
        self._cashdisplay = Text(win, "Cash: $ %s" % (self._player._cash),
                                 center=(self._x - 20, self._y + 80), size=16)
        self._win.add(self._propdisplay)
        self._win.add(self._cashdisplay)

    def update(self):
        """ Updates the playerbox to reflect current property and cash. """

        # Have to reset to empty string, otherwise, it will
        # reprint the previous elements as well.
        self._propname = ""
        for tile in self._player._ownedprop:
            self._propname += tile['name'] + ". "

        self._propdisplay.set_text("Property: %s" % (self._propname))
        self._cashdisplay.set_text("Cash: $ %s" % (self._player._cash))


class Button(EventHandler):
    """ Creates buttons to handle tasks. """

    def __init__(self, game, win, label, width, height, center, color):
        """ Constructs a button. """

        self._game = game
        self._win = win
        self._label = label
        self._width = width
        self._height = height
        self._center = center
        self._color = color

        # Graphically makes the rectangle button with text
        # and adds it to the window.
        self._body = Rectangle(win, width, height, center)
        self._body.set_fill_color(color)
        self._text = Text(win, label, center=center, size=18)
        self._win.add(self._body)
        self._win.add(self._text)

        # Adds handler for the button.
        self._body.add_handler(self)
        # CITE : Professor Perkins
        # DESC : Suggested adding a handler for the button's text so that
        # button will be clickable everywhere inside the button.
        self._text.add_handler(self)


class HireButton(Button):
    """ This button will show you all your owned property by placing
    a clickable circular object on the circle of each.
    You can then use this clickable object to choose which instrument
    you want to hire a musician/section leader for. """

    def __init__(self, game, win, label, width, height, center, color):

        Button.__init__(self, game, win, label, width, height, center, color)

        self._game = game

    def handle_mouse_press(self, _):

        self._game._cur_player.my_property()


class Clickable(EventHandler):
    """ Creates a clickable button for selecting things. """

    def __init__(self, player, win, radius, center, color):

        self._player = player
        self._win = win
        self._radius = radius
        self._center = center
        self._color = color

        # Makes a clickable circle.
        self._body = Circle(win, radius, center)
        self._body.set_border_color(self._color)
        self._win.add(self._body)
        self._body.add_handler(self)

    def handle_mouse_press(self, _):
        """ Fills the circle and opens a hire confirm screen when clicked. """

        self._body.set_fill_color(self._color)
        HireConfirm(self._player, self._win, _.get_mouse_location())


class HireConfirm():
    """ Creates a hire confirm window. """

    def __init__(self, player, win, mouse_loc):

        self._player = player
        self._win = win
        self._mouse_loc = mouse_loc

        for tile in self._player._ownedprop:

            # Gets the location of the mouse clicked, and finds which tile
            # was clicked. The mouse click range for each tile is 10
            # because the radius of the fillable is 10 and the user
            # can click anywhere between that range.
            if (tile['location'][0] - 10, tile['location'][1] - 10) < \
               self._mouse_loc < \
               (tile['location'][0] + 10, tile['location'][1] + 10):
                self._clicked_tile = tile

        # Pops up a screen that asks if you want to hire a musician
        # and player can click "Yes" or "No."
        if self._clicked_tile['type'] == 'instruments':
            self._confirm = [Rectangle(self._win, 512, 312, (800, 500)),
                             Text(self._win, "Do you want to hire a musician",
                                  center=(800, 400), size=16),
                             Text(self._win, "for %s?"
                                  % (self._clicked_tile['name']),
                                  center=(800, 440), size=16)]

            self._yes = YesHire(self, self._win, self._player,
                                "Yes", 70, 50, (750, 520), "plum")
            self._no = NoHire(self, self._win, self._player,
                              "No", 70, 50, (850, 520), "plum")

        # Makes sure that the player hires musicians only for instruments,
        # not for facilities and music halls.
        else:
            self._confirm = [Rectangle(self._win, 512, 312, (800, 500)),
                             Text(self._win, "Musicians are not purchasable",
                                  center=(800, 400), size=16),
                             Text(self._win, "for this property.",
                                  center=(800, 440), size=16)]
            self._okay = NoHire(self, self._win, self._player, "Okay",
                                70, 50, (800, 520), "plum")

        for elements in self._confirm:
            self._win.add(elements)

    def remove(self):
        """ Closes the Hire Confirm window. """

        for elements in self._confirm:
            self._win.remove(elements)

        if self._clicked_tile['type'] == 'instruments':
            self._win.remove(self._yes._body)
            self._win.remove(self._yes._text)
            self._win.remove(self._no._body)
            self._win.remove(self._no._text)
        else:
            self._win.remove(self._okay._body)
            self._win.remove(self._okay._text)


class YesHire(Button):
    """ Confirms the hiring of a musician/section leader. """

    def __init__(self, game, win, player, label, width, height, center, color):

        Button.__init__(self, game, win, label, width, height, center, color)

        self._screen = game
        self._clicked_tile = game._clicked_tile
        self._player = player

    def hire(self):
        """ Hires musicians and leaders, and graphically displays them
        on the board. """

        # After 4 musicians, hires a section leader.
        if self._clicked_tile['musician'] == 4:
            self._clicked_tile['musician'] -= 4
            self._clicked_tile['leader'] += 1
        elif self._clicked_tile['musician'] <= 3:
            self._clicked_tile['musician'] += 1

        self._player._cash -= self._clicked_tile['price_hire']
        self._player._playerbox.update()

        self.update()

    def update(self):
        """ Updates the musicians/leader shown on the board. """

        self._x, self._y = self._clicked_tile['location']

        # Different center range for horizontal and vertical tiles
        # to place the musician graphical icon nicely.
        if 0 < self._clicked_tile['id'] < 10 or \
           20 < self._clicked_tile['id'] < 30:

            # Different placement for each musician icon
            # so the icon won't overlap.
            if self._clicked_tile['musician'] == 1:
                self._win.add(Image(self._win, "./img/music.jpg", 20, 40,
                                    (self._x - 10, self._y - 20)))

            elif self._clicked_tile['musician'] == 2:
                self._win.add(Image(self._win, "./img/music.jpg", 20, 40,
                                    (self._x - 10, self._y + 20)))

            elif self._clicked_tile['musician'] == 3:
                self._win.add(Image(self._win, "./img/music.jpg", 20, 40,
                                    (self._x + 10, self._y - 20)))

            elif self._clicked_tile['musician'] == 4:
                self._win.add(Image(self._win, "./img/music.jpg", 20, 40,
                                    (self._x + 10, self._y + 20)))

            elif self._clicked_tile['leader'] == 1:
                self._win.add(Image(self._win, "./img/leader.jpg", 40, 30,
                                    (self._x, self._y)))

        else:
            if self._clicked_tile['musician'] == 1:
                self._win.add(Image(self._win, "./img/music.jpg", 20, 40,
                                    (self._x - 20, self._y - 10)))

            elif self._clicked_tile['musician'] == 2:
                self._win.add(Image(self._win, "./img/music.jpg", 20, 40,
                                    (self._x - 20, self._y + 10)))

            elif self._clicked_tile['musician'] == 3:
                self._win.add(Image(self._win, "./img/music.jpg", 20, 40,
                                    (self._x + 20, self._y - 10)))

            elif self._clicked_tile['musician'] == 4:
                self._win.add(Image(self._win, "./img/music.jpg", 20, 40,
                                    (self._x + 20, self._y + 10)))

            elif self._clicked_tile['leader'] == 1:
                self._win.add(Image(self._win, "./img/leader.jpg", 40, 30,
                                    (self._x, self._y)))

    def handle_mouse_press(self, _):
        """ Closes confirm screen, hides current property options,
        and hires a musician/section leader. """

        self._screen.remove()
        self._player.hide_my_property()
        self.hire()


class NoHire(Button):
    """ Closes the hire screen and hides the current property options. """

    def __init__(self, game, win, player, label, width, height, center, color):

        Button.__init__(self, game, win, label, width, height, center, color)

        self._screen = game
        self._player = player

    def handle_mouse_press(self, _):
        """ Removes hire screen, and hides property options. """

        self._screen.remove()
        self._player.hide_my_property()


class BuyButton(Button):
    """ Makes a button that buys property when clicked. """

    def __init__(self, game, win, label, width, height, center, color):

        Button.__init__(self, game, win, label, width, height, center, color)

    def handle_mouse_press(self, _):
        """ Buys the property. """

        self._game._cur_player.buy()


class DrawButton(Button):
    """ Makes a button that draws a card when clicked. """

    def __init__(self, card, game, win, label, width, height, center, color):

        Button.__init__(self, game, win, label, width, height, center, color)

        self._win = win
        self._tilecard = card

    def handle_mouse_press(self, _):
        """ Draws from either the chest card or the chance card stack
        when clicked, depending on the type. """

        if self._tilecard._tile['type'] == 'chest':
            chestcard = random.choice(self._game._chestcard_list)
            self._card = Image(self._win, chestcard['file'],
                               200, 120, (920, 550))
            self._win.add(self._card)
            # Appends the chestcard to card info so that it will be removed
            # with other tile card objects when the x button is clicked.
            self._tilecard._info.append(self._card)

        elif self._tilecard._tile['type'] == 'chance':
            chancecard = random.choice(self._game._chancecard_list)
            self._card = Image(self._win, chancecard['file'],
                               200, 120, (920, 550))
            self._win.add(self._card)
            self._tilecard._info.append(self._card)


class NewGame(Button):
    """ Initializes the game back to the default state.
    One bug is that it does not get rid of the musicians/leader
    you bought on the board. """

    def __init__(self, game, win, label, width, height, center, color):

        Button.__init__(self, game, win, label, width, height, center, color)

    def handle_mouse_press(self, _):
        """ Starts a new game. """

        # Initializes the die.
        self._game._die1._rollnum = 1
        self._game._die2._rollnum = 1
        self._game._die1.update()
        self._game._die2.update()

        # Initializes the status message.
        self._game._status = "Start the game!"
        self._game.update_status()

        # Unbuys all properties.
        for tile in self._game._tile_list:
            tile['bought_status'] = False
            tile['musician'] = 0
            tile['leader'] = 0

        # Puts the players back to their appropriate starting position.
        self._game._player1._body.move_to(self._game._start_pos1)
        self._game._player2._body.move_to(self._game._start_pos2)
        self._game._player3._body.move_to(self._game._start_pos3)

        # Initializes the player properties.
        for player in self._game._player_list:
            player._index = 0
            player._cash = 1500
            player._double = 0
            player._facilities = 0
            player._musichalls = 0
            player._jail_cards = 0
            player._jail_turns = 0

            # CITE : StackOverflow (https://stackoverflow.com/questions/
            # 1400608/how-to-empty-a-list-in-python)
            # DESC : Clears all the elements in a list to make it empty.
            player._ownedprop.clear()
            player._playerbox.update()

        # Initializes the current player icon and sets current player
        # to Player 1 again.
        self._win.remove(self._game._show_cur_plyr)
        self._game._cur_player = self._game._player_list[0]
        self._game._show_cur_plyr = Image(self._win,
                                          self._game._cur_player._file,
                                          30, 38, (1280, 700))
        self._win.add(self._game._show_cur_plyr)


class RollButton(Button):
    """ Rolls the two dice when clicked and moves the player to the
    appropriate location on the board. """

    def __init__(self, game, win, label, width, height, center, color):

        Button.__init__(self, game, win, label, width, height, center, color)

        self._die1 = game._die1
        self._die2 = game._die2

    def handle_mouse_press(self, _):
        """ Rolls die, checks for double, moves the players. """

        self._die1.roll()
        self._die2.roll()
        self._game.double()

        # Needs to exclude the case when the player rolls three doubles,
        # since it should then go to jail directly.
        if self._game._cur_player._double != 3:
            self._game._cur_player.move()


class EndTurn(Button):
    """ Ends the turn of the current player
    and switches to the next player when clicked. """

    def __init__(self, game, win, label, width, height, center, color):

        Button.__init__(self, game, win, label, width, height, center, color)

    def handle_mouse_press(self, _):
        """ Switches the player to the next. """

        # Checks whether player is bankrupt, and if so, removes the player
        # from the game.
        self._game._cur_player.check_bankruptcy()
        self._game._cur_player._double = 0

        """" Switches the player and declares which player rolls. """
        self._game.switch()
        self._game._status = "Player %s rolls." % (self._game._cur_player._id)
        self._game.update_status()


class Instructions(Button):
    """ Makes a button that shows the instructions when clicked. """

    def __init__(self, game, win, label, width, height, center, color):

        Button.__init__(self, game, win, label, width, height, center, color)

        self._win = win

    def handle_mouse_press(self, _):

        # Opens the InstructionCard.
        InstructionCard(self._win)


class InstructionCard(EventHandler):
    """ Makes the instructions screen and closes the window. """

    def __init__(self, win):
        self._win = win

        # Instructions for Orchestropoly.
        self._instr = Image(self._win, "./img/ins.jpg", 700, 800, (800, 390))
        self._win.add(self._instr)
        self._xbutton = Image(self._win, "./img/x.jpg", 40, 40, (1100, 100))
        self._win.add(self._xbutton)
        self._xbutton.add_handler(self)

    def handle_mouse_press(self, _):
        """ Gets rid of the instruction card when x button is pressed. """

        self._win.remove(self._instr)
        self._win.remove(self._xbutton)


# CITE : Professor Perkins
# DESC : Code for reading the data in a json file.
def read_data():
    """ Reads and returns the data stored in the json file. """

    with open("tile.txt", "r") as json_file:
        data = json.load(json_file)
        return data


def program(win):
    """ Runs the program. """

    # Adjusts the size of the window.
    win.set_width(1600)
    win.set_height(800)

    # Runs the game.
    Game(win)


def main():
    # Starts the graphics system.
    StartGraphicsSystem(program)


if __name__ == "__main__":
    main()
