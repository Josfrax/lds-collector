
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


class Browser:
    """ This class initilize a browser. 

        Methods:
            - open(): Open browser.
            - close(): Close browser.
    """

    def __init__(self) -> object:
        """ Setup browser. """
        self.driver = None
        # Browser options.
        self.options = Options()  # Options()
        # self.options.add_argument('--headless')
        self.options.page_load_strategy = 'normal'
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-software-rasterizer')

        # Browser references
        self.options.add_experimental_option("prefs", {
            # download path.
            #"download.default_directory": f"{BASE_DIR}/downloads",
            # don't ask for download.
            "download.prompt_for_download": False,
            # allow to update download path.
            "download.directory_upgrade": True,
            # disable safebrowsing.
            "safebrowsing_for_trusted_sources_enabled": False,
            # disable safebrowsing.
            "safebrowsing.enabled": True,
            # disable auto download.
            #'profile.default_content_setting_values.automatic_downloads': 2,
            'excludeSwitches': ['enable-logging']
        })

    def open(self) -> object:
        """ Start browser. 

            Arguments: None.

            Return:
                object -- Webdriver.
        """
        self.driver = webdriver.Chrome(options=self.options)
        return self.driver

    def close(self) -> None:
        self.driver.close()


""" if __name__ == "__main__":
    b = Browser()
    b.open()
 """