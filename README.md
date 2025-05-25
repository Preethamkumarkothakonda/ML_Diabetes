
### 📄 `README.md`

```markdown
# 🩺 Diabetes Prediction Web App

A responsive and interactive web application for predicting diabetes based on medical input features using a trained Machine Learning model (SVM). Built with Flask, HTML, CSS, JavaScript, and deployed for free.



🔗 **[Try the website Here](https://ml-diabetes-1-9gtd.onrender.com)**  
*(Deployed using Render – free hosting platform)*

---

## 💡 Features

- 🧠 **ML Model (SVM)**: Trained on the Pima Indians Diabetes Dataset.
- 🌐 **Frontend**: Beautiful, animated UI with form validations and prediction feedback.
- 🔥 **Flask Backend**: Handles predictions with your trained model and scaler.
- ⚡ **Deployed Free**: On Render.com using GitHub integration.
- 📊 **Prediction Output**: Binary result (Positive/Negative) with user-friendly display.

---

## 🛠 Tech Stack

| Frontend       | Backend     | ML Model     |
|----------------|-------------|--------------|
| HTML, CSS, JS  | Flask (Python) | SVM (Scikit-learn) |
| Animations via JS | REST API (JSON) | joblib for serialization |

---

## 🧪 Input Features

This app takes the following **8 medical inputs**:

1. Pregnancies  
2. Glucose  
3. Blood Pressure  
4. Skin Thickness  
5. Insulin  
6. BMI  
7. DiabetesPedigreeFunction  
8. Age  

---

## 📁 Project Structure

```

ML\_Diabetes\_Predictor/
│
├── app.py                  # Flask backend script
├── diabetes.pkl            # Trained SVM model
├── scaler.pkl              # StandardScaler used during training
├── requirements.txt        # Python dependencies
│
├── index.html          # Main HTML page
│
````

---

## ⚙️ Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Preethamkumarkothakonda/ML_Diabetes.git
   cd ML_Diabetes
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:

   ```bash
   python app.py
   ```

4. Open your browser and go to:

   ```
   http://localhost:5000
   ```

---

## ☁️ Deployment

This app is deployed using [Render](https://render.com):

* Connect your GitHub repo
* Add `requirements.txt` and `app.py`
* Set build command: `pip install -r requirements.txt`
* Set start command: `python app.py`
* Add `PORT` environment variable = `10000` or leave it as default

---

## 🙋‍♂️ Author

**Preetham Kumar Kothakonda**
👨‍💻 Machine Learning & Web Developer
🔗 [GitHub](https://github.com/Preethamkumarkothakonda)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🌟 Acknowledgements

* [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
* [Render](https://render.com)
* [Scikit-learn](https://scikit-learn.org/)

````

