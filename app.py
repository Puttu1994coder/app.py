import streamlit as st

# Define keywords for each funnel stage
keywords = {
    "awareness": ["what is", "how to", "guide", "tips"],
    "consideration": ["best", "compare", "vs", "review"],
    "conversion": ["buy", "discount", "book", "pricing"]
}

# Map funnel stages to landing page messages
landing_pages = {
    "awareness": "###  Welcome! Discover what we do and how it helps you.",
    "consideration": "###  Explore features, compare options, and learn why we’re the best.",
    "conversion": "###  Ready to act? Book now and get exclusive benefits!",
}

# Funnel detection logic
def detect_funnel_stage(query):
    for stage, words in keywords.items():
        if any(word in query.lower() for word in words):
            return stage
    return "awareness"  # default stage

# Streamlit UI
st.title("Funnel Stage Detector")
st.write("Enter a user query to classify the funnel stage and generate landing content.")

query = st.text_input("User Search Query")

if st.button("Generate Landing Page"):
    if query.strip() == "":
        st.error("Please enter a query.")
    else:
        stage = detect_funnel_stage(query)
        content = landing_pages[stage]
        st.success(f"Funnel Stage: **{stage.capitalize()}**")
        st.markdown(content, unsafe_allow_html=True)
