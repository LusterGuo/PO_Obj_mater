from appium import webdriver

def Init_driver():
    desired_caps = dict(
        platformName='Android',
        deviceName='192.168.56.101:5555',
        automationName='uiautomator2',
        appPackage='com.android.settings',
        appActivity='.Settings',
        unicodeKeyboard=True,
        resetKeyboard=True
    )
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities=desired_caps)
    driver.implicitly_wait(5)
    return driver
