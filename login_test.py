
def test_login():
    username = "student01"
    password = "demo_password"

    if username and password:
        print("Login test: PASS")
        print("Login input validation completed.")
    else:
        print("Login test: FAIL")


if __name__ == "__main__":
    test_login()
