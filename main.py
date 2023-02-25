from selenium import webdriver

def help():
    help_text = open('./help.txt', 'r')
    print(help_text.read())
    help_text.close()

def main():
    user_input = input("Insert what websites you would like to open, or type 'help'\n")
    
    if user_input == "help":
        help()
    else:
        driver = webdriver.Chrome()
        for i in range(len(user_input)):
            driver.execute_script(f"window.open('{youtube_login}')")
            driver.switch_to.window(driver.window_handles[i])

if __name__ == "__main__":
    main()