import pytest
from selenium import webdriver
from google.cloud.bigquery import dbapi
import pandas_gbq
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="auth_key.json"

"""
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options
)


chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')"""


query = """
	SELECT distinct(tag_code) as tag,* FROM `ssr-project-262905.ssr_dw_esb.user_tag_info_view`  as a
	full join `ssr-project-262905.ssr_dw_esbp.user_tag_info_view`  as b
	using(tag_code)
	where a.tag_name in ('VIP客','深耕客','eline聲量','好客','再存客','即將流失客','潛在VIP客','小額健康客','退場VIP','退場深耕客',
	'套利客','壞壞客','AG視訊疑似對打客','AG視訊對打客','BB視訊疑似對打客','BB視訊對打客','XBB視訊疑似對打客','XBB視訊對打客')
	 order by tag;
"""
result = pandas_gbq.read_gbq(query)
print(result)
"""
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.google.com/')

print("Docker magic!!")
"""