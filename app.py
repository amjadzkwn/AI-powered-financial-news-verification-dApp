import streamlit as st
from fake_news_model import (
    load_model,
    predict_fake_news
)

# Page configuration
st.set_page_config(
    page_title="AI Fake News Detection",
    page_icon="🔍",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .result-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin-top: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .sentiment-positive {
        color: #10b981;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .sentiment-negative {
        color: #ef4444;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .sentiment-neutral {
        color: #f59e0b;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .fake-high {
        color: #ef4444;
        font-weight: bold;
    }
    .fake-low {
        color: #10b981;
        font-weight: bold;
    }
    .info-box {
        background: #2d3748;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        font-size: 1rem;
        border-left: 4px solid #667eea;
        color: #ffffff;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        font-size: 1rem;
        padding: 0.5rem 2rem;
        border-radius: 8px;
        border: none;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

# Header with icon
st.markdown("""
    <div class="main-header">
        <h1 style="color: white; margin: 0;">🤖 AI Powered Financial News Verification dApp</h1>
        <p style="color: #e0e7ff; margin: 0.5rem 0 0 0;">Advanced Financial News Authenticity Checker</p>
    </div>
""", unsafe_allow_html=True)

# Load trained model only
with st.spinner("🔄 Loading AI Model... Please wait"):
    model, vectorizer = load_model()

# Info box - FIXED with better contrast
st.markdown("""
    <div class="info-box">
        💡 <strong>Tip:</strong> Enter financial news below and click "Analyze" to check its authenticity.
        The AI will analyze sentiment, fake probability, and provide a classification.
    </div>
""", unsafe_allow_html=True)

# News input area
news = st.text_area(
    "📰 Enter Financial News",
    height=150,
    placeholder="Example: 'Stock market reaches all-time high as tech sector surges...'",
    help="Paste or type the financial news article you want to analyze"
)

# Analyze button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze_clicked = st.button("🔍 Analyze News", use_container_width=True)

if analyze_clicked:
    if news.strip():
        # Show spinner during analysis
        with st.spinner("📊 Analyzing news content..."):
            result = predict_fake_news(news, model, vectorizer)

        # Display results in a styled card
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.subheader("📈 Analysis Results")

        # Sentiment display with color coding
        sentiment = result["sentiment"]
        sentiment_lower = sentiment.lower()
        if "positive" in sentiment_lower:
            sentiment_class = "sentiment-positive"
            sentiment_icon = "😊"
        elif "negative" in sentiment_lower:
            sentiment_class = "sentiment-negative"
            sentiment_icon = "😞"
        else:
            sentiment_class = "sentiment-neutral"
            sentiment_icon = "😐"

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Sentiment:** <span class='{sentiment_class}'>{sentiment_icon} {sentiment}</span>",
                        unsafe_allow_html=True)

        # Fake probability with progress bar
        fake_prob = result["fake_probability"]
        fake_percentage = fake_prob * 100
        with col2:
            st.markdown(
                f"**Fake Probability:** <span class='{'fake-high' if fake_prob > 0.5 else 'fake-low'}'>{fake_percentage:.1f}%</span>",
                unsafe_allow_html=True)
            st.progress(fake_prob)

        st.markdown("---")

        # Classification with styled badge
        label = result["label"]
        if "fake" in label.lower():
            badge_color = "#ef4444"
            badge_icon = "⚠️"
        else:
            badge_color = "#10b981"
            badge_icon = "✅"

        st.markdown(f"""
            <div style="text-align: center; padding: 1rem; background: {badge_color}20; border-radius: 10px;">
                <h3 style="margin: 0; color: {badge_color}">{badge_icon} Classification: {label}</h3>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please enter some news text to analyze.")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666; font-size: 0.8rem;'>Powered by Advanced Machine Learning | Financial News Analysis</p>",
    unsafe_allow_html=True
)