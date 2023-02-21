import requests
from progress.bar import Bar

while True:
    url_video = input("Ведите URL видео:")
    bar = Bar("Loading")
    
    def download_video(url=""):
        try:
            get = requests.get(url=url, stream=True)
            with Bar('Processing', fill="%", max=1) as bar:
                for i in range(1):
                    with open("video.mp4", "wb") as file:
                        for chunk in get.iter_content(chunk_size=1024 * 1024):
                            if chunk:
                                file.write(chunk)
                    bar.next()
            
            return "Все прошло как по маслу ✅"
    
        except Exception as _ex:
            return "Что-то пошло не так ⛔"
    
    
    def main():
        print(download_video(url=url_video))
    
    
    if __name__ == "__main__":
        main()
    