# Casualty Information Extraction
Casualty information extraction project uses the news from the link extracted using RSS feed. The news are scraped and from the text, and using that text various information such as death number, injury number, vehicles types are extracted.

## Build Instruction 
```
cd DeathExtraction
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
