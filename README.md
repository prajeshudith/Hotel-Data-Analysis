# **Project Setup and Execution Guide**

## **Environment Setup**

1. **Create a Virtual Environment**  
   Run the following command to create a virtual environment:  
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**  
   Activate the environment using the appropriate command for your operating system:  
   - On Windows:  
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:  
     ```bash
     source venv/bin/activate
     ```

3. **Install Required Packages**  
   Install all necessary dependencies by running:  
   ```bash
   pip install -r requirements.txt
   ```

---

## **Notebook Execution**

1. Open the provided Jupyter Notebook file `data_analytics.ipynb` in your preferred IDE or Jupyter environment.
2. Click on `Select Kernal` and choose `python environment -> venv`
3. Click on `Run All` to execute all cells sequentially.  
   This will process the datasets, perform analyses, and generate visualizations.

---

## **Output and Insights**

- The outputs of each cell are displayed directly within the notebook upon execution.
- Detailed interpretations and business insights derived from the analyses are documented in the `Interpretations_&_Insights.pdf` file for your reference.

---

### **Notes**

- Ensure all required datasets are available in the same directory as the notebook before execution.
    
    * Data Analyst Intern Assignment - Excel.xlsx
    * requirements.txt
    * data_analytics.ipynb
- If any issues occur during package installation or execution, verify the Python version and ensure compatibility with the dependencies listed in `requirements.txt`.

---
