# Squirrel Data Analysis with Pandas

This project analyzes the Central Park Squirrel Census dataset using the Pandas library. The program reads a CSV file, counts the number of squirrels based on their primary fur color, and exports the summarized results into a new CSV file.

---

## Project Overview

The program performs the following tasks:

- Reads the squirrel dataset from a CSV file.
- Counts the number of squirrels with:
  - Gray fur
  - Cinnamon fur
  - Black fur
- Displays the counts in the console.
- Creates a new DataFrame containing the summarized data.
- Exports the summary to a new CSV file.

---

## Technologies Used

- Python 3
- Pandas
- 
---

## Dataset

The project uses the **Central Park Squirrel Census** dataset, which contains observations of squirrels, including their primary fur color and other attributes.

Relevant column used:

| Column |
|--------|
| Primary Fur Color |

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/yourusername/Squirrel_Data_Analysis.git
```

2. Navigate to the project directory.

```bash
cd Squirrel_Data_Analysis
```

3. Install Pandas (if not already installed).

```bash
pip install pandas
```

4. Run the program.

```bash
python main.py
```

---

## Sample Output

```
Gray Squirrels: 2473
Cinnamon Squirrels: 392
Black Squirrels: 1034
```

A new file named `squirrel_count.csv` is generated containing the summarized data.

---

## Output Format

| Primary Fur Color | Count |
|-------------------|------:|
| Gray | 2473 |
| Cinnamon | 392 |
| Black | 1034 |

---

## Concepts Practiced

- Reading CSV files using Pandas
- Data filtering
- Counting records
- Creating DataFrames
- Exporting data to CSV
- Basic data analysis with Python

---

## Future Improvements

- Count all unique fur colors dynamically using `value_counts()`.
- Visualize the distribution using Matplotlib or Seaborn.
- Analyze additional squirrel attributes such as age, location, and activity.
- Generate charts and summary reports.

---

## Learning Outcomes

This project demonstrates the fundamentals of data analysis using Pandas, including importing datasets, filtering data, performing basic aggregation, creating new DataFrames, and exporting processed results for further analysis.


