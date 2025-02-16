


### 1. [Live Cryptocurrency Data Analysis]

## Overview

This project is designed to fetch live cryptocurrency data for the top 50 cryptocurrencies by market capitalization, perform data analysis, and present the results in a live-updating Excel sheet. Additionally, a detailed Word report is generated automatically, summarizing key insights and analysis.

## Features

- **Live Data Fetching**\
  Retrieves real-time data from the CoinGecko API for the top 50 cryptocurrencies.

- **Data Analysis**

  - Identifies the top 5 cryptocurrencies by market capitalization.
  - Calculates the average current price of the top 50 cryptocurrencies.
  - Determines the highest and lowest 24-hour percentage price changes.

- **Live-Updating Excel Workbook**\
  The script updates an Excel workbook with two sheets:

  - **Crypto Data:** Contains the raw live data.
  - **Update Info:** Displays the timestamp of the last update and the next scheduled update.

- **Detailed Word Report**\
  A comprehensive analysis report in Word format is generated and updated automatically. It includes:

  - Title Page & Executive Summary
  - Methodology
  - Data Overview
  - Detailed Findings (including a table for the top 5 cryptocurrencies, average price, and 24-hour change analysis)
  - Visualizations (e.g., a bar chart for the top 5 cryptocurrencies)
  - Additional Observations
  - Conclusion and Recommendations

- **Scheduling & Logging**

  - The script uses the `schedule` module to update the data every 5 minutes.
  - Python's `logging` module is used to log key events and errors.

## Requirements

- Python 3.6+
- Required packages:
  - `requests`
  - `pandas`
  - `openpyxl`
  - `schedule`
  - `matplotlib`
  - `python-docx`

To install the required packages, run:

```bash
pip install requests pandas openpyxl schedule matplotlib python-docx
```

## Setup & Installation

1. Clone or download the repository.
2. Update the `dropbox_folder` variable in the script (`crypto_tracker.py`) with the correct path to your Dropbox folder.
3. (Optional) Create and activate a virtual environment, then install the required packages.

## Usage

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the script:

   ```bash
   python crypto_tracker.py
   ```

3. The script will:

   - Fetch live cryptocurrency data from the CoinGecko API.
   - Analyze the data.
   - Update an Excel workbook (`Live_Crypto_Data.xlsx`) with live data and update info.
   - Generate a detailed Word report (`Crypto_Analysis_Report.docx`) with insights, visualizations, and recommendations.

4. The script is scheduled to run every 5 minutes. To stop it, press `Ctrl+C`.

## Files Included

- **crypto\_tracker.py**\
  The main Python script that fetches, analyzes, and updates data, and generates both the Excel workbook and the Word report.

- **Live\_Crypto\_Data.xlsx**\
  The Excel workbook (automatically saved in your Dropbox folder) containing the live cryptocurrency data and update information.

- **Crypto\_Analysis\_Report.docx**\
  The detailed Word report (automatically saved in your Dropbox folder) that provides an in-depth analysis of the live data.

## Additional Information

### Live Updates:

- The system continuously updates every 5 minutes. Ensure that your machine is on and the script is running to keep the data current.

### Dropbox Integration:

- The Excel and Word files are saved in your Dropbox folder, making it easy to share a live link with your assessor.

## Contact

If you have any questions or need further assistance, please feel free to contact:

[Anas Sheikh]

Email: [[anassheikh926@gmaul.com](mailto\:anassheikh926@gmaul.com)]
note: There is a sample more detailed code of a Web_scrapper in script scrapper_API.py  

