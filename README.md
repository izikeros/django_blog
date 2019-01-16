# Blog web application

My very first web application implemented using Django. It was created by 
following [djangogirls tutorial](https://tutorial.djangogirls.org/en/).

The final effect looks like this:
![blog](https://tutorial.djangogirls.org/en/images/application.png)

# Installation
Setup virtual virtual env named `blogenv`
```
python3 -m venv blogvenv
```

activate virtualenv and install required packages:
```
pip install -r requirements.txt
```

make migrations, then run the blog locally:
```
manage.py runserver
```

