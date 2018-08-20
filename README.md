# Village diary


## Current Features

*TODO*

- [x] Only one image is needed
- [x] Proper spelling use should be done.
- [x] Image size  14 GB for 1 img per plot and 28 gb for 2 img per plot (so decide plan for hosting)
- [ ] PDF generation of the query(Vishal)
- [ ] Print out facility for every query(Vishal)
- [ ] Modify shreni names (Giri)
	- [ ] There are two shreni 5,6
	- [ ] These two shrenies have sub shrenies
- [x] 9000-10000 rows will be there in database.
- [ ] Capitalize name of village before saving to database. (Vishal)
- [ ] Add plugin for history. (Giri)
- [ ] Automatic imagee compression(size of image<500). (Vishal)
- [ ] Get full detail of Digital Ocean pricing. (Shukla)

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
