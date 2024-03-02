# DSC Rongo uchaguzi online project


# Overview
This is a website created to conduct annual elections in Google Developers Students Club (GDSC) Rongo University.

## Tech stack
Python team will be developing the website by utilizing the following technologies
- HTML
- CSS
- Javascript
- htmx
- Django

## Developer instructions
Installation guide to run the project remotely.
```(bash)
  $ cd Desktop - or your desired location, e.g. Documents, Downloads, etc.
  $ git clone https://github.com/DSCRongo/dsc_uchaguzi_online.git
  $ python3 -m venv .dsc-uchaguzi-venv
  $ source .dsc-uchaguzi-venv/bin/activate
  $ pip install -r requirements.txt
  $ python manage.py runserver
```

The project will require a SECRET_KEY value. To create one, you can use the command shown below:

```(bash)

  $ python -c "import secrets; print(secrets.token_hex(32))"

```

Copy the value printed on your terminal, and create a `.env` file in src folder. Type the following variable in the .env file
```(env)
  SECRET_KEY=<your-generated-secret-key>
```

## Contributor expectations
Contribution guidelines for fixing bugs or assist in project development.

1. Create a new git branch using command
    ```(bash)
    
     $ git checkout -b <name-of-your-branch
    
     ```
    **NOTE:** To avoid merging conflicts, please check that the name of your branch does not exist in this GitHub repo. For example, if you wish to create a branch named `feature` confirm that the name of the branch does not exist.
2. For the changes you make, you can push to your branch. For example, if I have created branch `feature`, I will push my changes to GitHub using the command
   
   ```(bash)
   
   $ git push -u origin <name-of-your-branch>
   
   ```
   
   In this case the `<name-of-your-branch>` will be `feature`.
   
3. Your changes will be pushed to GitHub. You can create a pull request after pushing your code and changes.

## Conclusion
Don't forget to star the repo 🌟😉
