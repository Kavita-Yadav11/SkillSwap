# 🔁 SkillSwap – A Peer-to-Peer Skill Exchange Platform

SkillSwap is a fullstack web platform that allows users to **list the skills they offer**, **request skills they want to learn**, and **connect through direct swap requests**. Designed to promote community learning, the platform also includes **admin moderation tools** for a safe and respectful user experience.

---

## 🚀 Problem Statement
Submitted for **Hackathon 2025** under the category:

> **Skill Swap Platform**  
> A mini application that enables users to list their skills and request others in return.

---

## 🛠️ Tech Stack

| Layer        | Technology Used     |
|--------------|---------------------|
| Frontend     | HTML, CSS (Tailwind or Bootstrap), JavaScript or React |
| Backend      | Python (Django)     |
| Database     | SQLite (for prototype) |
| Auth         | Django default auth (username/email, password) |
| Version Control | Git + GitHub     |

---

## ✨ Core Features (Planned)

- 🔐 User registration/login
- 👤 User profile (skills offered/wanted, availability, public/private toggle)
- 🔍 Browse users by skill
- 🔄 Send/accept/cancel skill swap requests
- ⭐ Feedback/rating after swaps
- 🛡️ Admin panel to moderate skills and ban users

---

## 📂 Project Structure

skillswap/
├── backend/ # Django backend
├── frontend/ # Optional frontend (if using React separately)
├── README.md
└── .gitignore


## 📦 Installation (Backend)

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
