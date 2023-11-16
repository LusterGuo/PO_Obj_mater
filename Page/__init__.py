from selenium.webdriver.common.by import By

"""
searchpage
"""
# settings功能的输入框按钮
s_action_bar = (By.ID, "com.android.settings:id/search_action_bar")
# settings功能的输入框
s_src_text = (By.ID, "android:id/search_src_text")
# settings查询框的返回按钮
s_rebutton = (By.CLASS_NAME, "android.widget.ImageButton")


"""
settings的滑动点击事件
"""
#点击无障碍功能
list_btn_wuzhangai=(By.XPATH,"//*[contains(@text,'无障碍')]")
#滑动的距离
swip_xp_data=(200,1200,200,200)
#获取字幕的文案
test_zimu=(By.XPATH,"//*[contains(@text,'字幕')]/following-sibling::*")
#点击列表字幕
list_btn_zimu=(By.XPATH,"//*[contains(@text,'字幕')]")
#点击使用字幕开关
btn_use_zimu=(By.ID,"com.android.settings:id/switch_widget")
#点击返回按钮
s_rebutton = (By.CLASS_NAME, "android.widget.ImageButton")


