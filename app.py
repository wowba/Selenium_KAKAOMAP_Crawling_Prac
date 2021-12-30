from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
actionChains = ActionChains(driver)
driver.get("https://map.kakao.com/")
elem = driver.find_element_by_name("q")
elem.send_keys("동대문구 카페")

# elem.send_keys("동대문구 카페")
# elem.send_keys(Keys.RETURN)
# time.sleep(5)

# name = driver.find_element_by_css_selector("#pane > div > div.Yr7JMd-pane-content.cYB2Ge-oHo7ed > div > div > div.siAUzd-neVct.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc.siAUzd-neVct-Q3DXx-BvBYQ > div.siAUzd-neVct.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc.siAUzd-neVct-Q3DXx-BvBYQ > div:nth-child(3) > div > a")
# realname = name.get_attribute("aria-label")
# print(realname)


# 다음페이지 넘어가기
# next = driver.find_element_by_id("interactive-hovercard")
# actionChains.context_click(next).perform()


# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()