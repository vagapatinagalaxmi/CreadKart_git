pytest -v -s -n=4 --html=HtmlReports/chrome_report.html --browser Chrome --alluredir="AllureReports"
pytest -v -s -n=4 --html=HtmlReports/firefox_report.html --browser Firefox --alluredir="AllureReports"
pytest -v -s -n=4 --html=HtmlReports/Edge_report.html --browser Edge --alluredir="AllureReports"
