# Legal AI

## Our Mission: Justice as a Right, Not a Luxury
In a world where legal representation is often tied to financial capability, the scales of justice can sometimes tilt in favor of those who can afford it. **Legal AI** was built on the core moral principle that everyone deserves access to fair, objective, and immediate legal insight, regardless of their background or financial standing. 

Legal matters, particularly family law (like divorce and custody), are deeply emotional and exhausting. Our goal is to alleviate this burden by offering a purely data-driven, non-judgmental analysis that provides clarity in times of vulnerability.

---

## What Makes This Project Different?
While traditional legal consultations require scheduling, fees, and emotional toll, this project aims to provide:
- **Objective Clarity:** By analyzing historical case data, the AI provides an unbiased look into probable outcomes. It removes human prejudice and emotional sway from the equation.
- **Immediate Empowerment:** Instead of waiting weeks for a preliminary analysis, individuals can immediately understand the key legal points of their case documents.
- **Accessibility:** Empowering ordinary citizens to understand complex legal jargon and expected compensation without spending exorbitant fees on day one.

---

## How to Use Legal AI
Using the application is straightforward and designed for non-technical users seeking guidance:
1. **Case Summarization:** Simply upload your legal PDF documents. The AI instantly reads through the complex legalese and provides a clear, bulleted summary of the core facts.
2. **Outcome Prediction:** Fill in a few baseline details about your scenario (e.g., salaries, reason for separation). The AI compares your data against thousands of similar historical cases to predict:
   - Who is most likely to receive custody.
   - What the estimated compensation will be (calculated in ₹ Rupees).
3. **Chatbot Assistance:** Chat directly with the AI for any general legal queries. *(Coming Soon / Active Integration)*

---

## The AI Behind the Predictions
To provide the most accurate and unbiased insights, this platform relies on a sophisticated machine learning pipeline:

### The Dataset
Our models are trained on `Modified_Final_Database.xlsx`, a comprehensive dataset of anonymized historical family law cases. The dataset includes critical features such as:
- **Financial Standing** (Father's Salary, Mother's Salary)
- **Family Dynamics** (Child's Age)
- **Case Background** (Divorce Status, Reason for Divorce)
- **Historical Outcomes** (Granted Custody, Compensation Amount)

### The Methodology & Models
When a user submits their case details, the backend (built with Python, scikit-learn, and pandas) processes the data through a rigorous pipeline:
1. **Data Preprocessing:** Categorical data (like the Reason for Divorce) is transformed using *One-Hot Encoding*, while numerical data (Salaries, Child Age) is normalized using a *StandardScaler*. This ensures the AI weighs all factors fairly.
2. **Custody Prediction (Classification):** We utilize a **Random Forest Classifier** to predict categorical outcomes (e.g., whether the Mother, Father, or Both receive custody). This model builds multiple decision trees during training and merges them together to get a more accurate and stable prediction.
3. **Compensation Estimation (Regression):** For financial predictions, we use a **Random Forest Regressor**. Rather than outputting a category, it calculates a continuous numerical value—representing the estimated base compensation—which the frontend then automatically converts to Indian Rupees.

By leveraging these ensemble learning methods, the AI minimizes human bias, avoids overfitting, and provides an objective baseline drawn directly from historical legal precedents.

---

## Scaling for Impact
Currently, this AI serves as a guiding tool for family law, but its potential scale is massive:
- **Pro-Bono Law Firm Integration:** We aim to offer this tool to non-profit legal aid societies. They can use the summarizer to process case files 10x faster, allowing them to help more underprivileged clients.
- **Multilingual Support:** Justice shouldn't be limited to English speakers. Scaling the natural language processing to understand regional languages will democratize legal access for millions in rural areas.
- **Integration with Courts:** In the future, this system could be used by junior magistrates to quickly reference precedents, drastically reducing the massive backlog of pending cases in the justice system.

---

## Future Plans
Our roadmap is driven by social impact:
- **Expansion of Legal Domains:** Moving beyond family law to include tenant-landlord disputes, labor laws, and consumer rights.
- **Empathy Engine:** Refining the AI's communication style so that when delivering difficult predictions, it uses supportive, trauma-informed language.
- **Verified Legal Partner Handoff:** If a case is predicted to be highly complex, the app will securely and seamlessly hand off the summarized data to verified pro-bono human lawyers.

---

## Technical Quick-Start
*(For developers looking to contribute to our mission)*

**1. Clone the repository**
```bash
git clone https://github.com/Raman909/Legal-AI.git
```

**2. Start the Backend (Port 5000)**
```powershell
cd backened
python check.py
```

**3. Start the Frontend**
```powershell
cd frontened
npm install
npm run dev
```

*Join us in making justice accessible to all.*
