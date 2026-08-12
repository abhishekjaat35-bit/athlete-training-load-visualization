# 📊 Athlete Training Load Visualization

A Python sports-data analytics project that calculates athlete training load and converts the results into visual performance reports using **Pandas** and **Matplotlib**.

The project is designed to demonstrate how raw training-session data can be transformed into useful visual information for sports performance analysis.

---

## 🎯 Project Objective

The program analyzes training sessions and produces visualizations for:

- Athlete total training load
- Daily team training load
- Training load by session type
- Training-session volume
- Athlete workload comparison

---

## 📊 Data Flow

```text
Training Session CSV
        ↓
      Pandas
        ↓
Calculate Training Load
        ↓
Group & Summarize Data
        ↓
Matplotlib
        ↓
Create Visualizations
        ↓
Sports Performance Report
```

---

## 🧮 Training Load Calculation

The project uses a simple session-RPE approach:

```text
Training Load = Duration × sRPE
```

Example:

```text
Duration = 75 minutes
sRPE = 7

Training Load = 75 × 7
               = 525 AU
```

Where:

```text
AU = Arbitrary Units
```

---

## 📁 Project Structure

```text
athlete-training-load-visualization/
│
├── training_load_visualization.py
├── training_data.csv
├── athlete_total_training_load.png
├── daily_training_load.png
├── session_type_training_load.png
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🗂️ Dataset

The project uses a synthetic training dataset.

### Dataset variables

| Variable | Description |
|---|---|
| Athlete | Athlete identifier |
| Date | Training date |
| Session_Type | Type of training session |
| Duration_min | Session duration in minutes |
| sRPE | Session rating of perceived exertion |

Example:

```csv
Athlete,Date,Session_Type,Duration_min,sRPE
Rahul,2026-08-03,Strength,75,7
Rahul,2026-08-04,Speed,60,8
Rahul,2026-08-05,Recovery,45,3
```

The dataset contains synthetic data for programming and analytics practice.

---

## 🐍 Technologies Used

- Python
- Pandas
- Matplotlib
- CSV
- DataFrames
- GroupBy analysis
- Data visualization

---

## ⚙️ Installation

Install the required Python libraries:

```bash
pip install pandas matplotlib
```

Verify the installation:

```bash
python -c "import pandas; import matplotlib; print('Libraries installed successfully')"
```

---

## ▶️ How to Run

Open your terminal inside the project folder.

Run:

```bash
python training_load_visualization.py
```

The program will analyze the CSV dataset and generate three charts.

---

## 📈 Visualizations

### 1. Athlete Total Training Load

File:

```text
athlete_total_training_load.png
```

Shows the total accumulated training load for each athlete.

Expected ranking:

```text
Vikram → 2635 AU
Rahul  → 2260 AU
Arjun  → 1980 AU
```

---

### 2. Daily Team Training Load

File:

```text
daily_training_load.png
```

Shows how the team's total training load changes across training days.

Expected values:

```text
2026-08-03 → 1585 AU
2026-08-04 → 1405 AU
2026-08-05 →  345 AU
2026-08-06 → 1615 AU
2026-08-07 → 1925 AU
```

---

### 3. Training Load by Session Type

File:

```text
session_type_training_load.png
```

Shows the total training load contributed by different session types.

Expected results:

```text
Strength      → 3510 AU
Conditioning  → 1615 AU
Speed         → 1405 AU
Recovery      →  345 AU
```

---

## 📊 Expected Analysis

Using the supplied synthetic dataset:

| Metric | Result |
|---|---:|
| Total sessions | 15 |
| Athletes | 3 |
| Total training load | 6,875 AU |
| Highest athlete load | 2,635 AU |
| Highest daily load | 1,925 AU |
| Highest session-type load | Strength — 3,510 AU |

---

## 🔬 Sports Science Application

Training-load visualization can help coaches and sport scientists communicate workload patterns more effectively.

Potential applications include:

- Athlete monitoring
- Strength and conditioning
- Conditioning analysis
- Training-session comparison
- Team workload monitoring
- Periodization monitoring
- Performance dashboards
- Training-load reporting

---

## ⚠️ Scientific Limitation

The session-RPE method is a simple internal-load monitoring approach.

The calculated training load should **not** be interpreted as a direct measurement of physiological stress, fatigue, or injury risk.

This project does not currently include:

- Heart-rate data
- GPS distance
- High-speed running
- Accelerations and decelerations
- Player-load metrics
- Wellness scores
- Recovery status
- Neuromuscular testing
- Individual physiological thresholds

Therefore, this project is intended primarily for **educational programming and sports-data analytics practice**.

---

## 🚀 Future Improvements

Planned improvements include:

- [ ] Add weekly workload analysis
- [ ] Add rolling averages
- [ ] Add workload trends
- [ ] Add heart-rate data
- [ ] Add GPS data
- [ ] Add wellness data
- [ ] Add readiness scores
- [ ] Add automated reports
- [ ] Add interactive dashboards
- [ ] Add athlete comparison tools
- [ ] Add advanced statistical analysis
- [ ] Build an automated athlete-monitoring system

---

## 🧠 Skills Demonstrated

```text
Python
   ↓
CSV Data
   ↓
Pandas
   ↓
Data Transformation
   ↓
GroupBy Analysis
   ↓
Training Load Calculation
   ↓
Matplotlib
   ↓
Data Visualization
   ↓
Sports Analytics
```

---

## 👨‍💻 Author

**Abhishek Tomar**

Strength & Conditioning | Sports Performance | Sports Analytics | Python

---

## 📜 License

This project is licensed under the MIT License.

---

## 📌 Project Status

**Completed ✅**
