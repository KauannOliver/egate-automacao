# **e-Gate Automation System**

This project automates the transfer of document data from Excel spreadsheets to the e-Gate system, using Selenium to fill web forms. It eliminates manual data entry, ensuring faster and more accurate processing, while offering a user-friendly interface for seamless operation.

---

## **KEY FEATURES**

### 1. **Automated Authentication**
   - Automatically logs into the e-Gate portal using predefined credentials.
   - Ensures secure and precise access through Selenium WebDriver.

### 2. **Data Transfer from Excel to e-Gate**
   - Reads document data from an Excel sheet and populates corresponding fields in e-Gate’s web forms.
   - Supports entries such as document number, issue date, amount, and due date, submitted row-by-row.

### 3. **Removal of Read-Only Fields**
   - Removes the "readonly" attribute from e-Gate form fields, enabling automated data entry into otherwise non-editable fields.

### 4. **Graphical Interface with Tkinter**
   - Provides a simple and intuitive interface for users to select files, set row ranges for submission, and view results.
   - Designed for non-technical users to interact with the system easily.

### 5. **Excel File Selection**
   - Allows users to choose an Excel file (.xlsx format) as the data source.
   - Ensures compatibility and seamless integration with the automation process.

### 6. **Results Display**
   - Displays detailed logs of each operation, showing successful submissions and errors, if any, in a user-friendly window.

---

## **TECHNOLOGIES USED**

### 1. **Python**
   - Backbone of the project, enabling back-end processing and automation.

### 2. **Tkinter**
   - Creates the graphical user interface (GUI) for file selection, authentication, and process monitoring.

### 3. **Selenium**
   - Automates web interactions, including login, form completion, and data submission.

### 4. **Pandas**
   - Reads and processes data from Excel sheets, handling large datasets efficiently.

### 5. **Openpyxl**
   - Used for precise reading and manipulation of `.xlsx` files.

### 6. **Chrome WebDriver**
   - Executes the automation in the Chrome browser to ensure compatibility with the e-Gate system.

---

## **HOW IT WORKS**

1. The user launches the application and selects an Excel file containing the document data.
2. The row range to be submitted is specified through the graphical interface.
3. The system logs into the e-Gate portal using Selenium.
4. Document data from the Excel file is transferred into the corresponding form fields in e-Gate and submitted row-by-row.
5. After completion, a log is displayed detailing the success or failure of each row submission.

---

## **CONCLUSION**

The **e-Gate Automation System** provides a streamlined solution for transferring data from Excel to the e-Gate system. By automating repetitive tasks, it reduces manual workload, minimizes data entry errors, and improves operational efficiency. The use of technologies like Selenium, Tkinter, and Pandas ensures a powerful yet easy-to-use tool, making it an ideal solution for businesses seeking process automation.
