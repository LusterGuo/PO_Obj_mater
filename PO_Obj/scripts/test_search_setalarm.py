from Base.init_driver import Init_driver
from Page.search_obj import Search_Obj

import pytest

class Test_Search_Setalarm:

    @pytest.fixture()
    def begin(self):
        self.driver=Init_driver()


    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("text",[1,2])
    def test_search_page(self,text,begin):
        self.se = Search_Obj(self.driver).re_search_function()
        self.se.click_search()
        self.se.input_search(text)
        self.se.click_search_rebutton()

    def test_change_zimu_setting(self,begin):
        self.zm = Search_Obj(self.driver).re_search_setting()
        self.zm.click_setting_wuzhangai()
        self.zm.swipe_list()
        a=self.zm.get_set_text()
        print(a)
        self.zm.click_zimu()
        self.zm.click_setting_btn()
        self.zm.click_rebutton()
        assert a=='关闭'





