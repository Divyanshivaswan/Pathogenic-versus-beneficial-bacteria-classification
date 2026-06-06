# Soil Bacteria Classification Using 16S rRNA Sequences
A practical Machine Learning project to classify soil bacteria into pathogenic (*Agrobacterium*) and beneficial (*Rhizobium*) strains based on genomic data.

This repository contains the complete Python pipeline, from downloading raw DNA data to deploying a web-based predictor application.

## Project Overview
Soil contains thousands of bacterial strains that look very similar but do completely different things. For example, *Agrobacterium* causes harmful diseases in crops, while *Rhizobium* helps plants grow by fixing nitrogen in the soil. Safely and quickly telling them apart is highly important for both agriculture and biological safety.

The goal of this project is to build a reliable Machine Learning model that automates this identification process using 16S rRNA genetic sequences. Instead of using traditional alignment tools that can be slow and computationally heavy, this pipeline uses a data-driven approach. Raw DNA strings are broken down into short biological tokens (k-mers) to analyze their frequency patterns. 

This allows the final model to quickly screen new, unknown sequences and flag whether they are harmful or beneficial without needing expensive deep-learning setups.

## Dataset & Quality Control
The model was trained on raw genomic sequences downloaded directly from NCBI:
- `pathogenic_bacteria_Agrobacterium.fasta`: Genomic data for plant-pathogenic strains.
- `beneficial_bacteria_Rhizobium.fasta`: Genomic data for growth-promoting soil microbes.

To ensure proper model training, the pipeline applies two main data engineering steps:
1. **Handling Class Imbalance:** Uses a perfectly balanced dataset of 500 pathogenic and 500 beneficial sequences to prevent the classifier from biasing toward one class.
2. **Preventing Shortcut Learning:** Filters the dataset to keep only sequences between 1,200 and 1,400 base pairs (bp). This quality control step removes extreme outliers and ensures the model doesn't cheat by simply memorizing sequence lengths instead of learning actual genomic features.

##  Pipeline 
- **Sequence Tokenization:** Splits long, continuous 16S rRNA strings into smaller, overlapping chunks called k-mers.
- **Feature Extraction:** Applies TF-IDF vectorization. Instead of treating DNA as raw text, this technique calculates the statistical weight and importance of specific sequence motifs across both bacterial groups.
- **Model Training:** Trains and fine-tunes multiple classical Machine Learning models using Scikit-Learn to establish a solid accuracy baseline of **98% to 99%**.
- **Model Saving & Deployment:** Serializes the final optimized pipeline using **Joblib / Pickle**. This packages the trained weights and text vectorizer into a single file so new sequences can be tested instantly without local retraining loops.

## Technical Stack
- **Languages & Frameworks:** Python, Streamlit
- **Data Science Libraries:** Scikit-Learn, Pandas, NumPy
- **Visualization:** Seaborn and Matplotlib (used to generate performance charts, confusion matrices, and classification reports).
- **Validation Strategy:** 5-fold cross-validation.
   
## Plots

<img width="850" height="547" alt="Sequence Length Distribution" src="https://github.com/user-attachments/assets/b87abe00-feb2-4b8d-afe9-3b15b3d9f5b4" />
<br>
Figure 1: Sequence Length Distribution  
*This histogram shows the data filtering process. By forcing all sequence lengths to fall strictly within the 1,200 to 1,400 bp window, the pipeline removes length bias so the model focuses purely on biological patterns.*

<br>
<br>

<img width="691" height="470" alt="GC Content Distribution" src="https://github.com/user-attachments/assets/c9fb307e-a779-461f-a328-125e3d6fc9a3" />
<br>
Figure 2: GC Content Distribution Peak  
*Plotted using Seaborn (`sns.kdeplot`) to check the chemical signature of both strains. The distinct, separate peaks prove that pathogenic and beneficial soil bacteria have clear genomic differences.*

<br>
<br>

