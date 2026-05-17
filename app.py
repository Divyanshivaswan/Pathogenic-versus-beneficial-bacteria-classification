
import streamlit as st
import joblib
import numpy as np

# Page configuration 
st.set_page_config(page_title="Genomic Pathogen Predictor", page_icon="🔬", layout="centered")

# Load the model and vectorizer 
@st.cache_resource
def load_resources():
    # Make sure these filenames match exactly what you downloaded from Colab
    model = joblib.load('pathogen_model.pkl')
    tfidf = joblib.load('vectorizer.pkl')
    return model, tfidf

# Initializing the model and vectorizer
try:
    model, tfidf = load_resources()
except Exception as e:
    st.error("Error: Model files not found. Please ensure 'pathogen_model.pkl' and 'vectorizer.pkl' are in the same folder.")
    st.stop()

# User Interface
st.title("🧬 Bacterial Pathogen AI Classifier")
st.markdown("""
Welcome to the **Genomic Diagnostic Tool**. This application uses a **Random Forest Classifier** to identify bacterial types based on 16S rRNA gene sequences.
""")

st.sidebar.header("Project Details")
st.sidebar.info("""
- **Target 1:** Agrobacterium tumefaciens (Pathogen)
- **Target 0:** Rhizobium leguminosarum (Beneficial)
- **Method:** K-mer (Size=6) + TF-IDF Vectorization
""")

# Input section
st.subheader("Step 1: Input Sequence")
sequence_input = st.text_area("Paste the DNA Sequence below:", height=200, placeholder="Example: ATGCGT...")

# Prediction Logic
if st.button("Run Diagnostic Analysis"):
    if sequence_input:
        # 1. Cleaning the input
        clean_seq = sequence_input.upper().strip().replace("\n", "").replace("\r", "").replace(" ", "")

        # Validation
        if not all(base in "ATGC" for base in clean_seq) or len(clean_seq) < 10:
            st.error("⚠️ Invalid DNA sequence! Please ensure the sequence contains only A, T, G, C and is of sufficient length.")
        else:
            with st.spinner('Analyzing genomic patterns...'):
                # 2. Tokenization (matching your 'getKmers' function with size=6)
                k = 6
                kmers = [clean_seq[i:i+k].lower() for i in range(len(clean_seq) - k + 1)]
                sentence = " ".join(kmers)

                # 3. Vectorization
                vectorized_data = tfidf.transform([sentence])

                # 4. Prediction & Confidence
                prediction = model.predict(vectorized_data)[0]
                probabilities = model.predict_proba(vectorized_data)[0]
                confidence = np.max(probabilities) * 100

                # 5. Display Results
                st.divider()
                st.subheader("Step 2: Diagnostic Result")

                res_col1, res_col2 = st.columns(2)

                with res_col1:
                    if prediction == 1:
                        st.error("### ⚠️ Result: PATHOGEN")
                        st.write("**Species Identified:** *Agrobacterium tumefaciens*")
                    else:
                        st.success("### ✅ Result: BENEFICIAL")
                        st.write("**Species Identified:** *Rhizobium leguminosarum*")

                with res_col2:
                    st.metric("Confidence Score", f"{confidence:.2f}%")
                    st.progress(int(confidence))

                st.info(f"**Bio-Insight:** The model identified {len(kmers)} unique K-mer features to verify this classification.")
    else:
        st.warning("Please paste a sequence to start the analysis.")

st.divider()
st.caption("Developed for Bioinformatics Research | IARI Final Year Project")