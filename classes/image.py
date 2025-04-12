from PyQt6.QtGui import QPixmap, QImage

class Image:
    def __init__(self, url):
        self.url = url
        self.pixmap = QPixmap(url)
        self.name, self.format = self._get_file_str(url)
        self.image = QImage(url)
        

        #print(self.url, self.name, self.format)


    def _get_file_str(self, url):
        splited_url = url.split("/") if "/" in url else url.split("\\")
        file_name = splited_url[-1].split(".")[0]
        file_format = splited_url[-1].split(".")[1]
        return file_name, file_format