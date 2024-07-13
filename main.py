import os
from colorama import Fore, Style, init

init(autoreset=True)

print("")
print(Fore.RED + "   ╔═╗╦ ╦╔═╗═╗ ╦╦ ╦   ╔═╗╔═╗╔═╗╦═╗╔═╗╦ ╦" + Style.RESET_ALL)
print(Fore.GREEN + "   ╚═╗║║║║ ║╔╩╦╝╚╦╝   ╚═╗║╣ ╠═╣╠╦╝║  ╠═╣" + Style.RESET_ALL)
print(Fore.BLUE + "   ╚═╝╚╩╝╚═╝╩ ╚═ ╩    ╚═╝╚═╝╩ ╩╩╚═╚═╝╩ ╩" + Style.RESET_ALL)
print("")

def new_func(__name__):
    input_directory = input("   Dosya konumunu girin: ")
    url = input("   Aranacak metin: ")

    def illegalplatform_embrance(input_dir, output_file):
        colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        color_index = 0

        with open(output_file, 'w', encoding='utf-8') as output:
            total_txt_files = sum(1 for file in os.listdir(input_dir) if file.endswith('.txt'))
            processed_files = 0 

            print(Fore.YELLOW + "Tarama başladı..." + Style.RESET_ALL)
            for file in os.listdir(input_dir):
                if file.endswith('.txt'):
                    file_path = os.path.join(input_dir, file)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        for line in f:
                            if url in line:
                                color = colors[color_index % len(colors)]
                                print(color + f"{line.strip()}" + Style.RESET_ALL)  
                                output.write(f"{line.strip()}\n")
                                color_index += 1

                processed_files += 1
                print(Fore.CYAN + f"Taranıyor... ({processed_files}/{total_txt_files})", end='\r', flush=True)

            print(Fore.YELLOW + "\nTarama bitti." + Style.RESET_ALL)

    if __name__ == "__main__":
        output_txt = 'result.txt'  
        illegalplatform_embrance(input_directory, output_txt)

new_func(__name__)