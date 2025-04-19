import curses

class Window:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.max_height, self.max_width = stdscr.getmaxyx()
        # Calls are necessary to ensure screen is clean, refresh is necessary to ensure the screen is updated
        self.stdscr.clear()
        self.stdscr.refresh()
        curses.curs_set(0)
        curses.noecho()
        self.stdscr.nodelay(True) # Make getch() non-blocking

    def draw_player(self, player_x, player_y):
        """Draws the player on the screen at the given coordinates"""
        self.stdscr.addch(player_y, player_x, "@")

    def screen_refresh(self):
        """Refreshes the screen"""
        self.stdscr.refresh()
        
    def screen_clear(self):
        """Clears the screen"""
        self.stdscr.clear()

    def get_screen_size(self):
        """Returns the screen size"""
        return self.max_height, self.max_width

    def get_input(self):
        """Gets input from the user"""
        try:
            return self.stdscr.getch()
        except:
            return -1