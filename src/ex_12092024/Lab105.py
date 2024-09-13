from browser_package.Open_Browser import start_browser
from browser_package.Close_Browser import stop_browser


def testcase():
    start_browser()
    print("running the test case")
    stop_browser()

testcase()