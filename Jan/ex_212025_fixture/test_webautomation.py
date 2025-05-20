from Jan.ex_212025_fixture.conftest import launch_browser, close_browser


def test_selenium (launch_browser,close_browser):
    launch_browser
    print("Do Tc")
    close_browser