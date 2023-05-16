# JNTUK_SGPA_CALCULATOR
This python code reads the excel file "Results1.xlsx" and create a data frame 

Then we initialize FLASK application to get the hallticket number from "page.html" . Then we query the dataframe to filter whole excel sheet 
The filterd data frame is used in further calculation's of results

I have stored that single dataframe in two variables, one for display purpose and other for calculation purpose

Later calculation part calculate sgpa

I have faced a challenge to convert alphabetical grades to numerical grades so I decided to use dictionary to assign an alphabetical key to a numerical value
 
calculaton using JNTUK sgpa formulae
 
Now ,Every thing is set now the only remaining thing is to display the   table and for this purpose I have used to_ html() function to convert dataframe into a html formate and used Django tags in page.html to present the output in html page

Simply I have used conversation tools to convert pdf to excel formate

After extracting the zip file just put your college's results excel file and rename it jn ghe code

now just run the python file on your favorite editor to get flask default URL "http://127.0.0.1:5000" Copy this url when you run the flask application and paste it on your web browser 