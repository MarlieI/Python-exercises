#! python3
# Practice Project "Command Line Emailer" from C11 of Automate The Boring Stuff
import sys
import time
from selenium import webdriver

if len(sys.argv) > 2:
    passwordElem = sys.argv[1]
    messageElem = ' '.join(sys.argv[2:])
else:
    print('Please give your password and message as command line arguments.')
    input('For example: "commandLineEmailer.py password message"')
    sys.exit()

browser = webdriver.Firefox()
browser.get('https://account.live.com/')
time.sleep(1)

signIn = browser.find_element_by_id('mectrl_headerPicture')
signIn.click()
time.sleep(1)

userInput = browser.find_element_by_id('i0116')
userInput.send_keys('OUTLOOK EMAIL TO LOG INTO')
nextButton = browser.find_element_by_id('idSIButton9')
nextButton.click()
time.sleep(1)

passwordInput = browser.find_element_by_id('i0118')
passwordInput.send_keys(passwordElem)
nextButton = browser.find_element_by_id('idSIButton9')
nextButton.click()
time.sleep(5)

goMail = browser.find_element_by_id('O365_MainLink_NavMenu')
goMail.click()
time.sleep(1)
clickMail = browser.find_element_by_id('O365_AppTile_Mail')
clickMail.click()
time.sleep(5)

newMessage = browser.find_element_by_id('id__7')
newMessage.click()
time.sleep(5)

receiver = browser.find_element_by_class_name('ms-BasePicker-input')
receiver.send_keys('EMAIL TO SEND MESSAGE TO')
time.sleep(3)

# dynamic id, last digit after "9" changes so makes sure it starts with same pattern
subject = browser.find_element_by_css_selector("*[id^='TextField9']")
subject.send_keys('Beep Beep')
time.sleep(3)

message = browser.find_element_by_class_name('_4utP_vaqQ3UQZH0GEBVQe')
message.send_keys(messageElem)
send = browser.find_element_by_class_name('ms-Button--primary')
send.click()
