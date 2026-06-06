# Pathogenic-versus-beneficial-bacteria-classification
This is a Machine learning model to classify soil bactertia based on 16s rRNA sequences.
This repository contains an end-to-end Machine Learning pipeline built in Python to classify soil-borne bacteria majorly pathogenic (_Agrobacterium_ strain) and beneficial (_Rhizobium_)  based on  their 16S rRNA genomic sequences.

## Project Overview
Soil bacteria can look very similar genetically but have completely opposite impacts on plants. For example, *Agrobacterium* is a pathogen that causes diseases in crops, while *Rhizobium* is a beneficial microbe that helps plants grow through nitrogen fixation. Telling them apart is highly important for both agriculture and biological safety.

The goal of this project is to build a reliable Machine Learning pipeline that can automatically classify these two types of bacteria using their 16S rRNA genomic sequences. Instead of running slow alignment tools, this project uses a data-driven approach: breaking DNA sequences down into short pieces (k-mers) and calculating their frequency patterns using TF-IDF. 

By finding these hidden genomic patterns, the final trained model can quickly screen raw sequences and accurately predict whether a bacteria strain is harmful or beneficial, without needing heavy deep-learning setups.

## Dataset & Quality Control
The model was trained on raw genomic sequences downloaded directly from NCBI:
- `pathogenic_bacteria_Agrobacterium.fasta`: Genomic data for plant-pathogenic strains.
- `beneficial_bacteria_Rhizobium.fasta`: Genomic data for growth-promoting soil microbes.

To ensure proper model training, the pipeline applies two main data engineering steps:
1. **Handling Class Imbalance:** Uses a perfectly balanced dataset of 500 pathogenic and 500 beneficial sequences to prevent the classifier from biasing toward one class.
2. **Preventing Shortcut Learning:** Filters the dataset to keep only sequences between 1,200 and 1,400 base pairs (bp). This quality control step removes extreme outliers and ensures the model doesn't cheat by simply memorizing sequence lengths instead of learning actual genomic features.


## Core Pipeline & Feature Engineering
- **Sequence Tokenization:** Implemented a rolling k-mer extraction strategy to segment long continuous 16S rRNA sequences into overlapping biological tokens.
- **Feature Extraction:** Applied TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to capture structural genomic patterns and motif weights across classes rather than processing raw characters.
- **Classification Approach:** Evaluated and tuned classical Machine Learning frameworks using Scikit-Learn, pushing the baseline to a peak classification accuracy of **98% to 99%**.
- **Model Inference & Deployment:** Serialized the final trained pipeline using **Joblib / Pickle** to generate a portable predictor module. This allows the model to instantly ingest and predict unseen 16S rRNA sequences without requiring local retraining loops.

## Technical Stack & Diagnostic Suite
- **Languages & Frameworks:** Python, Streamlit
- **Data Science Stack:** Scikit-Learn, Pandas, NumPy
- **Visualization Suite:** Utilized **Seaborn** and Matplotlib to generate performance diagnostic plots, including:
- **Confusion Matrices:** Tracking predictive precision and checking for critical False Negatives.
- **Classification Reports:** Documenting structural Precision, Recall, and F1-Scores.
- **validation:**  5 fold cross validation
   
## Visual Insights & Diagnostic Plots

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
*A clear comparison evaluating accuracy across 5 different classical machine learning models (including Logistic Regression, Random Forest, SVM, Naive Bayes, and Gradient Boosting).*

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
