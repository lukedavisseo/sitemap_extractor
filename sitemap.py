import pandas as pd
import streamlit as st

sitemap_urls = st.text_area('Enter individual sitemap URLs, 1 per line')

submit = st.button('Submit')

if submit:

	sitemap_url_list = [line for line in sitemap_urls.split("\n")]

	sitemap_df = pd.DataFrame()

	for url in sitemap_url_list:

		df = pd.read_xml(url)

		sitemap_df = sitemap_df.append(df, ignore_index=True)

	sitemap_csv = sitemap_df.to_csv()

	st.download_button(label='Download CSV', data=sitemap_csv, file_name='sitemaps.csv', mime='text/csv')