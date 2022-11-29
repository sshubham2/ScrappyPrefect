class XpathQ:
    DATE = '//*[@id="site-dashboard"]/div/div/div[1]/div[1]/h5/span/text()[1]'
    ACTIVE_CASE = '//*[@id="site-dashboard"]//strong[2]/text()'
    TOTAL_DISCHARGED = '//*[@id="site-dashboard"]//li[2]/strong[2]/text()'
    TOTAL_DEATHS = '//*[@id="site-dashboard"]//li[3]/strong[2]/text()'
    TOTAL_VACC = '//*[@id="site-dashboard"]//div/span[2]/text()'

DATE_FORMAT = '%d%B%Y%H:%M%z'