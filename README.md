# Multiple Disease Prediction

## 📌 Project Overview
The **Multiple Disease Prediction System** is a machine learning–based application designed to assist in the **detection of multiple diseases**.  
It provides healthcare providers and patients with quick, scalable, and accurate predictions, reducing both diagnostic time and cost.

### 🎯 Objective
- Assist in **detection** of diseases.  
- Improve **decision-making** for healthcare providers.  
- Reduce diagnostic **time and cost** through automated predictions.  

---

## 🏗 System Architecture
- **Frontend**: Interactive user interface built with **Streamlit** for input (symptoms, test results).  
- **Backend**: Python-based ML models for processing and predictions.  
- **Models**: Logistic Regression, Random Forest, etc.  
- **Visualization**: Matplotlib, Seaborn, Plotly for interactive graphs.  

---

## ✨ Features
- 🔹 **Multi-disease Prediction**: Supports Chronic Kidney Disease (CKD), Chronic Liver Disease (CLD), and Parkinson’s Disease.  
- 🔹 **User-friendly Interface** with simple input forms and clear outputs.  
- 🔹 **Interactive Visualizations** to explain predictions.  
- 🔹 **Secure Data Handling** for user privacy.  
- 🔹 **Scalable System** capable of supporting more diseases in the future.  

---

## 📂 Project Structure
```
.
├── app.py                   # Streamlit app for disease prediction
├── Fun.py                   # Utility functions
├── requirements.txt         # Required Python packages
├── README.md                # Project documentation
│
├── ckd_code.ipynb           # CKD - Data Processing, EDA, Model Building
├── ckd_model.pkl            # Trained CKD model
├── ckd_info.md              # Documentation for CKD
├── ckd_logo.png             # CKD logo
│
├── cld_code_1.ipynb         # CLD - Data Processing, EDA, Model Building
├── cld_model.pkl            # Trained CLD model
├── cld_info.md              # Documentation for CLD
├── cld_logo.png             # CLD logo
│
├── parkinsons_code_1.ipynb  # Parkinson’s - Data Processing, EDA, Model Building
├── parkinsons_model.pkl     # Trained Parkinson’s model
├── parkinsons_info.md       # Documentation for Parkinson’s
├── parkinsons_logo.png      # Parkinson’s logo
│
├── try.ipynb                # Testing notebook
```

---

## ⚙️ Installation & Requirements
Clone the repository and install dependencies:

```bash
git clone <https://github.com/arun8nov/Multiple-Disease-prediction>
cd Multiple-Disease-prediction
pip install -r requirements.txt
```

### Requirements
- pandas  
- numpy  
- matplotlib  
- seaborn  
- plotly  
- scikit-learn  
- streamlit  
- imbalanced-learn  
- nbformat  

---

## 🚀 How to Run
1. Train or use pre-trained models (`.pkl` files).  
2. Start the Streamlit app:  
   ```bash
   streamlit run app.py
   ```
3. Open the app in your browser and enter patient details.  
4. View disease prediction results with probabilities and insights.  

---

## 🔬 Workflow
1. **Input Data**: User enters test results/symptoms.  
2. **Preprocessing**: Missing value handling, encoding, and scaling.  
3. **Model Inference**: Predictive ML models (per disease).  
4. **Output**: Prediction results with probabilities and risk levels.  

---

## 📊 Evaluation Metrics
- **Classification**: Accuracy, Precision, Recall, F1-score. 
- **App Performance**: Responsiveness and quality.

---

## 🛠 Tools & Technologies
- **Language**: Python  
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Plotly  
- **Frontend**: Streamlit  
- **ML Algorithms**: Logistic Regression, Random Forest. 

---

## 📈 Results
The system successfully predicts the probability of **CKD, CLD, and Parkinson’s Disease** with good accuracy.  
It enhances accessibility and efficiency in healthcare by enabling **Diesease detection** and reducing **manual diagnostic efforts**.

---

## 📌 Project Deliverables
- ✅ Source Code (Python + Jupyter Notebooks)  
- ✅ Pre-trained Models (`.pkl` files)  
- ✅ Streamlit App (`app.py`)  
- ✅ Documentation (this README + info files)  

---

## 🔖 Technical Tags
`Streamlit` `Python` `Machine Learning` `Healthcare` `Visualization`

---
## Author
Arunprakash B

web : https://crystal-acai-529.notion.site/Hey-there-I-am-Arunprakash-B-223fe4a17f8a80faa5abee1f246a06f1
