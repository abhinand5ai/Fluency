
def angleClock(self, hour: int, minutes: int) -> float:
    minDeg = minutes / 60 * 360
    hourDeg = (hour / 12 * 360 + (minDeg/360) * 30) % 360

    angle = abs(hourDeg - minDeg)
    return min(angle, 180 - angle)