from typing import *

class Styles:
	reset='\033[0m'
	bold='\033[01m'
	italic='\033[03m'
	underline='\033[04m'
	invisible='\033[08m'
	strikethrough='\033[09m'

class Colors:
	reset='\033[0m'
	negative='\033[07m'
	
	class fg:
		default='\033[39m'
		black='\033[30m'
		red='\033[31m'
		green='\033[32m'
		orange='\033[33m'
		blue='\033[34m'
		purple='\033[35m'
		cyan='\033[36m'
		lightgrey='\033[37m'
		darkgrey='\033[90m'
		lightred='\033[91m'
		lightgreen='\033[92m'
		yellow='\033[93m'
		lightblue='\033[94m'
		pink='\033[95m'
		lightcyan='\033[96m'
	
	class bg:
		default='\033[49m'
		black='\033[40m'
		red='\033[41m'
		green='\033[42m'
		orange='\033[43m'
		blue='\033[44m'
		purple='\033[45m'
		cyan='\033[46m'
		lightgrey='\033[47m'
	
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

def fancyPrint(data, styles:List[str]|str, end:str="\n") -> None:
	"""
	Safely prints anything with provided style table
	"""
	for style in styles:
		print(style, end="")
	print(f'{data}\033[0m', end=end)