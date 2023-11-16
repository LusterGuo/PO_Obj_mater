from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver=driver


    def find_element_define(self,loc):
        """
        :param loc:元组 ，by和对应的value
        :param timeout:查找时间
        :param t: 多长时间查找一次
        :return: element
        """
        return WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*loc))

    def click_ele(self,loc):
        """
        :param loc:元组，by和对应的value
        :return:None
        """
        self.find_element_define(loc).click()

    def input_text(self,loc,text):
        """
        :param loc: 元组，by和对应的value
        :param text: 要输入的文本
        :return: None
        """
        input=self.find_element_define(loc)
        input.clear()
        input.send_keys(text)

    def swip_xp(self,node):
        self.driver.swipe(*node)
