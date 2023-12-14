from datetime import datetime

from utilities.animator import Animator
from setup import colours, fonts, frames

from rgbmatrix import graphics

# Setup
DAY_COLOUR = colours.PINK_DARK
DAY_FONT = fonts.small
DAY_POSITION = (2, 23)

def DayOfWeek(isoDay):
    if isoDay == 1:
        return "Maandag"
    elif isoDay == 2:
        return "Dinsdag"
    elif isoDay == 3:
        return "Woensdag"
    elif isoDay == 4:
        return "Donderdag"
    elif isoDay == 5:
        return "Vrijdag"
    elif isoDay == 6:
        return "Zaterdag"
    elif isoDay == 7:
        return "Zondag"
    else:
        return "<Ongeldig>"

class DayScene(object):
    def __init__(self):
        super().__init__()
        self._last_day = None

    @Animator.KeyFrame.add(frames.PER_SECOND * 1)
    def day(self, count):
        if len(self._data):
            # Ensure redraw when there's new data
            self._last_day = None

        else:
            # If there's no data to display
            # then draw the day
            now = datetime.now()
            current_day = DayOfWeek(now.isoweekday())
            

            # Only draw if time needs updated
            if self._last_day != current_day:
                # Undraw last day if different from current
                if not self._last_day is None:
                    _ = graphics.DrawText(
                        self.canvas,
                        DAY_FONT,
                        DAY_POSITION[0],
                        DAY_POSITION[1],
                        colours.BLACK,
                        self._last_day,
                    )
                self._last_day = current_day

                # Draw day
                _ = graphics.DrawText(
                    self.canvas,
                    DAY_FONT,
                    DAY_POSITION[0],
                    DAY_POSITION[1],
                    DAY_COLOUR,
                    current_day,
                )
