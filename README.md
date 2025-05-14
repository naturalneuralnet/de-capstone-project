# Data Engineering Capstone Project 

This is my capstone for the Data Engineering course. It is an example of my technical skills in pandas, python and streamlit and a demonstration of my understanding and ability to work with and manipulate data into an extract, load and transform pipeline. 

## Project Details and User Stories

I chose a UFO sighting dataset as I've always been intrigued by reports. The dataset can be found on Kaggle [here](https://www.kaggle.com/datasets/NUFORC/ufo-sightings)

This dataset was scraped, geolocated, and time standardized from NUFORC data by Sigmond Axel [here](https://github.com/planetsig/ufo-reports).

### User Stories

- [x] I want to load the data from the source so I can clean, transform and visualise it to generate insights.
- [x] I want to clean the data by removing nulls, standardising formats and dropping unnecessary columns using pandas so I can have a clean dataset to work with.
- [x] I want to enrich the dataset by transforming the data into new information using aggregation, summarisation and feature generation so I can have an interesting dataset to generate insights from. 
- [x] I want to load the enriched dataset into streamlit so I can create filters and visualisations such as bar charts and scatter plots in order to discover insights to share.
- [x] I want to write unit tests for major functions that load, clean and transform the data so I can ensure my code is functional and consistent.


## Local Setup and Usage

- Clone or download the project from this Github.
- Create and activate a Python virtual environment.
- Install project dependencies from the requirements.txt.
- To deploy the streamlit project locally use the 'streamlit run app/main.py' command.
- To run the tests use 'pytest app/tests/test-main.py' command inside the app folder.


## Analytical Questions

After exploring the dataset I discovered some interesting questions that insights from transforming and aggregating the data might be able to answer.

- Where are UFO sightings most common?
- Is there a trend in number of sightings over the years?
- How often are sightings flagged as hoaxes?
- What months of the year are sightings most likely?
- How are sightings most often described?
- What hour of the day are sightings most likely to happen?

## Summary of Findings

The project produced the following insights:

- UFO sightings are most commonly reported in the United States. California is the most popular state for sightings but the most popular city is Seattle, in Washington.
- Outside of the US the majority of reported sightings are in Canada. This suggests that proximity to the US is a factor of seeing UFOs.
- The number of reports increases significantly after 2000, perhaps TV Shows like The X-Files had an influence?
- Sightings in this dataset are very rarely flagged as hoaxes, possibly because the data collector wants to collect UFO sightings. 
- Sightings are much higher during the summer, this maybe because the days are longer or because aliens enjoy a cruise on a summer evening.
- In the US, sightings are most often described as lights in the sky as opposed to saucers, the next likeliest description is also surprising: triangle!
- Sightings are most likely to occur at 9pm in the evening. 


## Proposed Improvements

### Create more features

- Create a colour feature so I can analyse the colour of the UFOs.
- Create a distance from Area 51 feature so I can analyse wether distance affects the number of sightings.

### Get more data
- This dataset is limited to sightings from 1910 to 2013, so there is no recent data.
- This dataset is further limited by the regions the reports are collated from, primarily North America. In the future I would like to analyse a more region diverse dataset.
  
## Additional Considerations

#### How would you go about optimising query execution and performance if the dataset continues to increase?

I did not use a database during this project but in order to optimise query execution and performance for an increasing dataset I would utilise:

- Indexing in SQL to speed up common queries
- Common Table Expressions to optimise query speed
- Sharding on a cloud provider to improve read and write speeds for very large datasets. 

#### What error handling and logging have you included in your code and how this could be leveraged?

I have not included any error handling or logging in the project so far. In the future I would like to add error handling and try and catch statements to catch exceptions where they may occur and handle them so the application doesn't crash. 

I would add logging to the tests and data processing and visualisation function to give information to the user about the success of those functions.

#### Are there any security or privacy issues that you need to consider and how would you mitigate them?

A security issue to consider is that the dataset was downloaded from the internet. If it was input into an SQL database without thorough checking of all the values it is possible that a SQL Injection attack could occur. Additionally, it would be prudent to hide the authentication credentials for the database using environment variables so that they are not in the public repository and available to the internet.

#### How this project could be deployed or adapted into an automated cloud environment using the AWS services you have covered?

A bash script could be written to store the data and the application on an S3 bucket and it could be run on an EC2 instance with a Redshift database to store the data. An Amazon Glue service could be used to create an ETL pipeline in the cloud, which is then queried by the application running on an EC2 instance. Amazon Managed Workflows for Apache Airflow could be used to create and run a workflow that carries out each step of the process automatically, from provisioning the instances to creating and running the data transformations jobs.