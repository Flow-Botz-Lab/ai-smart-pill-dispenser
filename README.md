# AI Smart Pill Dispenser (Cloud-Managed IoT System)

## Project Overview

The AI Smart Pill Dispenser is a secure, child-proof, cloud-managed medication system designed to:

- Remind users when it is time to take medication
- Dispense medication only during scheduled time windows
- Authenticate the authorized user before dispensing
- Log all medication activity (Taken / Missed / Late)
- Upload logs securely to a cloud database
- Use AI to predict missed doses and improve reminders

This project demonstrates the integration of embedded systems, cloud infrastructure, and artificial intelligence in a healthcare-focused IoT device.

---

## Problem Statement

Medication non-adherence can lead to severe health risks.  
Traditional pill organizers lack:

- Security
- User authentication
- Controlled dispensing
- Cloud tracking
- Predictive intelligence

Our system addresses these limitations with secure hardware design and cloud-managed logging.

---

## System Architecture

Raspberry Pi Device (Edge Layer)  
↓  
Secure HTTPS Communication  
↓  
Cloud API (FastAPI on Render)  
↓  
Cloud Database (Supabase PostgreSQL)  
↓  
Remote Monitoring Dashboard  

---

## Core Features

### Local Device Features
- Scheduled medication reminders
- Time-restricted dispensing window
- PIN-based authentication
- Child-proof locking design
- Local activity logging

### Cloud Features
- Secure API endpoint
- Centralized medication logs
- Remote monitoring capability
- Scalable database storage
- AI data aggregation

---

## Security Design

To ensure child-proof and secure operation:

- Locked medication housing
- Dispensing only within scheduled time window
- PIN-based user authentication
- Lockout after failed attempts
- HTTPS encrypted communication
- API key authentication between device and cloud

---

## AI Component

A supervised learning model predicts the probability of a missed dose based on:

- Time of day
- Day of week
- Previous missed doses
- User response time patterns

If risk exceeds a threshold, the system escalates reminders.

---

## Development Workflow

This project follows a professional software engineering process:

1. Development in VS Code
2. Version control with Git
3. Repository hosted on GitHub
4. Feature branching for team collaboration
5. Deployment of cloud backend on Render
6. Cloud database hosted on Supabase
7. Raspberry Pi clones repository for device execution

---

## Project Structure

ai-smart-pill-dispenser/
│
├── README.md
├── requirements.txt
├── src/                     # Device-side code
│   ├── main.py
│   ├── scheduler.py
│   ├── auth.py
│   ├── dispenser.py
│   ├── logger.py
│   └── ai_model.py
│
├── backend/                 # Cloud API
│   ├── main.py
│   └── requirements.txt
│
└── data/
    └── medication_log.csv

---

## Technologies Used

- Python
- Raspberry Pi 5
- GPIO
- FastAPI
- Supabase (PostgreSQL)
- Render (Cloud Hosting)
- scikit-learn
- Git & GitHub

---

## Deployment Overview

### Cloud Backend Deployment
Hosted on Render using:
- FastAPI application
- Environment variables for API keys
- Secure HTTPS endpoint

### Device Deployment
Raspberry Pi clones the repository:

git clone https://github.com/your-repo-link.git
cd ai-smart-pill-dispenser
python src/main.py

---

## Future Improvements

- Facial recognition authentication
- Mobile app integration
- Caregiver SMS alerts
- HIPAA-compliant cloud storage
- Over-the-air firmware updates

---

## Academic Purpose

This project demonstrates:

- Embedded system design
- IoT cloud architecture
- Secure device-to-cloud communication
- AI integration in healthcare systems
- Real-world software development workflow
