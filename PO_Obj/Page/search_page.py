from Base.Base import Base
import Page

class Search_Page(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_search(self):
        self.click_ele(Page.s_action_bar)

    def input_search(self,text):
        self.input_text(Page.s_src_text,text)

    def click_search_rebutton(self):
        self.click_ele(Page.s_rebutton)
