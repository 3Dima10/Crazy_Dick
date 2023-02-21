import wget
from pyfiglet import Figlet
import colorama


def download_wget(url='', file_type='img'):
    try:
        wget.download(url=url, out=f'photos{file_type}.jpg')
    except Exception as ex:
        return "Попробуй снова"


def main():
    pr = Figlet(font="smisome1")
    print("\n"
          "--------------------------------------------------------------------------------\n"
          "\n")
    print(colorama.Fore.GREEN + pr.renderText("crazy photos"))

    a = input(colorama.Fore.BLUE + "Ведите URL фотографий:")
    download_wget(url=a, file_type="img")
    pass


while True:
    if __name__ == "__main__":
        main()
