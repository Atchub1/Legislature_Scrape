from splinter import Browser
from bs4 import BeautifulSoup
import requests
import re

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# IL Genearl Assembly homepage
url = 'http://www.ilga.gov'


# retrieve the webpage, create BeautifulSoup object to parse the data
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())



# Locate link to all Senators and go to the page 
links = soup.find_all(href=re.compile("/senate/"), text='Members')

for link in links:
    reference = link.get('href')
#     browser.click_link_by_partial_text('Members')
    senate_url = url+reference
print(senate_url)
browser.visit(senate_url)
html = browser.html
senate_soup = BeautifulSoup(html, 'html.parser')
# print(senate_soup.prettify())


senator_links = senate_soup.find_all('a', {'class':'notranslate'})
# senate_soup.find_all('a')



# create empty list to hold all member urls
senator_link_list = []

# loop though senate page and add each member link to the senator_link_list
for link in senator_links:
    reference = link.get('href')
#     browser.click_link_by_partial_text('Members')
    senator_url = url+reference
    senator_link_list.append(senator_url)
    
# print(senator_link_list[0])







# Create a function that will go to each senator's page and scrape thier information


def senator_scrape(link):

    # visit the first senator page
    browser.visit(link)
    html = browser.html
    senator_soup = BeautifulSoup(html, 'html.parser')


    # Obtain the senator's and district number
    senator_name = senator_soup.find('span', {'class':'notranslate'}).text
    senator_district = senator_soup.find('span', {'class':'heading2 notranslate'}).text


    # Obtain the parital image link from the senator's webpage
    senator_img_partial = senator_soup.find('table', {'class' : 'notranslate'}).img['src']


    # obtain the full image link by combining the orignal il.gov url with the partial senator image link
    senator_img = url + senator_img_partial


    # Get the leadership position
    senator_position_all = senator_soup.find_all('span', {'class':'heading2'})
    senator_position = senator_position[3].text


    # Most of the sentor info are in tables, so can gather the address and committee assignments from td in the "member" class
    senator_info_list = senator_soup.find_all('td', {'class': 'member'})


    # In[71]:


    # Springfield office information

    senator_springfield_address_line1 = senator_info_list[1].text
    # senator_springfield_address_line1
    senator_springfield_address_line2 = senator_info_list[2].text
    senator_springfield_address_line3 = senator_info_list[3].text

    senator_springfield_phone_number = senator_info_list[4].text


    # In[73]:


    #  District office information

    senator_district_address_line1 = senator_info_list[8].text

    senator_district_address_line2 = senator_info_list[9].text
    senator_district_address_line3 = senator_info_list[10].text

    senator_district_phone_number = senator_info_list[11].text

    # senator_district_address_line1


    # In[77]:


    # Senator info: The # of years served, committee assignments, and biographhy are all under the same child tag

    senator_bio_info  = senator_info_list[12].text
    senator_bio_info


    # In[87]:


    ass_reps_tag = senator_soup.find_all('a', {'class': 'notranslate'})
    ass_reps_tag


    # In[92]:


    current_senator_assoc_reps = []
    for tag in ass_reps_tag:
        rep = tag.text
        current_senator_assoc_reps.append(rep)
    #     print(rep)
    # current_senator_assoc_reps





