import time

import pytest
from Page.search_obj import Search_Obj
from Base.init_driver import Init_driver
from Base.data_excel import Excel_Data

def data_excel_deal():
    list_data=[]
    yaml_data=Excel_Data("data").excel_data()
    for i in yaml_data.get("Search_Data").keys():
        list_data.append((i,yaml_data.get("Search_Data").get(i).get("input_text")))
    return list_data


class Test_Yaml:
    def setup_class(self):
        self.driver=Init_driver()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize('test_id,input_text',data_excel_deal())
    def test_search(self,test_id,input_text):
        sp=Search_Obj(self.driver).re_search_function()
        sp.click_search()
        print("输入的数据 :", test_id,input_text)
        sp.input_search(input_text)
        time.sleep(2)
        self.driver.get_screenshot_as_file("D:\Datas\PyDatas\PO_Obj\Screen\%s.png"%test_id)
        sp.click_search_rebutton()




