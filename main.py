from selenium import webdriver
from time import sleep
from url import url_dict

driver = webdriver.Chrome()


def help():
    # This function prints out the technical guide for different website options 

    help_text = open('./help.txt', 'r')
    print(help_text.read())
    help_text.close()


def open_tab(url, tab_index):
    driver.execute_script(f"window.open('{url[0]}')")
    driver.switch_to.window(driver.window_handles[tab_index])
    sleep(1000)
    # //*[@id="identifierId"].sendkeys()
    # //*[@id="identifierNext"]/div/button.click

def extract_url(user_input):
    # This function extracts the user inputs and sends the urls to the open website function

    current_tab = 1
    for input in user_input:
        match input.lower():
            case "y":
                curr_urls = [value for key, value in url_dict.items() if 'y' in key][0]
                open_tab(curr_urls, current_tab)
                current_tab+=1
            
            case "p":
                curr_urls = [value for key, value in url_dict.items() if 'p' in key][0]
                open_tab(curr_urls, current_tab)
                current_tab+=1

            
            case "c":
                curr_urls = [value for key, value in url_dict.items() if 'c' in key][0]
                open_tab(curr_urls, current_tab)
                current_tab+=1


            case "h":
                curr_urls = [value for key, value in url_dict.items() if 'h' in key][0]
                open_tab(curr_urls, current_tab)
                current_tab+=1

            case "g":
                curr_urls = [value for key, value in url_dict.items() if 'g' in key][0]
                open_tab(curr_urls, current_tab)
                current_tab+=1


def main():
    user_input = input("Insert what websites you would like to open, or type 'help'\n")
    
    if user_input == "help":
        help()
    else:
        extract_url(user_input)

if __name__ == "__main__":
    main()
