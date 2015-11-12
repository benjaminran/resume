#!venv/bin/python3
import sys
import re
import configparser
from selenium import webdriver

import pdb


def login_to_linkedin():
    """Log in to LinkedIn"""
    username = credentials[0]
    password = credentials[1]
    driver.get("https://www.linkedin.com")
    email_field = driver.find_element_by_id("login-email")
    email_field.send_keys(username)
    password_field = driver.find_element_by_id("login-password")
    password_field.send_keys(password)
    submit = driver.find_element_by_name("submit")
    submit.click()

def update_linkedin_summary(newlink):
    """Insert newlink in the place of the old resume link in LinkedIn summary"""
    login_to_linkedin()
    pdb.set_trace()
    edit_profile = driver.find_elements_by_link_text("Profile")[0]
    edit_profile.click()
    edit_summary = driver.find_element_by_css_selector("p.body-field:nth-child(1) > button:nth-child(1)")
    edit_summary.click()
    summary = driver.find_element_by_id("expertise_comments-editExpertiseForm")
    summary.click()
    summary.clear()
    new_summary = re.sub('Resume: .+', '\n\nResume: '+newlink, summary.text)
    summary.send_keys(new_summary)
    submit = driver.find_element_by_name("submit")
    submit.click()
    contact_info = driver.find_element_by_partial_link_text("Contact Info")
    contact_info.click()
    resume_site = driver.find_element_by_css_selector("div.field > ul.field-text > li")
    resume_site.click()
    resume_site_link = driver.find_element_by_id("url_addr-memberURLParam0-editContactInfoForm")
    resume_site_link.clear()
    resume_site_link.send_keys(newlink)
    contact_info_submit = driver.find_element_by_name("submit")
    contact_info_submit.click()
    driver.close()

def parse_credentials(ini_file):
    """Extract and return login credentials from config file"""
    config = configparser.ConfigParser()
    config.read(ini_file)
    username = config['LinkedIn']['username']
    password = config['LinkedIn']['password']
    credentials = (username, password)
    return credentials


if __name__ == "__main__" :
    """Main Routine"""
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    credentials = parse_credentials('credentials.ini')
    update_linkedin_summary(sys.argv[1])
