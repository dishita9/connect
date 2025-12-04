import streamlit as st
import pandas as pd
import os
from datetime import datetime

# =====================================================
# Setup
# =====================================================
st.set_page_config(page_title="SponsorConnect Pro", layout="wide")

SEEKERS_FILE = "seekers_data.csv"
SPONSORS_FILE = "sponsors_data.csv"

if not os.path.exists(SEEKERS_FILE):
    pd.DataFrame().to_csv(SEEKERS_FILE, index=False)

if not os.path.exists(SPONSORS_FILE):
    pd.DataFrame().to_csv(SPONSORS_FILE, index=False)


# =====================================================
# Helper functions
# =====================================================
def save_data(file, new_row):
    try:
        df = pd.read_csv(file)
    except:
        df = pd.DataFrame()

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(file, index=False)


def load_data(file):
    try:
        return pd.read_csv(file)
    except:
        return pd.DataFrame()


# =====================================================
# UI Components
# =====================================================
def landing_page():
    st.title("🚀 SponsorConnect Pro")
    st.write(
        """
        A complete ecosystem to connect **Sponsors**, **Stall Providers**,  
        and **Sponsorship Seekers**. Streamlined. Professional. Efficient.
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🙋 Looking for Sponsors or Stalls?")
        st.write("Submit your business details and requirements.")
        if st.button("Fill Seeker Form"):
            st.session_state["page"] = "seekers"

    with col2:
        st.subheader("🏢 Are You a Sponsor or Stall Provider?")
        st.write("Share your offerings and opportunities.")
        if st.button("Fill Sponsor Form"):
            st.session_state["page"] = "sponsors"

    st.markdown("---")
    st.info("🔐 Admin? Go to Dashboard from the sidebar.")


def seekers_form():
    st.header("🙋 Sponsorship / Stall Requirement Form")

    with st.form("seekers_form"):
        name = st.text_input("Business / Organization Name*", "")
        desc = st.text_area("Describe your business and goals*", "")
        target = st.text_input("Target Audience*", "")
        type_needed = st.selectbox(
            "Type of Support Needed*", ["Sponsorship", "Stall", "Both"]
        )
        budget = st.text_input("Budget Range*", "")
        event_info = st.text_area("Event Details*", "")
        website = st.text_input("Website (optional)")
        email = st.text_input("Email*", "")
        phone = st.text_input("Phone*", "")
        social = st.text_input("Social Media Links")
        pitch = st.file_uploader("Upload Pitch Deck / Logo (optional)")

        submitted = st.form_submit_button("Submit")

        if submitted:
            if not (name and desc and target and type_needed and budget and event_info and email and phone):
                st.error("Please fill all required fields marked with *")
            else:
                save_data(SEEKERS_FILE, {
                    "timestamp": datetime.now(),
                    "name": name,
                    "description": desc,
                    "target_audience": target,
                    "support_type": type_needed,
                    "budget_range": budget,
                    "event_details": event_info,
                    "website": website,
                    "email": email,
                    "phone": phone,
                    "social_links": social
                })
                st.success("Your request has been submitted successfully!")


def sponsors_form():
    st.header("🏢 Sponsor / Stall Provider Form")

    with st.form("sponsor_form"):
        org = st.text_input("Organization Name*", "")
        contact = st.text_input("Contact Person*", "")
        category = st.selectbox(
            "Sponsorship Category*", ["Gold", "Silver", "Bronze", "Stall Provider", "Custom"]
        )
        products = st.text_area("Products / Services*", "")
        budget_offer = st.text_input("Budget Offered*", "")
        interest_area = st.text_input("Events/Regions Interested In*", "")
        email = st.text_input("Email*", "")
        phone = st.text_input("Phone*", "")
        website = st.text_input("Website")
        social = st.text_input("Social Media Links")

        submitted = st.form_submit_button("Submit")

        if submitted:
            if not (org and contact and category and products and budget_offer and interest_area and email and phone):
                st.error("Please fill all required fields marked with *")
            else:
                save_data(SPONSORS_FILE, {
                    "timestamp": datetime.now(),
                    "organization": org,
                    "contact_person": contact,
                    "category": category,
                    "products_services": products,
                    "budget_offer": budget_offer,
                    "interest_area": interest_area,
                    "email": email,
                    "phone": phone,
                    "website": website,
                    "social_links": social
                })
                st.success("Your details have been submitted successfully!")


# =====================================================
# Admin Dashboard
# =====================================================
def admin_dashboard():
    st.title("📊 Admin Dashboard")

    password = st.text_input("Enter Admin Password", type="password")
    if password != "admin123":
        st.warning("Enter password to access dashboard.")
        return

    st.success("Access granted!")

    seekers_data = load_data(SEEKERS_FILE)
    sponsors_data = load_data(SPONSORS_FILE)

    st.subheader("📥 Sponsorship / Stall Seekers Data")
    st.datafr
