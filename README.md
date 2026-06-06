# Pathogenic-versus-beneficial-bacteria-classification
This is a Machine learning model to classify soil bactertia based on 16s rRNA sequences.
This repository contains an end-to-end Machine Learning pipeline built in Python to classify soil-borne bacteria majorly pathogenic (_Agrobacterium_ strain) and beneficial (_Rhizobium_)  based on  their 16S rRNA genomic sequences.

## Project Overview
Soil bacteria can look very similar genetically but have completely opposite impacts on plants. For example, *Agrobacterium* is a pathogen that causes diseases in crops, while *Rhizobium* is a beneficial microbe that helps plants grow through nitrogen fixation. Telling them apart is highly important for both agriculture and biological safety.

The goal of this project is to build a reliable Machine Learning pipeline that can automatically classify these two types of bacteria using their 16S rRNA genomic sequences. Instead of running slow alignment tools, this project uses a data-driven approach: breaking DNA sequences down into short pieces (k-mers) and calculating their frequency patterns using TF-IDF. 

By finding these hidden genomic patterns, the final trained model can quickly screen raw sequences and accurately predict whether a bacteria strain is harmful or beneficial, without needing heavy deep-learning setups.

## Dataset 
The model was trained on distinct genomic sequences of 16S rRNA in FASTA format obtained from NCBI:
- 'pathogenic_bacteria' - Agrobacterium.fasta: Contains genomic sequences of plant-pathogenic strains.
- 'beneficial_bacteria' - Rhizobium.fasta : Contains sequences of growth-promoting soil microbes.
  <br>
A perfectly balanced dataset of 500 pathogenic (*Agrobacterium*) and 500 beneficial (*Rhizobium*) strains was used to eliminate class imbalance bias. Aditionally, sequence lengths were strictly restricted to a 1,200 to 1,400 bp rang to filter out outliers and prevent size-based shortcut learning .


## Methodology
- **Sequence Tokenization:** Implemented k-mer tokenization to break down long DNA/RNA sequences into overlapping biological tokens.
- **Feature Extraction:** Utilized TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to capture structural genomic patterns.
- **Classification Models:** Trained and optimized classical Machine Learning models using Scikit-Learn, achieving an overall classification accuracy of **98% to 99%**.
- **Predictor Pipeline:** The final trained model and vectorizer pipeline were serialized using **Joblib / Pickle** to generate a reusable predictor file.
- This allows the model to be instantly loaded for predicting unknown 16S rRNA sequences without retraining.

## Data Visualization (Tech Stack)
 #### Languages and Frameworks: Python , Streamlit
 #### Libraries or Data Science Stack : Scikit-Learn, Pandas, NumPy
 #### Visualization: Used **Seaborn** and Matplotlib to plot evaluation metrics, including:
  Confusion Matrix (to analyze True Positives vs False Positives),
  Classification Reports (Precision, Recall, and F1-Score),
   validation : 5 fold cross validation
   
   ## images and plots
 <img width="850" height="547" alt="image" src="https://github.com/user-attachments/assets/b87abe00-feb2-4b8d-afe9-3b15b3d9f5b4" />
 <br>
 Figure 1: Sequence Length Distribution
 Filtered raw NCBI sequences using a histogram to ensure all data points strictly fall within the 1,200 to 1,400 bp range. This quality control step eliminates outliers and prevents the model from exploiting sequence length
<br>
<br>
 <img width="691" height="470" alt="image" src="https://github.com/user-attachments/assets/c9fb307e-a779-461f-a328-125e3d6fc9a3" />
<br>
 Figure 2: GC Content Distribution Peak
Plotted using Seaborn (sns.kdeplot) to analyze the chemical signature of both strains. The distinct, non-overlapping peaks demonstrate that plant-pathogenic and growth-promoting soil bacteria possess unique genomic signatures.
<br>
<br>
<img width="928" height="470" alt="image" src="https://github.com/user-attachments/assets/aa160d64-20a0-48e1-92c4-f804fc3766ae" />
<br>
Figure 3: Hexamer Feature Importance & Motif Signature
<br>
Visualized the distribution of high-impact k-mer tokens. Using a broad feature visualization (figsize=(10, 5)), the pipeline ensures the classifier evaluates complex double-hexamer distributed motifs rather than overfitting to a single isolated hexamer pattern
<br>
<br>
<img width="990" height="590" alt="image" src="https://github.com/user-attachments/assets/266bacab-365e-4dc5-b00b-98abd503e999" />
<br>
Figure 4: Model Performance Benchmarking & Comparative Analysis
A comparative analysis evaluating the accuracy of 5 different classical Machine Learning architectures (including Logistic Regression, Random Forest, SVM, Naive Bayes, and Gradient Boosting)
<br>
<br>
<img width="649" height="547" alt="image" src="https://github.com/user-attachments/assets/8fd689fa-7c4f-4073-898a-f373b1a6baf0" />
<br>
Figure 5: Confusion Matrix for Deployed Random Forest Classifier

Demonstrates high predictive precision on the test set, accurately classifying 103 Beneficial and 96 Pathogenic sequences. The zero False Negative rate (0 pathogens misclassified as beneficial) validates the model's reliability for biosecurity and diagnostic screening.
<br>
<br>
<img width="855" height="547" alt="image" src="https://github.com/user-attachments/assets/e14ca857-70fc-4f4c-9f28-eb57d5d914c5" />
<br>
Figure 6: Stability Boxplot across Multiple Random Seeds

### Model Selection & Robustness Evaluation (Stability Report)

To ensure the classifier learns robust biological features rather than memorizing noise, a rigorous stability analysis was performed. Six architectures were benchmarked across multiple random seeds and validated using 5-fold cross-validation. Performance was visualized via Boxplots to track variance.

| Model | CV Avg Accuracy (%) | Stability (Std Dev) |
| :--- | :---: | :---: |
| **Random Forest** | **99.250%** | **0.007289** |
| SVM (Linear) | 99.250% | 0.007289 |
| XGBoost | 99.000% | 0.008478 |
| KNN | 98.750% | 0.003953 |
| Logistic Regression | 98.125% | 0.005590 |
| Naive Bayes | 98.125% | 0.005590 |

**Key Insights:**
- **Final Predictor Selection:** While both Random Forest and Linear SVM achieved a peak accuracy of 99.25%, **Random Forest** was chosen for the final deployment pipeline due to its exceptional structural robustness across seed fluctuations and minimal standard deviation ($\sigma \approx 0.007$).
- **Overfitting Mitigation:** The tight distribution in the 5-fold cross-validation loops confirms that the ensemble model generalizes exceptionally well to unseen 16S rRNA sequences without relying on overfitting shortcuts.
 the robust performance of the classifier and the minimal false positive/negative rates validate that the pipeline generalizates exceptionally well without memorizing training data.


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
