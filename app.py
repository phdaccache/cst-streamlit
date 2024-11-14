import streamlit as st
import os
import shutil

st.write("hey")

if st.button("Build ws3d JAR"):
    with st.spinner("Building..."):
        os.system("cd ws3d && ./gradlew build")

    os.system("echo 'BEFORE'")
    os.system("cd ws3d && ls -a")

    with open("ws3d/build/libs/ws3d-0.0.1-full.jar", "rb") as fp:
        btn = st.download_button(
            label="Download ws3d JAR",
            data=fp,
            file_name="ws3d.jar",
        )

    shutil.rmtree("ws3d/build")
    shutil.rmtree("ws3d/.gradle")

os.system("echo 'AFTER'")
os.system("cd ws3d && ls -a")

if st.button("Build DemoCST JAR"):
    with st.spinner("Building..."):
        os.system("cd DemoCST && ./gradlew build")

    with open("DemoCST/build/libs/DemoCST-0.0.4-full.jar", "rb") as fp:
        btn = st.download_button(
            label="Download DemoCST JAR",
            data=fp,
            file_name="democst.jar",
        )

    shutil.rmtree("DemoCST/build")
    shutil.rmtree("DemoCST/.gradle")