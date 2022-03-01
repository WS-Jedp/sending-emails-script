# SEND EMAILS TO ENDPOINT UTILITY 📧

Small Python script to use when you need to send emails to some endpoint

## How it works?
To use correctly this script you may want to follow the next steps:  

- The first that you may want to do is install all the Python needed dependencies with the command:  
    - `pip install` - All the needed dependencies are in the requirements.txt file  

- Once all the dependencies are installed you can modify the enviroment variables to let know the script how to get the data and how to send it into the specified endpoint, the environment variables are:

    - `CSV_FILE`                  - Specifies the path to the csv file to get the emails
    - `CSV_EMAIL_FIELD`           - Specify which is the field of the CSV to get the emails
    - `ENPOINT_URL`               - Specify the endpoint to the script will make the post request to send the emails
    - `PAYLOAD_EMAILS_FIELD`      - Indicates which is the field of the body payload in which the emails should be in 
    - `RESPONSE_FILE`             - Specify the name of the file where the response of the request it will be saved
    - `PAYLOAD_OPTIONAL_FIELDS`   - (Optional) Receive a JSON string with the other fields that may require the endpoint
    - `AVOID_EMAILS`              - (Optional) Indicates all the emails that should be ignore when the script is getting the emails from the CSV

- Once you had configured all the needed environment variables you will need to execute the Python code with the next command:
    - `python3 index.py`

That's all! 🚀
