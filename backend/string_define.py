web_linked = "https://www.sgx.com/research-education/derivatives"
box_linked = '//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div'
box_element_linked = '//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/sgx-input-select[1]'

type_of_data = ["Tick",\
    "Tick Data Structure",\
    "Trade Cancellation Data",\
    "Trade Cancellation Data Structure"]

button = '//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/button'
box_date_linked = '//*[@id="page-container"]/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/sgx-input-select[2]/sgx-select-model'

time_schedule = 60*60*24
time_schedule_unit = []

file_handler = 'test/test.log'

## example :driver.findElement(By.xpath('//a[contains(text(),'HOD') ][1]')).click(); 