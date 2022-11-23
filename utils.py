import Settings


def height_percentage(percentage):
    return (Settings.height/100) * percentage

print(height_percentage(10))

def width_percentage(percentage):
    return (Settings.width/100) * percentage
width_percentage(25)
