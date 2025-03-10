import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo


TIME_ZONES = [
    "UTC", "Asia/Karachi", "Asia/Tokyo", "Asia/Dubai", "Asia/Kolkata",
    "America/New_York", "America/Los_Angeles", "Australia/Sydney", 
    "Europe/London", "Europe/Berlin", "Africa/Cairo", "Africa/Johannesburg",
    "America/Chicago", "America/Toronto", "Asia/Shanghai", "Asia/Singapore",
    "Europe/Paris", "Europe/Moscow", "Pacific/Auckland", "Pacific/Honolulu"
]

st.title("⏰ Time Zone App")

# Create a multiselect widget for selecting timezone!
selected_time_zone = st.multiselect("Select Time Zones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

# Display the selected timezone
st.subheader("🕒 Selected Time Zone")
for tz in selected_time_zone:
    
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    
    st.write(f'**{tz}**: {current_time}')
    
st.subheader("Convert Time Between Time Zones")

current_time = st.time_input("Current Time", datetime.now().time())

from_time_zone = st.selectbox("From Time Zone", TIME_ZONES, index=0)

to_time_zone = st.selectbox("To Time Zone", TIME_ZONES, index=1)

if st.button("Convert Time Zone"):
    
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_time_zone))
    
    converted_time = dt.astimezone(ZoneInfo(to_time_zone)).strftime("%Y-%m-%d %I:%M:%S %p")
    
    st.info(f"Converted Time in {to_time_zone} : {converted_time} ")

    