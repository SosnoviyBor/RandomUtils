"""
!!! For Windows users !!!
To enable color display in cmd and powershell, see this page and enable VT100 using any of listed options
https://stackoverflow.com/questions/51680709/colored-text-output-in-powershell-console-using-ansi-vt100-codes
"""

from typing import List

class Style:
    RESET='\033[0m'
    BOLD='\033[01m'
    ITALIC='\033[03m'
    UNDERLINE='\033[04m'
    INVISIBLE='\033[08m'
    STRIKETHROUGH='\033[09m'

class Color:
    RESET='\033[0m'
    NEGATIVE='\033[07m'
    
    class Foreground:
        DEFAULT='\033[39m'
        BLACK='\033[30m'
        RED='\033[31m'
        GREEN='\033[32m'
        ORANGE='\033[33m'
        BLUE='\033[34m'
        PURPLE='\033[35m'
        CYAN='\033[36m'
        LIGHTGREY='\033[37m'
        DARKGREY='\033[90m'
        LIGHTRED='\033[91m'
        LIGHTGREEN='\033[92m'
        YELLOW='\033[93m'
        LIGHTBLUE='\033[94m'
        PINK='\033[95m'
        LIGHTCYAN='\033[96m'
    
    class Background:
        DEFAULT='\033[49m'
        BLACK='\033[40m'
        RED='\033[41m'
        GREEN='\033[42m'
        ORANGE='\033[43m'
        BLUE='\033[44m'
        PURPLE='\033[45m'
        CYAN='\033[46m'
        LIGHTGREY='\033[47m'
    
    def saturate(color:str) -> str:
        """
        Returns saturated version of a color\n
        Saturation can be applied only once to a certain color\n
        Saturated colors act the same as regular color + bold style. 
        However, they can be combined with bold style to make it more thick and saturated\n
        If you saturate saturated by default color, it will look like saturated color + bold style. 
        Adding bold style to it won't make any difference
        """
        if color.endswith(";1m"):
            raise("Colors can be saturated only once")
        return color[:-1]+";1m"
    
    def getRGBColor(type:str,r:int,g:int,b:int) -> str:
        """
        !!! Might not work correctly in your terminal !!!\n
        Returns custom rgb color string\n
        type = "fg" -> foreground color\n
        type = "bg" -> background color\n
        0 <= r,g,b <= 255\n
        Otherwise raises an exception
        """
        if (0 < r < 255 or 0 < g < 255 or 0 < b < 255):
            raise("r,g,b can be assigned only to value between 0 and 255")
        match (type):
            case "fg":
                return f"\033[38;2;{r};{g};{b}m"
            case "bg":
                return f"\033[48;2;{r};{g};{b}m"
            case _:
                raise("Color types can only be 'fg' or 'bg'")
    
    def getTableColor(type:str,n:int) -> str:
        """
        !!! Might not work correctly in your terminal !!!\n
        Returns color string from the following table https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit\n
        type = "fg" -> foreground color\n
        type = "bg" -> background color\n
        0 <= n <= 255\n
        Otherwise raises an exception
        """
        if n < 0 or n > 255:
            raise("n can be assigned only to value between 0 and 255")
        match (type):
            case "fg":
                return f"\033[38;5;{n}m"
            case "bg":
                return f"\033[48;5;{n}m"
            case _:
                raise("Color types can only be 'fg' or 'bg'")

def wrap(data, style:str) -> str:
    return style + data + Color.RESET