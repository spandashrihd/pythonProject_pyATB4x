def add_before_ui_after_ui(func):
    def wrapper():
        print("before running UI test")
        print("start the browser")
        func()
        print("ending the running UI test")
        print("quit the browser")

    return wrapper()

@add_before_ui_after_ui
def test_ui():
    print("I will test the UI")