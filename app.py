import streamlit as st
import pandas as pd
from io import BytesIO
import zipfile
import openpyxl
from openpyxl import load_workbook
import hashlib
import os

st.title('Excel Wizard')

# ... (rest of your code)

# ... (split_excel and merge_excels functions)

# File upload options
st.sidebar.title("Excel Wizard Options")
option = st.sidebar.radio("Choose an action", ('Split Excel by Sheets', 'Merge Excel Files'))

# Split Excel File
if option == 'Split Excel by Sheets':
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])
    if uploaded_file is not None:
        # ... (processing logic)

        # Create a file dialog to select the download directory
        download_dir = st.file_dialog("Select Download Directory", type=["folder"])

        if download_dir:
            # Download the file to the selected directory
            with open(os.path.join(download_dir, "split_sheets.zip"), "wb") as f:
                f.write(split_result)
            st.success("Files downloaded to the selected directory.")
        else:
            st.warning("Please select a download directory.")

# Merge Excel Files
elif option == 'Merge Excel Files':
    # ... (processing logic)

    # Create a file dialog to select the download directory
    download_dir = st.file_dialog("Select Download Directory", type=["folder"])

    if download_dir:
        # Download the file to the selected directory
        with open(os.path.join(download_dir, "merged_file.xlsx"), "wb") as f:
            f.write(merged_result)
        st.success("File downloaded to the selected directory.")
    else:
        st.warning("Please select a download directory.")
