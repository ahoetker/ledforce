from subprocess import call, check_output
from time import sleep
from os import devnull
import re

DEVNULL = open(devnull, "w")


def set_brightness(brightness: int) -> None:
    call(
        ["nvidia-settings", "--assign", "GPULogoBrightness={}".format(brightness)],
        stderr=DEVNULL,
        stdout=DEVNULL,
    )


def get_brightness() -> int:
    query = check_output(
        ["nvidia-settings", "-q", "GPULogoBrightness"],
        stderr=DEVNULL,
        universal_newlines=True,
    )
    prog = re.compile("\d+\.")
    brightness = re.findall(prog, query)[0].replace(".", "")
    return int(brightness)


def toggle() -> None:
    brightness = get_brightness()
    if brightness == 100:
        set_brightness(0)
    else:
        set_brightness(100)


def breathe(step: int, sleeptime: float) -> None:
    for i in range(0, 100 + step, step):
        set_brightness(i)
        print(i)
        sleep(sleeptime)

    for i in range(100, 0 - step, -1 * step):
        set_brightness(i)
        print(i)
        sleep(sleeptime)


if __name__ == "__main__":
    breathe(3, 0.01)
