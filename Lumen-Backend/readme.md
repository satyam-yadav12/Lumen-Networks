# 🌌 Lumen Captures – Backend

**Lumen Captures** is the backend API powering an image-based platform where users can upload, manage, and explore public images.  
It’s built using **Flask + MongoDB** with a focus on modular design, security, and scalability.

---

## 🧠 Overview

This backend handles:

- 🔐 **JWT Authentication** (Access + Refresh)
- 🧑‍💻 **User management** (profiles, passwords, avatars)
- 🖼️ **Image upload & management**
- 📦 **Collections and favorites**
- 💬 **Feedback and reporting**
- 🔍 **Image search and public discovery**

All routes are protected using **JWT tokens** stored securely in HTTP-only cookies.

---

## ⚙️ Tech Stack

| Layer          | Technology                      |
| -------------- | ------------------------------- |
| Framework      | Flask                           |
| Database       | MongoDB (via PyMongo)           |
| Authentication | flask-jwt-extended              |
| Security       | Werkzeug password hashing, CORS |
| Architecture   | Modular MVC-style               |
| Deployment     | Render                          |

---

<!-- ## 📁 Project Structure

Lumen-Backend/
│
├── app/
│ ├── controllers/ # Core business logic
│ ├── middlewares/ # JWT auth & request validation
│ ├── models/ # MongoDB schemas
│ ├── routes/ # API route definitions
│ ├── services/ # Helper modules (upload, search)
│ ├── utils/ # Utility functions
│ ├── config.py # App configuration
│ ├── extensions.py # Flask extensions (JWT, DB, etc.)
│ └── init.py # App factory
│
├── run.py # Entry point
└── requirements.txt # Dependencies -->

## ⚡ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/satyam-yadav12/Lumen-Captures.git
cd Lumen-Captures/Lumen-Backend

# 2. Create a virtual environment
python -m venv venv

venv\Scripts\activate      # for Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables (.env)
SECRET_KEY = "secret key for app"
MONGO_URI="atlas connection string"
JWT_SECRET_KEY="secret key for jwt"
GOOGLE_CLIENT_ID= "your google client id"
GOOGLE_CLIENT_SECRET= "google client secret"
FRONTEND_ORIGIN="http://localhost:5173"
CLOUDINARY_CLOUD_NAME="cloud name"
CLOUDINARY_API_KEY="cloudinary api key"
CLOUDINARY_API_SECRET="cloudinary api secret"

# 5. Run the application
python run.py

Server runs at: http://127.0.0.1:5000
```
