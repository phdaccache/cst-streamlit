import streamlit as st
import os
import shutil
import subprocess

st.title("Test App")

if st.button("Build ws3d JAR"):
    with st.spinner("Building..."):
        os.system("cd ws3d && ./gradlew build")

    with open("ws3d/build/libs/ws3d-0.0.1-full.jar", "rb") as fp:
        btn = st.download_button(
            label="Download ws3d JAR",
            data=fp,
            file_name="ws3d.jar",
        )

    command = "java -jar ws3d/build/libs/ws3d-0.0.1-full.jar"
    generated_descriptors = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout

    shutil.rmtree("ws3d/build")
    shutil.rmtree("ws3d/.gradle")

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