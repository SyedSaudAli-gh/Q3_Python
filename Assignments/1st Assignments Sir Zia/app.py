import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up our app
st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("💾 Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualizations.")

upload_files = st.file_uploader("Upload your file (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if upload_files:
    for file in upload_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read the uploaded file
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        # Display file info
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.getbuffer().nbytes / 1024:.2f} KB")

        # Show first 5 rows
        st.write("Preview of the DataFrame:")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader(f"✨ Data Cleaning Options for {file.name}")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed!")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values have been filled!")

        # Column Selection
        st.subheader(f"🔁 Select Columns to Convert for {file.name}")
        columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=list(df.columns))
        if columns:
            df = df[columns]

        # Data Visualizations
        st.subheader(f"📊 Data Visualizations for {file.name}")
        if st.checkbox(f"Show Visualizations for {file.name}"):
            numeric_df = df.select_dtypes(include="number")
            if not numeric_df.empty:
                st.bar_chart(numeric_df.iloc[:, :2])
            else:
                st.warning("No numeric columns available for visualization.")

        # File Conversion Options
        st.subheader(f"🎯 Conversion Options for {file.name}")
        conversion_type = st.radio(f"Convert {file.name} to:", ['CSV', 'Excel'], key=file.name)

        buffer = BytesIO()
        file_name = file.name  # Default name

        if st.button(f"Convert {file.name}"):
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = 'text/csv'

            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False, engine="openpyxl")
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            # Download Button
            st.download_button(
                label=f"⬇️ Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

st.success("All files processed!")
