import geocoder
import os
import pyfiglet

#######____________________________----------______________________#########
print()
def display_center(text):
    # Get terminal width
    terminal_width = os.get_terminal_size().columns
    
    # Calculate left padding to center the text
    left_padding = (terminal_width - len(text)) // 3
    
    # Display text with padding
    print(" " * left_padding + text)

def main():
    text = "   FiLocate "
    banner = pyfiglet.figlet_format(text)
    display_center(banner)
    display_center("-----------------------------------")
    display_center("---- Made by Eng Hazem Othman ----")
    display_center("-----------------------------------")
    display_center("-----------------------------------")
    display_center("----  github.com/hazemothman246 ----")
    display_center("-----------------------------------")
    print() 
    print()
    print()
if __name__ == "__main__":
    main()
    

#######____________________________----------______________________#########


def get_location_from_ip(ip_address):
    g = geocoder.ip(ip_address)
    if g.ok:
        return f"{g.country}, {g.city}"
    else:
        return "Location not found"
print()
print()
ip_address = input(".     Enter the IP address: ")
location = get_location_from_ip(ip_address)
print()
print(".     Location:", location)
print()


#######____________________________----------______________________#######
  
    
    





