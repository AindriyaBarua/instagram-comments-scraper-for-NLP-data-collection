# instagram-comments-scraper
Scrap Instagram comments under a post with python and Selenium
**What the project does:**
This project:
1. Reads a list of Instagram post links from an Excel file placed inside Input folder
2. Scraps comments from all the files
3. Writes the links and corresponding comments into another Excel file inside Output folder

**How to Run:**
1. Clone the project
2. Create an Excel file with the links you want to scrap and place it in the Input folder
3. The constants.py file holds all the constants, edit the INPUT_FILENAME and OUTPUT_FILENAME with your filenames
4. In your venv ternminal, run 
  >pip install -r requirements.txt
6. Run
  >python driver.py
  

