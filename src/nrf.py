from selenium.webdriver.common.by import By

from utils.browser import Browser


class NombreRutFirma(Browser):
    def __init__(self) -> None:
        super().__init__()
        self.driver = None
        self.base_url: str = "https://www.nombrerutyfirma.com"

    def __seach_name(self, name:str) -> None:
        # Seach name
        self.driver.find_element(
            By.XPATH, '//*[@id="valid"]/div/input'
        ).send_keys(name)

        self.driver.find_element(
            By.XPATH, '//*[@id="valid"]/div/span/button'
        ).click()

    def __get_names(self) -> list:
        names:list = list()
        rows = self.driver.find_elements(
            By.XPATH, '/html/body/div[2]/div/table/tbody/tr'
        )
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, 'td')
            data_row:list = [column.text for column in columns]
            row_dict:list = dict(
                name=data_row[0],
                rut=data_row[1],
                sex=data_row[2],
                address=dict(
                    street=data_row[3],
                    commune=data_row[4],
                    full=f"{data_row[3]}, {data_row[4]}"
                )
            )
            names.append(row_dict)
            print(row_dict)
        return names

    def seach_by_name(self, name:str) -> None:
        # Go to main page.
        self.driver = super().open()
        url:str = self.base_url
        self.driver.get(url)
        # Search by name
        self.__seach_name(name)
        self.__get_names()
        # Run End
        super().close()
        




if __name__ == "__main__":
    nrf = NombreRutFirma()
    nrf.seach_by_name('abajo')

