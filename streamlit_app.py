import streamlit as st
import os
import requests
from io import BytesIO
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
st.markdown('''
# :movie_camera: Threads Video Downloader
### Criado por [@Gabeira](https://beacons.ai/gabeira)

Insira o link do Threads que você deseja extrair o vídeo.'''
)

opts = ChromeOptions()
opts.add_argument("--headless")
driver = webdriver.Chrome(options=opts)
url = st.text_input('URL', label_visibility='hidden', placeholder='URL do Threads')
try:
    driver.get(url)
    video = driver.find_element(By.CSS_SELECTOR, 'video')
    video_url = video.get_attribute('src')
    st.markdown('''
    ## Download pronto!
    Clique no link abaixo para fazer download do video.
    ''')
    video_data = requests.get(video_url)
    buffer = BytesIO()
    buffer.write(video_data.content)
    st.download_button('Download', buffer, mime='video/mp4')
except:
    st.write('URL vazia ou indisponível.')