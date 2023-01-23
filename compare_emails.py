import pandas as pd


def compare_emails(file_path, column1, column2):
    # read excel file and store it in a dataframe
    df = pd.read_excel(file_path)
    
    # convert all emails in column1 to lowercase and remove any whitespaces
    email_newsletter_list = df[column1].dropna().str.lower().str.strip()
    print('Number of emails in email_newsletter_list: {}'.format(len(email_newsletter_list)))
    # convert all emails in column2 to lowercase and remove any whitespaces
    store_customers = df[column2].dropna().str.lower().str.strip()
    print('Number of emails in store_customers: {}'.format(len(store_customers)))
    # find matched emails between column1 and column2
    matched_emails = email_newsletter_list[email_newsletter_list.isin(store_customers)]
    print('Number of matched emails: {}'.format(len(matched_emails)))
    # calculate the percentage of matched emails
    percentage = (len(matched_emails)/len(email_newsletter_list))*100
    print('Percentage of matched emails: {}%'.format(percentage))
    # return the percentage of matched emails
    return percentage

# Example usage
file_path = 'emails.xlsx'
column1 = 'Emails1'
column2 = 'Emails2'

percentage = compare_emails(file_path, column1, column2)
print(percentage)
