import streamlit as st
import os
import time

st.write("hey")

if st.button("Generate ws3d JAR"):
    os.system("cd ws3d && ./gradlew build")

    with open("ws3d/build/libs/ws3d-0.0.1-full.jar", "rb") as fp:
        btn = st.download_button(
            label="Download ws3d JAR",
            data=fp,
            file_name="ws3d.jar",
        )

if st.button("Generate DemoCST JAR"):
    os.system("cd DemoCST && ./gradlew build")

    with open("DemoCST/build/libs/DemoCST-0.0.4-full.jar", "rb") as fp:
        btn = st.download_button(
            label="Download DemoCST JAR",
            data=fp,
            file_name="democst.jar",
        )