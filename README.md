# e-Gate Automation System

This project was developed to automate the transfer of document data from an Excel spreadsheet directly to the e-Gate system. The solution integrates Selenium automation to complete web forms, eliminating the need for manual data entry and ensuring greater process efficiency.

**KEY FEATURES**

1. **Automated Authentication**  
   The system automatically logs into the e-Gate portal, entering predefined credentials and authenticating system access. Selenium WebDriver ensures precise execution of the automation.

2. **Data Transfer from Excel to e-Gate**  
   The system reads document data from an Excel sheet and automatically populates the corresponding fields in e-Gate’s web form. This includes document number, issue date, amount, and due date, submitted row-by-row based on user selection.

3. **Removal of Read-Only Fields**  
   Before submitting data, the system removes the "readonly" attribute from e-Gate form fields, enabling data entry for fields that would otherwise be non-editable.

4. **Graphical Interface with Tkinter**  
   The graphical interface is built with Tkinter, allowing for user-friendly interaction. Users can select an Excel file, set the row range for submission, authenticate login, and view results directly in the application.

5. **Excel File Selection**  
   The system includes a file selection feature, allowing users to choose the Excel sheet from which data will be extracted. Only .xlsx files are permitted, ensuring compatibility with the automation.

6. **Results Display**  
   After data submission, the system shows a window with a detailed log of operations, including successful submissions for each row and any errors that occurred during the process.

**TECHNOLOGIES USED**

1. **Python**: Main language used for back-end and automation development.
2. **Tkinter**: Library for creating the graphical interface, providing a user-friendly experience.
3. **Selenium**: Used to automate web interactions, such as login, form filling, and button clicks.
4. **Pandas**: Library used for reading and handling data from Excel sheets, ensuring efficient processing.
5. **Openpyxl**: Used for reading Excel files and extracting document data precisely.
6. **Chrome WebDriver**: Automation is conducted via Selenium, utilizing Chrome browser to access the e-Gate system.

**HOW IT WORKS**

1. The user launches the system and selects the Excel sheet containing document data.
2. Through the interface, the user specifies the range of rows to be submitted to e-Gate.
3. The system automatically logs in, accessing the e-Gate portal.
4. Data from Excel is filled into the form fields and submitted to the system.
5. After the process completes, the system displays a log with the results of each submission.

**CONCLUSION**

This project provides a robust solution for automating data transfer from Excel to the e-Gate system, removing manual work and reducing data entry errors. The combination of technologies like Selenium, Pandas, and Tkinter ensures efficient and easy-to-use automation, increasing productivity and accuracy in information submission.
