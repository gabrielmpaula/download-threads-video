import streamlit as st
import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Threads Video Downloader',
    page_icon=':movie_camera:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# :movie_camera: Threads Video Downloader

Insira o link do Threads que você deseja extrair o vídeo.
'''

opts = ChromeOptions()
opts.add_argument("--headless")
driver = webdriver.Chrome(options=opts)
url = st.text_input(placeholder='URL do Threads')
try:
    driver.get(url)
    video = driver.find_element(By.CSS_SELECTOR, 'video')
    video_url = video.get_attribute('src')
    st.write(video_url)
except:
    st.write('Insira o link que deseja extrair o video.')