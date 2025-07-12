# 🔁 SkillSwap – A Peer-to-Peer Skill Exchange Platform

**SkillSwap** is a fullstack web platform that allows users to **list the skills they offer**, **request skills they want to learn**, and **connect through direct swap requests**. Designed to promote **community learning**, the platform also includes **admin moderation tools** to ensure a safe and respectful user experience.

---

## 🚀 Problem Statement

Submitted for **Hackathon 2025** under the category:

> **Skill Swap Platform**  
> A mini application that enables users to list their skills and request others in return.

---

## 🛠️ Tech Stack

| Layer            | Technology Used                                     |
|------------------|-----------------------------------------------------|
| Frontend         | HTML, CSS (Bootstrap), JavaScript                   |
| Backend          | Python (Django)                                     |
| Database         | SQLite (default Django DB)                          |
| Authentication   | Django default auth (username/email, password)      |
| Version Control  | Git + GitHub                                        |

---

## ✨ Core Features (Planned & Implemented)

- 🔐 **User Authentication** – Register & login with email/password
- 👤 **User Profile** – Add name, location, toggle public/private, availability
- 🛠 **Skill Management** – Add "offered" and "wanted" skills
- 🔍 **Skill Discovery** – Browse users based on matching skills
- 🔄 **Swap Request Flow** – Send, accept, reject, and cancel skill swap requests
- 🛡️ **Admin Panel** – View/delete skills, soft-ban users
- ⭐ *Coming Soon:* Feedback and ratings after successful swaps

---

## 📂 Project Structure

```
.
├── core/                  # Core Django app (models, views, templates)
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── core/
│           ├── base.html
│           ├── home.html
│           ├── login.html
│           ├── profile.html
│           ├── register.html
│           ├── skills.html
│           └── swap_requests.html
│
├── skillswap/             # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
├── .gitignore
└── README.md              # Project README
```

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/skillswap.git
cd skillswap

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # On Windows
# OR
source venv/bin/activate     # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

---

## 🌐 Usage

- Visit `http://127.0.0.1:8000/`
- Register or log in
- Add your offered/wanted skills
- Browse users and send skill swap requests
- Visit `/admin/` for admin moderation tools


---

## 🙌 Contribution & Credits
- 🏁 Built for: Hackathon 2025 – Skill Swap Challenge
- 💡 Idea: Promote peer-to-peer learning by exchanging real-world skills
