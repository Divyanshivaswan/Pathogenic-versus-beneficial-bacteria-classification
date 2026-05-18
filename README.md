# Pathogenic-versus-beneficial-bacteria-classification
A Machine learning model to classify soil bactertia based on 16s rRNA sequences.
This repository contains an end-to-end Machine Learning pipeline built in Python to classify soil-borne bacteria majorly pathogenic (_Agrobacterium_ strain) and beneficial (_Rhizobium_)  based on  their 16S rRNA genomic sequences.

## Project Overview
The objective of this project is to accurately distinguish between pathogenic strains (such as *Agrobacterium*) and beneficial variants (agrobacterium) found in soil . Instead of treating biological data purely as raw matrices, the pipeline applies customized feature engineering tailored for genomic sequences.

## Dataset & Biological Input
The model was trained on distinct genomic sequences of 16srRNA in FASTA format obtained from NCBI:
- `pathogenic_bacteria - Agrobacterium.fasta: Contains genomic sequences of plant-pathogenic strains.
- `beneficial_bacteria - Rhizobium.fasta : Contains sequences of growth-promoting soil microbes.

## Key Features & Methodology
- **Sequence Tokenization:** Implemented k-mer tokenization to break down long DNA/RNA sequences into overlapping biological tokens.
- **Feature Extraction:** Utilized TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to capture structural genomic patterns.
- **Classification Models:** Trained and optimized classical Machine Learning models using Scikit-Learn, achieving an overall classification accuracy of **98%**.

## Model Serialization & Deployment
- **Predictor Pipeline:** The final trained model and vectorizer pipeline were serialized using **Joblib / Pickle** to generate a reusable predictor file.
- This allows the model to be instantly loaded for predicting unknown 16S rRNA sequences without retraining.

## Data Visualization (Tech Stack)
 #### Languages and Frameworks: Python , Streamlit
 #### Libraries or Data Science Stack : Scikit-Learn, Pandas, NumPy
 #### Visualization: Used **Seaborn** and Matplotlib to plot evaluation metrics, including:
  Confusion Matrix (to analyze True Positives vs False Positives),
  Classification Reports (Precision, Recall, and F1-Score),
   validation : 5 fold cross validation
 
## How to Test the Predictor
You can test the trained model using two interactive methods included in this repository:

### Method 1: Interactive Google Colab Form (Inside Notebook)
- Open the `.ipynb` notebook in Google Colab.
- Scroll to the final cell titled **"16S rRNA Bacterial Sequence Predictor"**.
- Simply paste your raw DNA sequence into the interactive form field on the right and press enter to view real-time pathogenic/beneficial predictions.

### Method 2: Streamlit Web Application (`app.py`)
- Clone this repository locally.
- Install dependencies: `pip install streamlit scikit-learn pandas`
- Launch the web interface by running: `streamlit run app.py`

 ## Limitation & Future Scope##:
-Dataset Scope: The current classifier is a prototype trained specifically on Agrobacterium and Rhizobium sequences. 
 It does  not classify all general pathogenic or beneficial bacteria yet.

-Scaling the Dataset: Expanding the pipeline to include a wider diversity of soil-borne pathogens 
 (like Ralstonia or     Xanthomonas) and beneficial microbes (like Pseudomonas or Bacillus).

-Deep Learning Integration: Testing Deep Learning architectures (like CNNs or Transformers) as the sequence database
 grows larger.
