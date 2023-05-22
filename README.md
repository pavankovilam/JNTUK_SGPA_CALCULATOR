
# JNTUK SGPA Calculator

This is a Flask application that calculates the SGPA (Semester Grade Point Average) for JNTUK (Jawaharlal Nehru Technological University, Kakinada) students based on their results stored in an Excel file.

## Prerequisites

- Python 3.x
- Flask
- pandas

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/pavankovilam/JNTUK_SGPA_CALCULATOR.git
   ```

2. Install the required dependencies:
   ```shell
   pip install flask pandas
   ```

## Usage

1. Ensure that the Excel file `'Results1.xlsx'` is present in the correct location and contains the necessary student result data. Make sure the file structure matches the expected format.

2. Run the Flask application:
   ```shell
   python app.py
   ```

3. Open your web browser and navigate to `http://localhost:5000`.

4. Enter the Hall Ticket Number (HTNO) of the student for whom you want to calculate the SGPA.

5. Click the "Submit" button.

6. The application will display the student's result, SGPA, and other relevant information.

## File Structure

- `app.py`: The main Flask application file that handles the routing and calculation logic.
- `page.html`: The HTML template file used for rendering the result page.
- `Results1.xlsx`: The Excel file containing the student result data. Ensure it follows the expected format.




## Disclaimer

This application is provided as-is, without any warranty or guarantee of its accuracy or functionality. Please use it responsibly and verify the results if necessary.

## Contact

For any inquiries or feedback, please contact kovi.pavan.kumar@gmail.com
