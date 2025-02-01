# 🎵 Data Modeling with Postgres - Sparkify Project

## 📌 Introduction
### What is Sparkify?
Sparkify is a **music streaming startup** looking to **analyze user activity** and **song preferences** to improve recommendations and business strategy.  
The company collects **log data** on user interactions and song metadata from their app.

### Purpose of This Project
The goal of this project is to:
✅ Design an **optimized Postgres database schema** for **analytics**  
✅ Build an **ETL pipeline** that extracts **JSON log & song data**, transforms it, and loads it into the database  
✅ Enable the Sparkify team to run **SQL queries** to analyze user behavior and song preferences  

---

## 🏗️ Database Schema and ETL Process

### **📊 Database Schema: Star Schema**
We use a **Star Schema** to optimize analytical queries.  
- **Fact Table:**
  - `songplays` (contains song play events)
- **Dimension Tables:**
  - `users` (details about users)
  - `songs` (details about songs)
  - `artists` (details about artists)
  - `time` (timestamps broken into components)

#### **Schema Diagram**
```
          songplays (fact)
        /         |        \
  users          songs     artists
        \         |        /
                time
```

### **🔄 ETL Pipeline**
1. **Process `song_data`**:
   - Extracts song and artist details from JSON files
   - Loads data into **`songs`** and **`artists`** tables
2. **Process `log_data`**:
   - Filters for `NextSong` events
   - Extracts and loads:
     - **Timestamps** into the `time` table
     - **User details** into the `users` table
     - **Song plays** into the `songplays` table (by looking up song/artist ID)

---

## 📂 Files in Repository

```
├── data/
│   ├── song_data/   # JSON files with song metadata
│   ├── log_data/    # JSON files with user activity logs
├── sql_queries.py   # SQL queries for table creation, inserts, and lookups
├── create_tables.py # Script to set up (drop & create) the database tables
├── etl.py           # Main ETL script to extract, transform, and load data
├── test.ipynb       # Jupyter Notebook to validate data insertion
├── README.md        # Project documentation (THIS FILE)
```

---

## 🚀 How to Run the Python Scripts

### **1️⃣ Set Up the Database**
First, create the tables by running:
```bash
python3 create_tables.py
```
✅ **This will drop & recreate all tables in the `sparkifydb` database.**

---

### **2️⃣ Run the ETL Pipeline**
To process all files and load the data into Postgres, run:
```bash
python3 etl.py
```
✅ **This will extract, transform, and load the data into the database.**

---

### **3️⃣ Verify Data Insertion**
Open **test.ipynb** and run the queries to verify the tables contain data.

Example SQL query to check songplays:
```sql
SELECT * FROM songplays LIMIT 5;
```

---

## 🏆 Key Features of This Project
✅ **PostgreSQL database schema optimized for analytics**  
✅ **Python-based ETL pipeline for batch processing JSON data**  
✅ **Star schema design for faster queries**  
✅ **Handles missing data & duplicates gracefully**  
✅ **Uses SQL joins for song-artist lookups in `songplays`**  

---

## 📜 Additional Notes
- This project demonstrates skills in **database modeling, ETL pipelines, SQL, and Python scripting**.
- The ETL script is modular and **scalable** to process large datasets.
- Proper **error handling** ensures smooth data ingestion.

🚀 **Built by [Greg Pina] for Udacity’s Data Engineering Nanodegree!**
