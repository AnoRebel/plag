# Plagiarize

**A simple concept of web scraping basic data from sites**

### [Demo](https://plagiarize.herokuapp.com): https://plagiarize.herokuapp.com

## Features

* Scrapes allowed images from a given link
* Scrapes allowed videos from a given link
* Scrapes available metadata from a given link

Made with:

 - Flask
 - Tailwind CSS

To run this;
 
  - Clone the repo
  
	`git clone https://github.com/anorebel/plag.git`
 
  - Enter the directory
  
	  `cd plag`
 
  - Create environment and install dependencies
  
	  `pipenv install`

  - Initialize database and run:
 	- In development:
	 	```bash
	 	 export FLASK_ENV=development
	 	 export FLASK_APP=app
	 	 flask run
	 	```
	 	
	 - In production:
	 	```bash
	 	 export FLASK_APP=app
	 	 flask run
	 	```
