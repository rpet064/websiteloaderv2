from selenium import webdriver

driver = webdriver.Chrome()

def help():
    help_text = open('./help.txt', 'r')
    print(help_text.read())
    help_text.close()

def main():
    user_input = input("Insert what websites you would like to open, or type 'help'\n")
    
    if user_input == "help":
        help()
    else:
        for i in range(len(user_input)):
            driver.execute_script("google.com")
            driver.switch_to.window(driver.window_handles[i])

if __name__ == "__main__":
    main()