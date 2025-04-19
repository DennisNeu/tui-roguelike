"""Game class, holds game loop and controls game logic"""
from player import Player
from window import Window
class Game:
    def __init__(self, stdscr):
        self.player = Player(5, 5, 100)
        self.window = Window(stdscr)
        self.running = True

    def run(self):
        """Main game loop"""
        while self.running:
            keypress = self.window.get_input()
            self.handle_input(keypress)
            self.window.screen_clear()
            self.window.draw_player(self.player.pos_x, self.player.pos_y)
            self.window.screen_refresh()

            sleep(0.05) # Add a small delay to control the frame rate


    def handle_input(self, keypress):
        if keypress == ord("q"):
            self.running = False
        elif keypress == ord("w"):
            if self.player.pos_y > 0:
                self.player.pos_y -= 1
        elif keypress == ord("s"):
            if self.player.pos_y < self.window.max_height - 2:
                self.player.pos_y += 1
        elif keypress == ord("a"):
            if self.player.pos_x > 0:
                self.player.pos_x -= 1
        elif keypress == ord("d"):
            if self.player.pos_x < self.window.max_width - 1:
                self.player.pos_x += 1