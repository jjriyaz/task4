class TV:
    def __init__(self, brand, inches, price):
        self.brand = brand
        self.channel = 1
        self.volume = 50
        self.inches = inches
        self.price = price
        self.on = False  # TV is initially off

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel} and volume {self.volume}"

# Example usage:
my_tv = TV("samsung", 55, 1500)
print(my_tv.status())
my_tv.increase_volume()
print(my_tv.status())
my_tv.set_channel(10)
print(my_tv.status())
my_tv.reset_tv()
print(my_tv.status())

# PART-B

class LedTV(TV):
    def __init__(self, brand, inches, price, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight):
        super().__init__(brand, inches, price)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def display_details(self):
        return f"{self.brand} LED TV: {self.inches}\" Screen, {self.refresh_rate}Hz Refresh Rate, {self.viewing_angle}° Viewing Angle"

class PlasmaTV(TV):
    def __init__(self, brand, inches, price, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle):
        super().__init__(brand, inches, price)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle

    def display_details(self):
        return f"{self.brand} Plasma TV: {self.inches}\" Screen, {self.refresh_rate}Hz Refresh Rate, {self.viewing_angle}° Viewing Angle"

# Example usage:
led_tv = LedTV("Sony", 65, 2500, "Thin", "Low", "10 years", 120, 178, "RGB")
print(led_tv.display_details())

plasma_tv = PlasmaTV("LG", 60, 1800, "Thick", "Medium", "8 years", 60, 160)
print(plasma_tv.display_details())