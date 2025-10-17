# 🕸️ Web Scraping Projects with BeautifulSoup

A collection of Python scripts demonstrating web scraping and data extraction using **BeautifulSoup**, **Requests**, and **Regular Expressions**.  
Each script focuses on scraping different types of data — from static HTML pages to live websites like TimesJobs and TPointTech.

## 📚 Project Overview
This repository contains multiple mini-projects:

### 1️⃣ **HTML File Scraper**
- Reads a local HTML file (`home.html`)
- Extracts:
  - All `<h1>` header tags
  - Course names, descriptions, and prices from `<div class="course-card">`
- Demonstrates **file handling**, **tag extraction**, and **DOM parsing**

### 2️⃣ **TimesJobs Scraper**
- Scrapes Python-related job postings from [TimesJobs](https://www.timesjobs.com)
- Extracts:
  - Job Title  
  - Company Name  
  - Required Skills  
  - Published Date  
  - “More Info” job link  
- Filters out jobs containing **unfamiliar skills** entered by the user
- Automatically saves each job posting into a `posts/` folder as text files

### 3️⃣ **TPointTech.com Scraper**
- Scrapes tutorial and contact information from [TPointTech.com](https://www.tpointtech.com)
- Extracts:
  - Tutorial names and URLs  
  - Email address, phone number, and address (using regex)
- Demonstrates:
  - URL joining with `urljoin`
  - Regular expression matching for contact info
  - Data structuring in Python dictionaries

## 🧠 Technologies Used

- **Python 3.x**
- **BeautifulSoup4** (`bs4`)
- **Requests**
- **lxml / html.parser**
- **re (Regular Expressions)**
- **File Handling & Data Cleaning**
