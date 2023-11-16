from Page.search_page import Search_Page
from Page.search_settings import Search_Settings

class Search_Obj:

    def __init__(self,driver):
        self.driver=driver

    def re_search_function(self):
        #返回搜索对象页面
        return Search_Page(self.driver)

    def re_search_setting(self):
        return Search_Settings(self.driver)