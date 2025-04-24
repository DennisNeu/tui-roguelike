"""Game class, holds game loop and controls game logic"""
from player import Player
from window import Window
from object import Object
from time import sleep

objects = [
    Object(1, 1, "O"),
    Object(2, 2, "X"),
    Object(3, 3, "Y"),
    Object(4, 4, "Z"),
    Object(5, 5, "A"),
    Object(6, 6, "B"),
    Object(7, 7, "C"),
    Object(8, 8, "D"),
]  # List to hold all objects in the game


class Game:
    def __init__(self, stdscr):
        self.player = Player(5, 5, 100)
        self.window = Window(stdscr)
        self.running = True
        self.score = 0

    def run(self):
        """Main game loop"""
        while self.running:
            keypress = self.window.get_input()
            self.handle_input(keypress)
            self.window.screen_clear()
            self.window.draw_list(objects)
            self.window.draw_player(self.player.pos_x, self.player.pos_y)
            self.check_collision()
            self.window.stdscr.addstr(0, 0, f"Score: {self.score}")
            self.window.screen_refresh()

            sleep(0.05)  # Add a small delay to control the frame rate

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

    # Check for collision with objects
    def check_collision(self):
        for object in objects:
            if (
                self.player.pos_x == object.pos_x
                and self.player.pos_y == object.pos_y
            ):
                self.score += 1
                objects.remove(object)
                break
