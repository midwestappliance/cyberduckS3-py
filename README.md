# MAP Cyberduck S3 

This is a script used to uplaod files to DigitalOcean S3 bucket or any amazon s3 compatible bucket. <br/><br/>


## Getting started
To run this script, 
1. You must first install [Cyberduck CLI](https://docs.duck.sh/cli/) 
2. Install python on your machine and run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` to install `python-dotenv`
3. Rename the `.env.template` file to simply `.env` and fill in the values as appropriate.
    - `USERNAME` Your Digitalocean spaces `public_key`
    - `PASSWORD` Your Digitalocean spaces `secret_key`
    - `SPACE_NAME` Your Digitalocean space name
    - `EXTENSIONS` The file extensions you intend to upload to S3. E.g. [txt, csv, xls, xlsx]
    - `BASE_URL` The base url of your s3 provider which includes the space name.

__NB: You can choose to not put the environment variables in .env and rather put them in your system wide environment variables for SECURITY PURPOSES (recommended)__

4. Put all the files you intend to upload in the `/output` folder.
5. On your terminal, `cd` into the current directory and run `python3 cyberducks3.py`

Make modifications in the script as neccessory to fit your usecase.

You can use Task Scheduler or Winautomation or any scheduling software to automatically run this script at regular intervals to automate your file upload process. 

Enjoy !


Author: 
Kinason kinason42@gmail.com 

