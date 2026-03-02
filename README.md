# AI Smart Pill Dispenser

## Project Overview

The AI Smart Pill Dispenser is a secure, child-proof medication management system designed to:

- Remind users when it is time to take medication
- Dispense medication only during scheduled time windows
- Authenticate the authorized user before dispensing
- Log all medication activity (Taken / Missed / Late)
- Use AI to predict missed doses and adjust reminders

This project was developed for an academic AI & Robotics presentation.

---

## Problem Statement

Medication non-adherence can lead to serious health risks.
Traditional pill boxes do not provide:
- Security
- Controlled dispensing
- Logging
- Predictive intelligence

---

## Solution

Our system integrates:

- Scheduled reminder system
- Secure authentication (PIN-based access)
- Controlled dispensing mechanism
- Dose logging database
- AI missed-dose prediction model

---

## System Architecture

Hardware Layer  
↓  
Control & Authentication Layer  
↓  
Dispensing Mechanism  
↓  
Logging Database  
↓  
AI Prediction Layer  

---

## Technologies Used

- Python
- Raspberry Pi (GPIO control)
- SQLite / CSV logging
- scikit-learn
- Servo motor
- PIN authentication system

---

## Security Features

- Child-proof locking mechanism
- Time-restricted dispensing window
- PIN-based authentication
- Lockout after failed attempts
- Tamper logging

---

## Future Improvements

- Face recognition authentication
- Mobile application integration
- Caregiver alert system
- Cloud-based logging dashboard
