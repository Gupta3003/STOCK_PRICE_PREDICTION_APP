# 📈 Stock Price Prediction Mobile App

## 🧠 Project Overview

This project presents a mobile-based stock market analysis system that uses **Machine Learning (ML)** to predict stock prices. At its core, an **LSTM (Long Short-Term Memory)** model is trained using a decade of historical stock data and technical indicators to forecast future prices. 

The prediction results are served through a responsive **Kotlin-based Android application** that communicates with a **Flask backend** via secure REST APIs. The app supports personalized features such as watchlists, interactive charts, and real-time data fetching using the Yahoo Finance API.

---

## 🎯 Objectives

- Develop a stock prediction model using **LSTM** trained on historical stock prices.
- Improve prediction accuracy by integrating **technical indicators** such as RSI, MACD, Bollinger Bands, SMA, and EMA.
- Deliver real-time insights via an **Android mobile application**.
- Provide a **user-friendly** and intuitive interface for both novice and experienced investors.
- Implement **secure user authentication** using JWT tokens.

---

## ⚙️ Key Features

- 📲 **Android App**: Built using Kotlin, offering responsive and modern design.
- 🔐 **Authentication**: JWT-based login/signup system.
- 📉 **ML Model**: Predicts stock prices using LSTM and technical indicators.
- 📊 **Interactive Charts**: View historical trends and forecast results.
- ⭐ **Watchlist**: Save and track preferred stocks.
- 🔄 **Real-Time Updates**: Integrated with `yfinance` API for live data.
- 📬 **Push Notifications**: Notify users of major stock events and alerts.
- 💾 **SQL Database**: Manages users, predictions, and watchlists.

---

## 📽️ Demo Vedio
[https://github.com/user-attachments/assets/e29564b8-b29f-4e13-ae4b-1c360c9f8dd9](https://github.com/user-attachments/assets/853d26d4-181d-4a48-9649-d37c46a9378a)
---
## ScreenShort
### 🔐 Signup & Login
|Signin/Login Page                                                                               |Signup Page                                                                                    |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
|![Sign in page](https://github.com/user-attachments/assets/14627f5b-ee2d-4099-9176-a5d1535af734)|![Signup page](https://github.com/user-attachments/assets/19c26e9f-e75f-4fba-b944-86351909cd14)|

### 🏠 Home & Dashboard
|Home Page                                                                                    |Dashboard Page                                                                               |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
|![Home Page](https://github.com/user-attachments/assets/5929d0a7-14a4-4ed5-98de-a35f37c7764c)|![Dashboard](https://github.com/user-attachments/assets/195e3192-863c-4c90-83a6-3d34fdc18bc5)|

### 📰 News & 📈 TCS Stock Price 
|News Page                                                                                    |TCS Stock Price Page                                                                         |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
|![News Page](https://github.com/user-attachments/assets/66514520-8bb9-4fb4-924f-d97a31f11ed4)|![TCS price](https://github.com/user-attachments/assets/b11d66fe-df93-4084-8494-ba0576201f10)|

---

## 🧠 Technologies Used

### 🔍 Machine Learning
- LSTM (Keras/TensorFlow)
- Technical Indicators: RSI, MACD, Bollinger Bands, SMA, EMA
- Data Libraries: Pandas, NumPy, Scikit-learn

### 📱 Android Frontend
- Kotlin
- Android Studio
- XML UI Layouts

### 🌐 Backend
- Python 3.8+
- Flask (REST API)
- JWT (Authentication)
- yfinance (Data fetching)

### 🗄️ Database
- MySQL (Production)
- Secure storage of users, predictions, watchlists

### 📊 Visualization
- Matplotlib
- Seaborn

---

## 🧪 Testing Summary

### ✔️ Functional Testing
- User login, registration, session handling
- Watchlist and stock search features
- Input validation and error handling
- Prediction accuracy verification

### ⚡ Performance Testing
- App responsiveness under single-user conditions
- Efficient data retrieval and rendering
- Optimized memory usage

### 🔧 Usability Testing
- Clean and accessible UI
- Responsive layouts across screen sizes
- Informative tooltips and error messages

---

## 🧩 System Architecture

- **Presentation Layer**: Kotlin-based Android mobile app
- **Application Layer**: Flask backend with ML model integration
- **Data Layer**: MySQL for persistent user and stock data

---

## 🧱 Core Modules

- **Authentication Module**: User login/signup using JWT
- **Stock Data Module**: Fetch and process real-time/historical data
- **Prediction Engine**: LSTM model predicts future prices
- **User Interface Module**: Handles app navigation and interaction
- **Database Interface Module**: Handles all DB operations

---

## 👨‍💻 Team Members & Responsibilities

- **Bhavya Gupta** – Machine Learning & Data Analysis  
  Trained LSTM, SVR, and Random Forest models. Selected LSTM based on performance. Handled feature engineering and data preprocessing.

- **Aaditya Sharma** – Backend & API Integration  
  Developed Flask APIs, implemented JWT authentication, connected ML model to frontend, and handled data routing.

- **Ansh Tyagi** – Android App Development  
  Designed the mobile UI in Kotlin, integrated backend APIs, and optimized app layout and responsiveness.

---

## 🚀 Future Enhancements

- 🌐 Web and iOS versions
- 🗞️ Sentiment analysis using news & social media
- 📊 Portfolio tracking and profit/loss visualization
- 🔔 Smart alerts for stock events
- 🌍 Multilingual and accessibility improvements

---

## ✅ Conclusion

This project bridges the gap between complex stock market analysis and user accessibility. By combining advanced ML models with intuitive mobile design, it empowers users to make informed financial decisions. The app is reliable, scalable, and built for real-world usage and future expansion.

---