<img width="928" height="470" alt="Feature Importance" src="https://github.com/user-attachments/assets/aa160d64-20a0-48e1-92c4-f804fc3766ae" />
<br>
Figure 3: Hexamer Feature Importance & Motif Signature  
*This chart tracks high-impact k-mer tokens. Using a wider visualization window (`figsize=(10, 5)`), it verifies that the classifier looks at broad motif clusters rather than overfitting to just one or two isolated tokens.*

<br>
<br>

<img width="990" height="590" alt="Model Benchmarking" src="https://github.com/user-attachments/assets/266bacab-365e-4dc5-b00b-98abd503e999" />
<br>
Figure 4: Model Performance Benchmarking & Stability Analysis  
*A clear comparison evaluating accuracy across 6 different classical machine learning models (including Naive Bayes, Logistic Regression, XGBoost, KNN, SVM and Random Forest ).*

<br>
<br>

<img width="649" height="547" alt="Confusion Matrix" src="https://github.com/user-attachments/assets/8fd689fa-7c4f-4073-898a-f373b1a6baf0" />
<br>
Figure 5: Confusion Matrix for Deployed Random Forest Classifier  
*Shows exact results on the testing data (103 Beneficial and 96 Pathogenic sequences correctly matched). Crucially, the pipeline achieves a **zero False Negative rate**, meaning no dangerous pathogens are missed or misclassified as safe—a vital requirement for screening tools.*

<br>
<br>

<img width="855" height="547" alt="Stability Boxplot" src="https://github.com/user-attachments/assets/e14ca857-70fc-4f4c-9f28-eb57d5d914c5" />
<br>
Figure 6: Stability Boxplot across Multiple Random Seeds  

### Model Selection & Robustness Report
To ensure the model learns reliable biological features instead of just memorizing training noise, 6 different architectures were tested across multiple random seeds using 5-fold cross-validation. 

| Model | CV Avg Accuracy (%) | Stability (Std Dev) |
| :--- | :---: | :---: |
| **Random Forest** | **99.250%** | **0.007289** |
| SVM (Linear) | 99.250% | 0.007289 |
| XGBoost | 99.000% | 0.008478 |
| KNN | 98.750% | 0.003953 |
| Logistic Regression | 98.125% | 0.005590 |
| Naive Bayes | 98.125% | 0.005590 |

**Key Decisions:**
- **Why Random Forest was selected:** Even though both Random Forest and Linear SVM hit a peak accuracy of 99.25%, **Random Forest** was chosen for final deployment because it showed excellent structural robustness and a minimal standard deviation ($\sigma \approx 0.007$) across different random seed splits.
- **Generalization:** The very tight accuracy distribution in the cross-validation loops proves that the model generalizes well to new sequences and does not rely on dataset-specific shortcuts.

## How to Test the Predictor
The trained model can be tested using two interactive methods included in this repository:

### Method 1: Google Colab Interactive Form
- Open the `.ipynb` notebook in Google Colab.
- Scroll down to the last cell titled **"16S rRNA Bacterial Sequence Predictor"**.
- Paste a raw DNA sequence into the input field on the right panel and hit Enter to get real-time predictions.

### Method 2: Local Streamlit Web Application (`app.py`)
- Clone this repository to the local machine.
- Install the required packages: `pip install streamlit scikit-learn pandas`
- Run the web app locally using: `streamlit run app.py`

## Limitations & Future Scope
- **Species Limitation:** Currently, this model functions as a targeted prototype trained specifically on *Agrobacterium* and *Rhizobium*. It does not classify other general types of soil bacteria yet.
- **Expanding the Database:** Future steps include adding a wider variety of agricultural threats (like *Ralstonia* or *Xanthomonas*) and beneficial microbes (like *Pseudomonas* or *Bacillus*) to make the framework more useful for real-world setups.
- **Biosecurity Applications:** In the future, this type of robustness testing can be integrated into DNA synthesis screening workflows. This will help DNA manufacturing facilities automatically check sequence orders and flag dangerous plant pathogens before they are physically synthesized.
