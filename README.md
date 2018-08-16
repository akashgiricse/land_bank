# Village diary


## Current Features

*TODO*
- Data Retrival
- Search Feature
- Create Front end
	- Search with *shreni* number

## Getting started with development
Dependencies:
- Python 3.6.x
- Django 1.11.x
- Ubuntu 17.04 or later or Linux Mint 18.2 or later

### 1. Clone this repository
```bash
git clone https://github.com/akashgiricse/land_bank.git
# in the cloned directory goto land_bank directory i.e.
cd land_bank
```

### 2. Install the [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)
Follow [instructions on official documentation page](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).

### 3. Create the virtualenv
```bash
## run following command from `land_bank` directory
mkvirtualenv land_bank -a "$(pwd)" -p python3.6
```

### 4. Install python packages
```bash
## Activate the virtualenv which you created on the last step (should be automatically activated)
workon land_bank
pip install -r requirements.txt
```

### 5. Setup the database
*TODO - Add instructions for this when I start using MySQL/Postgre database.*

### 6. Run database migrations
```bash
python manage.py migrate
```

### 7. Create superuser
```bash
python manage.py createsuperuser
```

### 8. Run development server
```bash
python manage.py runserver
```
digital ocean 41000
dabase backup
email, one entry .5 mb. sql dump  backup point of view by email 7zip. 1GB, 1CPU, Bengaluru, run db server on same machine enginx front end facing, let's encrypt. 1 month renew, SendGrid 100 emails per day. Drop box for images. Google cloud storage. 300 doller per year. Bucket , s3 12 month free. 