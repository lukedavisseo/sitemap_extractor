import pandas as pd
import advertools as adv
import streamlit as st

st.header('Sitemap URL extractor')

st.subheader('This script extracts URLs from one or more sitemaps and adds them to a CSV file, ready to download.')

sitemap_urls = st.text_area('Enter individual sitemap URLs, 1 per line')

submit = st.button('Submit')

if submit:

	sitemap_url_list = [line for line in sitemap_urls.split("\n")]

	for url in sitemap_url_list:

		sitemap_df = adv.sitemap_to_df(url)

		sitemap_csv = sitemap_df.to_csv()

	st.download_button(label=f'Download {url} CSV', data=sitemap_csv, file_name=f'{url}_sitemap.csv', mime='text/csv')
