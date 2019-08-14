from googlesearch import search
from bs4 import BeautifulSoup
import requests
import xlwt
import boto3
from botocore.exceptions import NoCredentialsError
from xlwt import Workbook


# Retrieves urls for sites relevant to invention
def getSiteNames():
    # Creates array for storage of urls
    sites = []

    # File location of list of descriptors, is a local file as of now,
    # change this if you wish to run the code
    input_location = 'C:/Users/dselt/autoInfringe/descriptors.txt'

    # Creates txt file that will contain relevant urls
    f = open("sites.txt", 'w')

    # Opens file that contains descriptors of invention
    # Each line of text represents one descriptor
    descriptors = open(input_location, 'r')

    # Searches google with descriptors as search term
    # Results are added to list of urls
    # Starred terms are more important, search results from starred terms
    # are added with star at the front of url
    for line in descriptors:
        for url in search(line, stop=20):
            if line[0] == '*':
                sites.append('*' + url)
            else:
                sites.append(url)

    # If a url only appears once, and is not the result of a key term, it
    # is removed to prevent unnecessary search
    x = 0
    while x < len(sites):
        if sites[x][0] != '*' and sites.count(sites[x]) <= 1:
            sites.remove(sites[x])
        else:
            x += 1
    x = 0

    # Duplicate urls are removed from list
    # Stars are removed from key urls
    while x < len(sites):
        if sites.count(sites[x]) > 1:
            sites.remove(sites[x])
        elif sites[x][0] == '*':
            sites[x] = sites[x][1:]
        else:
            x += 1

    # Urls from list are written to a text file
    for x in sites:
        f.write(x + '\n')
    f.close()


def getSiteInfo():
        # Workbook is created
        wb = Workbook()

        # add_sheet is used to create sheet.
        sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)
        # Limit of characters allowed in a string is established
        STRING_LIMIT = 32767

        # Text file containing urls is opened
        f = open("sites.txt", 'r')

        # Row is kept track of
        row = 0

        # For each url, the html is retrieved and formatted
        for line in f:
            sheet1.write(row, 0, line)
            source = requests.get(line).text
            soup = BeautifulSoup(source, 'lxml')
            soup.prettify()

            # If website has a title, it is written to the excel file
            try:
                sheet1.write(row, 1, soup.title.text)
            except:
                pass
            txt = ''

            # Column for information is kept track of
            col = 2

            # Text within 'p' tags is retrieved, and written to excel file
            # If the text exceeds the character limit for a string, the first portion of
            # the text is written to the excel file, and string is reset to next portion of
            # text.
            for i in soup.find_all('p'):
                if len(txt + i.text) > STRING_LIMIT:
                    sheet1.write(row, col, txt)
                    txt = i.text
                    col += 1
                else:
                    txt += i.text
            sheet1.write(row, col, txt)
            row += 1
        f.close()

        # Location to where excel file is saved, is local as of now
        # File is excel as of now for debugging purposes, change address
        # if you wish to run
        output_location = 'C:/Users/dselt/autoInfringe/site data.xls'

        # Excel file is saved
        wb.save(output_location)


def uploadFile():
    ACCESS_ID = 'Enter ID Here'
    ACCESS_KEY = 'Enter Key Here'
    # Create an S3 client
    s3 = boto3.resource('s3',
                        aws_access_key_id=ACCESS_ID,
                        aws_secret_access_key= ACCESS_KEY)

    filename = 'C:/Users/dselt/autoInfringe/site data.xls'
    bucket_name = 'infringement'

    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.
    s3.meta.client.upload_file(filename, bucket_name, 'site data.csv')


def analyze():
    ACCESS_ID = 'Enter ID Here'
    ACCESS_KEY = 'Enter Key Here'
    input_s3_url = 's3://infringement/'
    input_doc_format = 'ONE_DOC_PER_LINE'
    output_s3_url = 's3://infringementanalyze/'
    data_access_role_arn = 'arn:aws:iam::428946227188:role/service-role/AmazonComprehendServiceRole-topicmodel'
    number_of_topics = 10  # Optional argument

    # Set up job configuration
    input_data_config = {'S3Uri': input_s3_url, 'InputFormat': input_doc_format}
    output_data_config = {'S3Uri': output_s3_url}

    # Begin a job to detect the topics in the document collection
    comprehend = boto3.client('comprehend',
                              region_name = 'us-east-1',
                              aws_access_key_id=ACCESS_ID,
                              aws_secret_access_key=ACCESS_KEY)
    start_result = comprehend.start_topics_detection_job(
        InputDataConfig=input_data_config,
        OutputDataConfig=output_data_config,
        DataAccessRoleArn=data_access_role_arn,
        NumberOfTopics=number_of_topics)
    job_id = start_result['JobId']
    print(f'Started Topic Detection Job: {job_id}')

    # Retrieve information about the job
    describe_result = comprehend.describe_topics_detection_job(JobId=job_id)
    job_status = describe_result['TopicsDetectionJobProperties']['JobStatus']
    print(f'Job Status: {job_status}')
    if job_status == 'FAILED':
        print(f'Reason: {describe_result["TopicsDetectionJobProperties"]["Message"]}')

    # List all topic-detection jobs
    list_result = comprehend.list_topics_detection_jobs()
    for job in list_result['TopicsDetectionJobPropertiesList']:
        print(f'Job ID: {job["JobId"]}, Status: {job["JobStatus"]}')


getSiteNames()
getSiteInfo()
uploadFile()
analyze()

