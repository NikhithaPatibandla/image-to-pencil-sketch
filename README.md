# 🖼️ Image to Pencil Sketch Web App

A Flask-based web application that converts user-uploaded images into pencil sketch artworks using OpenCV image processing techniques. Users can upload an image, view the original and sketch side-by-side, and download the generated sketch.

---

## 🚀 Live Demo

https://image-to-pencil-sketch-1mp2.onrender.com

---

## ✨ Features
- Upload image (JPG / PNG / JPEG)
- Convert image to pencil sketch using OpenCV
- Display original and sketch images
- Download generated sketch
- Clean and responsive UI
- Server-side image processing

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- OpenCV
- NumPy

### Frontend
- HTML
- CSS
- JavaScript

### Deployment
- Render
- Gunicorn

---

## 🧠 How It Works
1. User uploads an image via the web interface
2. Flask backend saves the image on the server
3. OpenCV processes the image using:
   - Grayscale conversion  
   - Image inversion  
   - Gaussian blur  
   - Image division for sketch effect
4. The processed pencil sketch is returned and displayed
5. User can download the final sketch

---

## 📁 Project Structure

```txt
image_to_pencil_sketch/
├── app.py
├── sketch.py
├── config.py
├── requirements.txt
├── runtime.txt
├── start.sh
├── static/
│   ├── style.css
│   ├── uploads/
│   ├── results/
├── templates/
│   └── index.html
└── README.md

---

## Run Locally

git clone https://github.com/NikhithaPatibandla/image-to-pencil-sketch.git
cd image-to-pencil-sketch
pip install -r requirements.txt
python app.py

Open browser:

http://127.0.0.1:5000

---

🌍 Deployment

This app is deployed on Render using Gunicorn and opencv-python-headless.

---

📌 Future Enhancements

    -Live sketch intensity control

    -Multiple sketch styles

    -Mobile-friendly UI

    -User authentication

    -Cloud image storage

---

👤 Author

Patibandla Nikhitha
B.Tech CSE (AI & ML)
Interested in AI, ML, Data Science, and Full-Stack Development