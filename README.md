# 🏏 Cricket Live Alerts

A Python-based desktop application that displays live cricket match scores as popup alerts using web scraping techniques.

## 📌 Project Overview
Cricket Live Alerts helps users stay updated with ongoing cricket matches without constantly refreshing websites.

This project fetches live cricket data from Cricinfo RSS feeds and displays:
- Live match details
- Team names
- Match scores
- Match location
- Match time

A GUI popup automatically shows updated score alerts every 20 seconds.

---

## 🚀 Features
- Fetches live cricket scores
- Displays available live matches
- User selects desired match
- Desktop popup alerts with latest score
- Auto-refresh every 20 seconds
- Error handling for invalid inputs and network failures

---

## 🛠️ Tech Stack
- **Language:** Python
- **Modules Used:**
  - requests
  - bs4 (BeautifulSoup)
  - tkinter
  - time
  - sys

---

## 📂 Project Structure
```bash
Cricket-Live-Alerts/
│
├── cricket_live_alerts.py
├── README.md
└── requirements.txt
```

---

## 📦 Installation

### 1. Clone repository
```bash
git clone https://github.com/yourusername/Cricket-Live-Alerts.git
cd Cricket-Live-Alerts
```

### 2. Install dependencies
```bash
pip install requests beautifulsoup4 lxml
```

### 3. Run project
```bash
python cricket_live_alerts.py
```

---

## ▶️ How It Works
1. Fetches live matches from Cricinfo RSS feed
2. Displays list of current live matches
3. User selects match number
4. Opens GUI popup showing live score
5. Updates score automatically every 20 seconds

---

## 📸 Output
- Live cricket match list in terminal
- Desktop popup alerts with scores

---

## 🎯 Learning Outcomes
Through this project, we learned:
- Web scraping using BeautifulSoup
- Working with XML data
- GUI creation with Tkinter
- Exception handling
- API/data fetching using Requests

---

## 👨‍💻 Team Members
- Dheerj Pulime
- Ganesh Sesha Sai Akhil


---

## 📚 References
- Cricinfo RSS Feed
- Python Documentation
- BeautifulSoup Documentation

---

## ⭐ Future Improvements
- Add score notifications in system tray
- Add match filtering by teams
- Mobile notifications integration
- Better GUI dashboard

---

## License
This project is for academic and learning purposes.
