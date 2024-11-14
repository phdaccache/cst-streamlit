import streamlit as st
import os
import time

st.write("hey")

if st.button("generate"):
    os.system("cd ws3d && ./gradlew build && ls")
if st.button("check 1"):
    os.system("ls")
if st.button("check 2"):
    os.system("cd ws3d && ls")
# os.system("DemoCST/gradlew build")
# os.system("DemoCST/gradlew run")

# with open("ws3d/build/libs/ws3d-0.0.1-full.jar", "rb") as fp:
#     btn = st.download_button(
#         label="Download ws3d JAR",
#         data=fp,
#         file_name="ws3d-0.0.1-full.jar",
#     )


# with open("DemoCST/build/libs/DemoCST-0.0.4-full.jar", "rb") as fp:
#     btn = st.download_button(
#         label="Download DemoCST JAR",
#         data=fp,
#         file_name="DemoCST-0.0.4-full.jar",
#     )