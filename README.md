![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Welcome!

This is my Code Institute README for deploying my third portfolio project, the Python command-line project. 
The last update to this file was: **October 20, 2022**

The aim of the game is to view a map/grid of possible locations for opponent's ships and try and locate the opponent's ships before their computer finds yours.

## Deployment
* My code has been deployed to Heroku at https://battleship-ib.herokuapp.com/

## The rules
- Battleships is a classic game that has been enjoyed for generations.
- I remember playing a version, with my friends and siblings, in a blue plastic case, with red and blue plastic pins.
- Before that it was a simple pencil and paper game. 
- The aim of the game is to guess the grid location of your opponent's ships, thus hitting and sinking the other player's ships before they sink yours. 
- Each player takes a turn, guessing the grid location where the opponent's ships are located. 
- This continues until all either player’s ships have all been hit. 
- The winner is the player with ships still remaining. 

## Flow chart

![Flow chart](docs/images/work-flow.PNG)


## Reminders

* My code is placed in the `run.py` file
* My dependencies are placed in the `requirements.txt` file using `pip3 freeze` and directing the output or copying to requirements.txt
* remember to `pip3 install gspread google-auth` and  `pip3 install gspread` if import fails initially
* remember to create a Google works sheet and share sheet to a google email address identity
* If not using our Heroku deployed environment, you will need your own creds.json to access your own google spreadsheet.
* Do not edit any of the other files or this code may not deploy properly

## Bugs fixed
* fixed pylint warnings about trailing spaces, space after # in comments
* also fixed pylint error if using space between print command and opening bracket i.e. print ("test") is incorrect - should be print("test") with no space.
* fixed .gitpod.yml problems by adding the following lines to vscode: extensions: section of .gitpod.yml file
    - ms-toolsai.jupyter
    - ms-toolsai.jupyter-keymap
    - ms-toolsai.jupyter-renderers
    
## Creating the Heroku app

To create the app, I have added two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

I have also created a _Config Var_ called `PORT`. Set this to `8000`

I have credentials, such as in the Love Sandwiches project, so have created another _Config Var_ called `CREDS` and pasted the JSON into the value field.

You should connect your GitHub repository and deploy as normal.

## **Deployment**

The site has been deployed through Heroku. 

The site has been developed on GitPod, committed and pushed to GitHub. 

Deployment proccess:

1. Log in [Github](https://github.com/).
    - Open the repo to deploy. 
    - The one for this project is [here](https://github.com/ian-IBCIRL/bat).
2. Log in [Heroku](https://www.heroku.com/).
    - Click in the "New" button in the top right.
    - Select "Create New App"
    - Give a name to the App and choose a region (Europe, for example).
    - Click in "Create App" button.
    - Go to Settings in the nav bar, and select "Add Buildpacks".
    - Add `Python` and save, do the same for `Node.js`, in that order. 
    - `Python` must show first in the list.
    - Go to Deploy in the nav bar. 
    - In Deploment Method, select GitHub/Connect to GitHub.
    - In Connect to GitHub (ideally with MFA), copy the repository name and click in search.
    - Once the route for the repo appears under the search, click in "Connect" button.
    - The deployment can be Manual or Automatic, select the one of your preference. 
    - Automatic has the advantage of updating your deployed site as you push the commit in GitHub.
    - Manual has the advantage of waiting until needed, rather than deploying evert time.
    - Verify that "Branch to deploy" is master/main.
    - Click Deploy.

Steps to use and deploy this repository:

- Access to the repo in GitHub [here](https://github.com/ian-IBCIRL/bat).
- It can be "Fork" following the steps [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo).
- It can be "Clone" following the steps [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository).

### **Features to implement in future**

I'd like to add more storyline, graphics and options for placing ships in user specified locations.
And find a way to make a two player game so the computer moves are not necessary.

## **Technologies Used**
- [Python](https://www.python.org/)
- [GitHub](https://github.com/)
- [GitPod](https://www.gitpod.io/)
- [Heroku](https://www.heroku.com/about)
- [LucidCharts](https://www.lucidchart.com/pages/)

## **Testing**

The site had been tested in Chrome, Firefox and Edge without issue. 

### **Validation**

The usual linter website is not working, but the linter built into the template works fine, so fixes have been made as noted above.
Gitpod's Linter shows no error for run.py file. 


### **Manual Testing**

| Feature | Test Action | Validation for Wrong Input  | Test Outcome |
|:---|        :---| :---|:---|
| Name Input | Type in user's name | Check if empty | Pass |

## Constraints

The deployment terminal is set to 80 columns by 24 rows. 
That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

## Libraries used

In this project, 3 libraries are utilised, as instructed by Code Institute and their python project template

- The random library is imported to generate random numbers for the opponent ship placement coordinates and to generate the computer's next target location.
- The Google gspread library is imported to control the spreadsheet containing the username and passwords and the user's scores.
- The Google google.oauth2.service_account library is imported and the Credentials subsystem is used to authenticate and authorise the code to access the spreadsheet. 


-----
Happy coding!