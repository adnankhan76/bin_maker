import string
import time
import requests
from colorama import init, Fore, Style
import secrets
from datetime import datetime

init(autoreset=True)

BIN_LENGTH = 5
API_ENDPOINT = 'https://bin-adnankhan76s-projects.vercel.app/api/'

def generate_bin(TYPE):
    characters = string.digits
    return str(TYPE) + ''.join(secrets.choice(characters) for _ in range(BIN_LENGTH))

def print_colored_logo():
    # Larger font for the logo
    logo = f"""
{Fore.RED}         ____________________________ 
{Fore.BLUE}        |┏┓┳┓┳┓┏┓┳┓  ┏┓┓┏┏┳┓  ┳┓┳┳┓ | 
{Fore.MAGENTA}        |┣┫┃┃┃┃┣┫┃┃  ┃┃┃┃ ┃   ┣┫┃┃┃ |
{Fore.CYAN}        |┛┗┻┛┛┗┛┗┛┗  ┣┛┗┛ ┻   ┻┛┻┛┗ |
{Fore.RED}        |_______ADNAN_KHAN__________|
{Fore.YELLOW}      ^ht{Fore.RED}tps:/{Fore.MAGENTA}/github.com/adnankhan76/bin_{Fore.CYAN}maker^                     
{Style.RESET_ALL}
""" 
    print(logo)

def get_bin_info(generated_bin):
    api_url = f"{API_ENDPOINT}{generated_bin}"
    response = requests.get(api_url)
    return response.json() if response.ok else None

def save_bin_info(file, generated_bin, bin_info):
    if bin_info and bin_info.get("result") == True:
        fields_to_save = ["bin", "vendor", "type", "level", "bank", "country"]
        save_data = "\n".join([f"{field}: {bin_info['data'].get(field)}" for field in fields_to_save])

        file.write(save_data + '\n')
        time.sleep(0.10)
        print(f'{Fore.GREEN}{save_data}{Style.RESET_ALL}')
        print(f'{Fore.BLUE}{generated_bin}{Style.RESET_ALL}')

def main():
    print_colored_logo()

    TYPE = input("Please enter type 1= Visa  2= master ? 1/2: ")
    TYPE = 4 if TYPE == "1" else 5

    NUM_BINS = int(input("Please enter quantity: "))

    # Create a filename with the current date and time
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    FILE_PATH = f'bin_{current_datetime}.txt'

    with open(FILE_PATH, 'w') as file:
        for _ in range(NUM_BINS):
            generated_bin = generate_bin(TYPE)
            bin_info = get_bin_info(generated_bin)
            save_bin_info(file, generated_bin, bin_info)

    print(f'Bins info saved to {FILE_PATH} data')

if __name__ == "__main__":
    main()
