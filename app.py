import streamlit as st
from main_pipeline import run_pipeline
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from io import BytesIO

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="AI Feedback Intelligence Engine",
    layout="wide"
)

# =====================================
# FUTURISTIC UI STYLING
# =====================================
st.markdown("""
<style>

/* ===== Background ===== */
.stApp {
    background:
        radial-gradient(circle at 20% 20%, rgba(0,255,200,0.08), transparent 40%),
        radial-gradient(circle at 80% 80%, rgba(0,120,255,0.08), transparent 40%),
        linear-gradient(135deg, #0a0f1c 0%, #0f172a 50%, #111827 100%);
    background-attachment: fixed;
}

/* ===== Title Gradient ===== */
h1 {
    font-weight: 700 !important;
    background: linear-gradient(90deg, #00f5c3, #00bfff, #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* ===== Subtle fade animation ===== */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(10px);}
    to {opacity: 1; transform: translateY(0);}
}
section.main > div {
    animation: fadeIn 0.6s ease-in-out;
}

/* ===== Text Area ===== */
textarea {
    background-color: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(0,255,200,0.3) !important;
    border-radius: 12px !important;
}

/* ===== Button Glow ===== */
.stButton>button {
    background: linear-gradient(90deg, #00f5c3, #00bfff);
    border: none;
    border-radius: 10px;
    color: black;
    font-weight: 600;
    padding: 0.6em 1.2em;
}
.stButton>button:hover {
    box-shadow: 0 0 20px rgba(0,255,200,0.6);
}

/* ===== Metric Cards ===== */
.metric-card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 14px;
    border: 1px solid rgba(0,255,200,0.2);
    text-align: center;
    backdrop-filter: blur(6px);
}

/* ===== Expander Glow ===== */
details {
    background: rgba(255,255,255,0.04);
    border-radius: 12px;
    border: 1px solid rgba(0,255,200,0.15);
    padding: 10px;
    margin-bottom: 10px;
}

details:hover {
    border: 1px solid #00f5c3;
}

/* ===== Scrollbar ===== */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: linear-gradient(#00f5c3, #00bfff);
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================
st.title("🧠 AI Feedback Intelligence Engine")
st.caption("Transform raw product feedback into structured executive insights.")

st.divider()

# =====================================
# USER INPUT
# =====================================
st.subheader("Enter Product Feedback")
st.markdown("⚠️ **Instruction:** Submit only one feedback per line. Avoid paragraphs.")

user_input = st.text_area(
    "Feedback Input",
    placeholder="""Example:
App crashes when uploading images
Dashboard is slow
Login fails sometimes"""
)

analyze_button = st.button("🚀 Analyze Feedback")

# =====================================
# ANALYSIS LOGIC
# =====================================
if analyze_button and user_input.strip():

    feedback_list = [line.strip() for line in user_input.split("\n") if line.strip()]

    with st.spinner("Running AI Agents..."):
        result = run_pipeline(feedback_list)

    pattern_analysis = result["pattern_analysis"]
    insight_memo = result["insight_memo"]
    system_evaluation = result["system_evaluation"]

    st.success("AI Analysis Complete")

    # =====================================
    # METRICS ROW
    # =====================================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>High Priority Issues</h3>
            <h2>{pattern_analysis["high_priority_count"]}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Theme Count</h3>
            <h2>{len(pattern_analysis["detected_themes"])}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Bug Volume</h3>
            <h2>{pattern_analysis["category_distribution"].get("Bug", 0)}</h2>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # =====================================
    # EXPANDERS
    # =====================================
    with st.expander("🔍 Detected Themes"):
        for theme in pattern_analysis["detected_themes"]:
            st.markdown(f"**{theme['theme']}**")
            for issue in theme["related_problems"]:
                st.write("–", issue)

    with st.expander("📊 Category Distribution"):
        st.bar_chart(pattern_analysis["category_distribution"])

    with st.expander("📈 Priority Distribution"):
        st.bar_chart(pattern_analysis["priority_distribution"])

    with st.expander("📝 Executive Insight Memo"):
        st.write(insight_memo)

    with st.expander("🧾 System Evaluation Summary"):
        st.write(system_evaluation)

    # =====================================
    # PDF DOWNLOAD
    # =====================================
    def generate_pdf(memo_text):
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer)
        styles = getSampleStyleSheet()
        elements = []

        elements.append(Paragraph("AI Feedback Intelligence Report", styles["Heading1"]))
        elements.append(Spacer(1, 0.3 * inch))
        elements.append(Paragraph(memo_text, styles["Normal"]))

        doc.build(elements)
        buffer.seek(0)
        return buffer

    pdf_buffer = generate_pdf(insight_memo)

    st.download_button(
        label="📥 Download Executive Memo (PDF)",
        data=pdf_buffer,
        file_name="Product_Insight_Memo.pdf",
        mime="application/pdf"
    )

elif analyze_button:
    st.warning("Please enter at least one feedback line.")