"""
AIAgronomist - AI-Powered Agricultural Assistant
A Streamlit application that helps farmers and agricultural enthusiasts
get insights about crops, weather, and farming best practices.
"""

import streamlit as st


def main():
    """Main function to run the AIAgronomist Streamlit application."""
    # Page configuration
    st.set_page_config(
        page_title="AIAgronomist",
        page_icon="🌾",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Main title
    st.title("🌾 AIAgronomist")
    st.subheader("Your AI-Powered Agricultural Assistant")

    # Sidebar for navigation
    st.sidebar.header("Navigation")
    page = st.sidebar.radio(
        "Select a page:",
        ["Home", "Crop Information", "Weather Insights", "Pest Management", "About"]
    )

    if page == "Home":
        show_home_page()
    elif page == "Crop Information":
        show_crop_information()
    elif page == "Weather Insights":
        show_weather_insights()
    elif page == "Pest Management":
        show_pest_management()
    elif page == "About":
        show_about_page()


def show_home_page():
    """Display the home page with an overview of the application."""
    st.markdown("""
    ## Welcome to AIAgronomist! 👋
    
    AIAgronomist is your intelligent companion for all things agriculture. 
    Whether you're a seasoned farmer or just starting your gardening journey, 
    we're here to help you grow better.
    
    ### What can you do here?
    
    - 🌱 **Crop Information**: Learn about different crops, their growing seasons, 
      and optimal conditions
    - 🌤️ **Weather Insights**: Understand how weather affects your crops
    - 🐛 **Pest Management**: Identify and manage common agricultural pests
    - 📚 **Expert Knowledge**: Access agricultural best practices and tips
    
    ---
    
    *Select a page from the sidebar to get started!*
    """)

    # Quick stats section
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Crops Database", "100+", help="Number of crops in our database")
    with col2:
        st.metric("Growing Tips", "500+", help="Expert growing tips available")
    with col3:
        st.metric("Pest Solutions", "200+", help="Pest management solutions")


def show_crop_information():
    """Display crop information page."""
    st.header("🌱 Crop Information")
    st.write("Search for crops and learn about their growing conditions.")

    # Search input
    crop_search = st.text_input("Search for a crop:", placeholder="e.g., Tomato, Wheat, Rice")

    # Common crops dropdown
    common_crops = st.selectbox(
        "Or select from common crops:",
        ["Select a crop...", "Tomato", "Wheat", "Rice", "Corn", "Potato", 
         "Soybean", "Cotton", "Sugarcane"]
    )

    if crop_search or common_crops != "Select a crop...":
        selected_crop = crop_search if crop_search else common_crops
        st.subheader(f"Information about {selected_crop}")

        # Display placeholder crop information
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Growing Season:** Spring - Fall
            
            **Optimal Temperature:** 18-26°C
            
            **Water Requirements:** Moderate
            
            **Soil Type:** Well-drained, fertile soil
            """)
        with col2:
            st.markdown("""
            **Days to Harvest:** 60-90 days
            
            **Sunlight:** Full sun (6-8 hours)
            
            **pH Level:** 6.0-7.0
            
            **Spacing:** 30-60 cm apart
            """)


def show_weather_insights():
    """Display weather insights page."""
    st.header("🌤️ Weather Insights")
    st.write("Understand how weather conditions affect your crops.")

    # Location input
    location = st.text_input("Enter your location:", placeholder="e.g., City, Country")

    if location:
        st.info(f"📍 Showing weather insights for: **{location}**")

    # Weather factors
    st.subheader("Key Weather Factors for Agriculture")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Temperature 🌡️
        Temperature affects plant growth rates, flowering, and fruit 
        development. Most crops have optimal temperature ranges.
        
        ### Rainfall 🌧️
        Water is essential for plant growth. Both too little and 
        too much rainfall can harm crops.
        """)
    with col2:
        st.markdown("""
        ### Humidity 💧
        High humidity can promote fungal diseases, while low humidity 
        can cause water stress in plants.
        
        ### Sunlight ☀️
        Plants need light for photosynthesis. Different crops have 
        varying light requirements.
        """)

    # Tips section
    st.info("💡 **Tip:** Monitor weather forecasts regularly and plan your farming " 
            "activities accordingly to maximize yield and minimize losses.")


def show_pest_management():
    """Display pest management page."""
    st.header("🐛 Pest Management")
    st.write("Identify and manage common agricultural pests.")

    # Pest categories
    pest_category = st.selectbox(
        "Select pest category:",
        ["Select category...", "Insects", "Diseases", "Weeds", "Rodents"]
    )

    if pest_category != "Select category...":
        st.subheader(f"Common {pest_category} in Agriculture")

        if pest_category == "Insects":
            st.markdown("""
            - **Aphids**: Small sap-sucking insects
            - **Caterpillars**: Larvae that feed on leaves
            - **Beetles**: Can damage roots, leaves, and fruits
            - **Whiteflies**: Tiny white insects on leaf undersides
            """)
        elif pest_category == "Diseases":
            st.markdown("""
            - **Powdery Mildew**: White powdery coating on leaves
            - **Blight**: Rapid browning and death of plant tissue
            - **Root Rot**: Fungal infection of plant roots
            - **Rust**: Orange-brown pustules on leaves
            """)
        elif pest_category == "Weeds":
            st.markdown("""
            - **Crabgrass**: Aggressive grass weed
            - **Dandelion**: Common broadleaf weed
            - **Bindweed**: Climbing vine that chokes crops
            - **Nutsedge**: Difficult-to-control sedge weed
            """)
        elif pest_category == "Rodents":
            st.markdown("""
            - **Field Mice**: Damage crops and stored grain
            - **Rats**: Can destroy large quantities of stored food
            - **Gophers**: Create tunnels that damage roots
            - **Voles**: Gnaw on bark and roots
            """)

    # Management tips
    st.subheader("General Pest Management Tips")
    st.success("""
    - 🔍 **Regular Monitoring**: Inspect crops frequently for early detection
    - 🌿 **Crop Rotation**: Helps break pest cycles
    - 🐞 **Beneficial Insects**: Encourage natural predators
    - 🧹 **Sanitation**: Remove crop residues and debris
    - 🌱 **Resistant Varieties**: Choose pest-resistant crop varieties
    """)


def show_about_page():
    """Display about page."""
    st.header("📚 About AIAgronomist")

    st.markdown("""
    ## Our Mission
    
    AIAgronomist aims to democratize agricultural knowledge and make it 
    accessible to farmers, gardeners, and agricultural enthusiasts worldwide.
    
    ## Features
    
    - **Comprehensive Crop Database**: Information on hundreds of crops
    - **Weather Integration**: Understand weather impacts on your farm
    - **Pest Management**: Identify and control agricultural pests
    - **Best Practices**: Expert agricultural recommendations
    
    ## Technology
    
    Built with:
    - 🐍 Python
    - 🎈 Streamlit
    - 🤖 AI-powered insights
    
    ---
    
    *AIAgronomist is continuously improving. Stay tuned for new features!*
    """)

    # Contact section
    st.subheader("Get in Touch")
    st.write("Have questions or feedback? We'd love to hear from you!")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            if name and email and message:
                st.success("Thank you for your message! We'll get back to you soon.")
            else:
                st.warning("Please fill in all fields.")


if __name__ == "__main__":
    main()
