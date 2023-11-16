from Base.Base import Base
import Page


class Search_Settings(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_setting_wuzhangai(self):
        self.click_ele(Page.list_btn_wuzhangai)

    def swipe_list(self):
        self.swip_xp(Page.swip_xp_data)

    def click_zimu(self):
        self.click_ele(Page.list_btn_zimu)

    def click_setting_btn(self):
        self.click_ele(Page.btn_use_zimu)

    def click_rebutton(self):
        self.click_ele(Page.s_rebutton)

    def get_set_text(self):
        return self.find_element_define(Page.test_zimu).text



