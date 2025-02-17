# Logo Generator for Google Play Apps

## Dataset and Scraping
Imported a kaggle dataset with the names of google play apps. I used the google play scraper to scrape app logos from the name, and wrote a script to parse 
the returned data into a structured json of the format: 
```
{
  "title": app_title
  "logo": logo_link
}
```
I created another script to parse my output json, creating a app_data folder with app_{num}.txt, app_{num}.png to match the format of simpletuner training. 

## Fine Tuning
Fine tuned a Flux1.Dev model trained on over 10,000 google play store app logos. The model and its weights can be found on hugging face at
https://huggingface.co/brianling16/logo-lora. I trained the model for 1 epoch of 2600 steps, with validation images being generated every 100 steps to monitor
model progress. 

Downloading the images and training took around 20 hours total on my macbook. 

## Application
Takes around 2 minutes for each image to generate, (cut out in the demo for time reasons). Frontend was done in react and backend was done through flask. To run the
application, run npm install and npm run to start the frontend, and python3 app.py to start the backend. 

You can see the working demo of the app, there is a file in the github repo. The full training repo can also be found under my profile if you want to see the code. 
