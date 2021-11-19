import time
from device_data import get_device
from luma.core.render import canvas


def primitives(device, draw):
    top = 6
    size = draw.textsize('World!')
    draw.text((device.width - 80, top), 'Deepak', fill="cyan")
    draw.rectangle(device.bounding_box, outline="white")


def main():
    device = get_device()
    print("Testing basic canvas graphics...")
    for _ in range(2):
        with canvas(device) as draw:
            primitives(device, draw)
    time.sleep(5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
