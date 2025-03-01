import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
import pandas as pd

def process_text_area(text):
    return [item.strip().lower() for item in text.split() if item.strip()]



if "list1_content" not in st.session_state:
    st.session_state.list1_content = ""
if "list2_content" not in st.session_state:
    st.session_state.list2_content = ""
if "list3_content" not in st.session_state:
    st.session_state.list3_content = ""
if "generate_venn" not in st.session_state:
    st.session_state.generate_venn = False

st.header("⭕ Venn Diagram App ⭕")

st.sidebar.subheader("Choose Venn Diagram Type")
page = st.sidebar.radio("Select:", ["2 Lists", "3 Lists"])

if page == "2 Lists":
    st.subheader("Enter List Data")
    col1, col2 = st.columns(2)
    with col1:
        list1_text = st.text_area("List 1", key="list1_content")
        list1_name = st.text_input("List 1 name", value="List A", key="list1_name")
    with col2:
        list2_text = st.text_area("List 2", key="list2_content")
        list2_name = st.text_input("List 2 name", value="List B", key="list2_name")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Generate Venn Diagram"):
            st.session_state.generate_venn = True

    if st.session_state.generate_venn:
        list1 = process_text_area(st.session_state.list1_content)
        list2 = process_text_area(st.session_state.list2_content)

        if list1 and list2:
            st.subheader("Venn Diagram")
            fig, ax = plt.subplots()
            venn2([set(list1), set(list2)], (list1_name, list2_name))
            st.pyplot(fig)

            st.subheader("Analysis")
            set1, set2 = set(list1), set(list2)
            common_elements = set1 & set2

            if st.button("Show Common Elements"):
                st.write(f"Common Elements ({len(common_elements)}):", common_elements)

            unique_list1 = set1 - set2
            unique_list2 = set2 - set1

            if st.button("Show Unique to List 1"):
                st.write(f"Unique to {list1_name} ({len(unique_list1)}):", unique_list1)
            if st.button("Show Unique to List 2"):
                st.write(f"Unique to {list2_name} ({len(unique_list2)}):", unique_list2)
        else:
            st.warning("Please enter valid data in both lists.")

if page == "3 Lists":
    st.subheader("Enter List Data")
    col1, col2, col3 = st.columns(3)
    with col1:
        list1_text = st.text_area("List 1", key="list1_content")
        list1_name = st.text_input("List 1 name", value="List A", key="list1_name")
    with col2:
        list2_text = st.text_area("List 2", key="list2_content")
        list2_name = st.text_input("List 2 name", value="List B", key="list2_name")
    with col3:
        list3_text = st.text_area("List 3", key="list3_content")
        list3_name = st.text_input("List 3 name", value="List C", key="list3_name")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Generate Venn Diagram"):
            st.session_state.generate_venn = True

    if st.session_state.generate_venn:
        list1 = process_text_area(st.session_state.list1_content)
        list2 = process_text_area(st.session_state.list2_content)
        list3 = process_text_area(st.session_state.list3_content)

        if list1 and list2 and list3:
            st.subheader("Venn Diagram")
            fig, ax = plt.subplots()
            venn3([set(list1), set(list2), set(list3)], (list1_name, list2_name, list3_name))
            st.pyplot(fig)

            st.subheader("Analysis")
            set1, set2, set3 = set(list1), set(list2), set(list3)
            common_all = set1 & set2 & set3
            common_1_2 = (set1 & set2) - set3
            common_1_3 = (set1 & set3) - set2
            common_2_3 = (set2 & set3) - set1

            if st.button("Common in All Lists"):
                st.write(f"Common in all ({len(common_all)}):", common_all)
            if st.button("Common in List 1 & 2"):
                st.write(f"Common in {list1_name} & {list2_name} ({len(common_1_2)}):", common_1_2)
            if st.button("Common in List 1 & 3"):
                st.write(f"Common in {list1_name} & {list3_name} ({len(common_1_3)}):", common_1_3)
            if st.button("Common in List 2 & 3"):
                st.write(f"Common in {list2_name} & {list3_name} ({len(common_2_3)}):", common_2_3)
        else:
            st.warning("Please enter valid data in all three lists.")
            