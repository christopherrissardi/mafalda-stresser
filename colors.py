from pystyle import *
from getpass import getpass as hinput

blue = Col.blue
red = Col.red
white = Col.white
blue = Col.StaticMIX((Col.blue, Col.black))
bpurple = Col.StaticMIX((Col.purple, Col.black, blue))
purple = Col.StaticMIX((Col.purple, blue, Col.white))


def stage(text, symbol="..."):
    col1 = purple
    col2 = white
    return f" {Col.Symbol(symbol, col2, col1, '{', '}')} {col2}{text}"


def error(text, start="\n"):
    hinput(f"{start} {Col.Symbol('!', blue, white)} {blue}{text}")
    exit()
