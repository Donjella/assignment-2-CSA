from colored import Style, Fore, Back

# Declaring variables for color palette
color1: str = f'{Style.underline}{Style.BOLD}{Fore.dark_green}{Back.spring_green_4}' # Color for welcome header and exit app
color2: str = f"{Style.BOLD}{Fore.white}{Back.dark_blue}"                   # Color for sub menu
color3: str = f"{Fore.yellow}{Back.black}"                                  # Color for sub menu headers and confirmations
color4: str = f"{Style.BOLD}{Fore.magenta}"                                 # color for other headers
color5: str = f"{Fore.red}{Back.black}"                                     # Color for errors/exceptions raised
