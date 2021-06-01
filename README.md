[![Build Status]()]()

<h1 align="center">
  <a href="" target="_blank"><img src="" alt="Multi Device Mockup"/></a>
</h1>

<div align="center">
<a href="" target="_blank"><img src="assets/images/GxP-Overall-Profile-Light.png" width='400px' height='auto' alt="logo"></a>
</div>


## Table of Contents

- [UX](#ux)
  * [Strategy plane](#strategy-plane)
    + [What are the goals and needs of the site owner?](#what-are-the-goals-and-needs-of-the-site-owner-)
    + [User stories](#user-stories)
  * [Scope plane: How?](#scope-plane--how-)
    + [Existing Features:](#existing-features-)
    + [Features which appear on every page:](#features-which-appear-on-every-page-)
  * [Database Architecture](#database-architecture)
    + [Choice of Database](#choice-of-database)
    + [Data model](#data-model)
      - [Users](#users)
  * [Skeleton plane: Presentation and navigation?](#skeleton-plane--presentation-and-navigation-)
    + [1. Wireframes](#1-wireframes)
  * [Surface plane: Design](#surface-plane--design)
        * [Colours:](#colours-)
        * [Logo:](#logo-)
        * [Fonts:](#fonts-)
        * [Icons:](#icons-)
        * [Images:](#images-)
- [Technologies Used:](#technologies-used-)
    + [IDE:](#ide-)
    + [Languages:](#languages-)
    + [Frameworks & Libraries:](#frameworks---libraries-)
    + [Databases](#databases)
    + [Tools](#tools)
- [Testing](#testing)
- [Deployment](#deployment)
  * [How to run this project locally](#how-to-run-this-project-locally)
    + [Instructions](#instructions)
  * [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
- [Special thanks](#special-thanks)
        * [Disclaimer:](#disclaimer-)

# UX
## Strategy plane


### User stories

#### Company director/site owner
1. As a user, I want to have a new online presence.
2. As a user, I want a website easy to use for my customers.
3. As a user, I want my customers to quickly find jobs available.
4. As as user, I want my customers to be able to contact me via my direct contact details or social media.
5. As a user, I do not want a contact form as I do not want to receive any empty or useless emails.
7. As a user, I want my customers to be able to upload CVs when they are interested in a job.
8. As a user, I want to be able to log in as an admin.
9. As a user, I want to be able to add or remove any jobs from available listing on the website.
10. As a user, I want to be able to download CVs uploaded by my candidates and know which job they are associated with.

#### Companies (upstream client)
1. As a user, I want to quickly find contact details of the recruitment company.
3. As a user, I want to know who is behing the recruitment company.
4. As a user, I want to see my company log showing for a job I am partnering with the site owner.

#### Candidates (downstream client)
1. As a user, I want a website which I can scroll easily and find quick infos.
2. As a user, I want to quickly find available jobs.
3. As a user, I do not want to spend too much time reading the job description.
4. As a user, I want to know the location of the job.
5. As a user, I want to know the job title or industry.
5. As a user, I want to know the type of contract associated with the job.
6. As a user, I want to be able to upload my CV so the recruitment company can see my details quickly.
7. As a user, I want to quickly find contact details of the recruitment company.
8. As a user, I want to know the company associated with the job advertised.
9. As a user, I want to learn about the people behind the recruitment company.

[Back to Top](#table-of-contents) 

## Scope plane: How?

### Existing Features:
### Features which appear on every page:

__Feature 1: Navbar__
- The navbar provides the user a quick way to navigate around the website. 

__Feature 2: Footer__
- 

__Feature 4: Feedback messages__
- Using django messages, sending a warning, success or error message to the user whenever an action is being taken. On logout, I used Sweet Alert to have it styled differently and catch the attention of the user. Also used Sweet Alert to send a message to the user when contactform is submitted.

[Back to Top](#table-of-contents) 

### Features on main section:
__Feature 5: Background image__


__Feature 6: Calls for action__


### Features on about us section:
__Feature 7: Photo and pitch__


__Feature 8: Flipping cards__


### Features on listings section:
__Feature 9: Filters/search__


__Feature 10: Listings__

[Back to Top](#table-of-contents) 

### 2. Features Left to Implement:
* 

[Back to Top](#table-of-contents) 

## Database Architecture
### Choice of Database


### Data model

#### Users


#### Profile


| Name         |  Validation     | Key type   |
|---------------|----------|-------------------|
|        |   |         |


#### Listing


| Name         |  Validation     | Key type   |
|---------------|----------|-------------------|


[Back to Top](#table-of-contents) 
	
## Skeleton plane: Presentation and navigation? 
### 1. Wireframes

I used Balsamiq tool for the wireframes and attached them to the workspace within their own directory at the root level. For the tablet format, I chose to use the horizontal size (1024x780) as this is how most users would use their tablet size to see websites. 

Please find a few wireframes showing the main page, the Our Team, . All the other wireframes can be found [here]()

<div align="center">
    <img src="" alt="" aria-label="" />
</div>

<div align="center">
    <img src="" alt="" aria-label="" />
</div>

<div align="center">
    <img src="" alt="" aria-label="" />
</div>

<div align="center">
    <img src="" alt="" aria-label="" />
</div>

<div align="center">
    <img src="" alt="" aria-label="" />
</div>

<div align="center">
    <img src="" alt="" aria-label="" />
</div>

[Back to Top](#table-of-contents) 

## Surface plane: Design 

Since design and UX are not my biggest qualities, I often spend time deciding on the right elements which will ensure the website being a success for the site owners and the users.

##### Colours:
The client had its own colors already chosen With a primary audience of men and the website main goal in attracting more users, the keywords which helped me to find the colors were reliability, power, excitement, engagement. The colors chosen will complement each other in achieving this, as well as making the website somehow reflecting the origins of the site owners and reviving their pride.

<div align="center">
    <img src="" alt="" aria-label="" />
</div>

- Black: #111820;
- DarkTurquoise: #04bbc9;
- Antique White: #FEEFDD;

* Primary:  <strong>Dark Turquoise</strong> 
* Secondary:  <strong></strong>
* Tertiary:  <strong></strong> This tertiary colour will compliment 

[Back to Top](#table-of-contents) 

##### Logo:
Logo provided by the client.

##### Fonts: 
Importing the fonts directly in my css file with the Import Url option.

__[Lato](http://www.latofonts.com/)__:
Simple, professional and elegant without having any spectacular innovative trait matches perfectly the corporate goal of the website. The semi-rounded details of the letters give Lato a feeling of warmth, while the strong structure provides stability and seriousness. The main idea of Lato is classical which will reassure our users when visiting the website.
It is used as main font for the body.

__[Crimson Text](https://fonts.google.com/specimen/Crimson+Text?preview.text=We%27ll+ship+any+car+parts+you+want!&preview.text_type=custom&sort=popularity&preview.size=24&query=crimson+text)__:
While Lato is representing the corporate and reliable character of the website, Crimson Text is giving that flash of innovation for small parts of the website without overwhelming the user with a different or unknown style. 
It is used for the slogan and any direct messages to the user.

[Back to Top](#table-of-contents) 

# Technologies Used: 

### IDE:
- [GitPod](gitpod.io) - I used __GitPod__ as my IDE for the development of this website.

### Languages:
This project used __HTML__, __CSS__, __Javascript__ and __Python__ as programming languages.

### Frameworks & Libraries:
- [Flask](https://www.djangoproject.com/) as a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [Travis CI](https://travis-ci.org/) for continuous integration.
- [PIP](https://pypi.org/project/pip/) for installing all Python libraries and packages needed in this project.
- [Git](https://git-scm.com/) to track changes in source code during software development and for version control.
- [GitHub](https://github.com/) to store and share all project code remotely.
- [Bootstrap](https://getbootstrap.com/) as a front-end open source toolkit, to handle the responsive grid system.
- [jQuery](https://jquery.com/) to handle DOM traversal and manipulation, event handling, animation, and Ajax.
- [Popper.js](https://popper.js.org/) used by Bootstrap for tooltip and popover positioning engine. 
- [FontAwesome](https://fontawesome.com/) as an icon library.
- [Google Fonts](https://fonts.google.com/) for the website fonts.

### Databases

- [mongoDB]() 

### Tools
- [AutoPrefixer](https://autoprefixer.github.io/) to make sure the css code worked on all browsers.
- [Tiny.jpg](https://tinyjpg.com) to compress logo image of the website to increase the website loading on browser
- [Coolors](https://coolors.co/) to find matching colors for the website
- [Balsamiq](https://balsamiq.cloud) to build the wireframes which I then exported to the IDE
- [Favicon converter](https://favicon.io/favicon-converter/) to convert the logo into a favicon which I was able to insert in the static folder and I tested it to be working
- [Sweetalert2](https://sweetalert2.github.io/)
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) to show content structure, margin and paddings and fix any offset
- [Techsini Multi-Mockup](https://techsini.com/multi-mockup/index.php) to create multi-device photo of README

[Back to Top](#table-of-contents) 

# Media and content used:
- [Photo of hand clicking](https://www.pexels.com/photo/apple-business-computer-connection-392018/) by [Vojtech Okenka](https://www.pexels.com/@vojtech-okenka-127162) from Pexels
- [Photo of person holding black pen](https://www.pexels.com/photo/person-holding-black-pen-1109541/) by [Lex Photography](https://www.pexels.com/@lexovertoom) from Pexels

- [Photo of group of people at desk](https://www.pexels.com/photo/person-in-white-long-sleeve-shirt-using-a-tablet-computer-holding-stylus-3740190/) by [bongkarn thanyakij](https://www.pexels.com/@bongkarn-thanyakij-683719) from Pexels
- [Photo of laptop white table](https://www.pexels.com/photo/person-using-laptop-on-white-table-3987029/) by [Anna Shvets](https://www.pexels.com/@shvetsa) from Pexels Photo by Anna Shvets from Pexels
- [404 and 500 pages](https://www.kapwing.com/404-illustrations)

[Back to Top](#table-of-contents) 

# Testing

I created a separate document for Testing writeup which can be found [here]()

[Back to Top](#table-of-contents) 

# Deployment
I have been using the Integrated development environment (IDE) [GitPod](gitpod.io) to develop this milestone project.

From that point, I could add, commit any update of my code and push it to the remote repository so it could be regularly backed up and accessed by others.

__GitHub__: All versions and branches of the code are stored in github.

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [GitPod](https://gitpod.io/)

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

### Instructions
1. Clone the git repository by downloading it [here]() or typing the following command in your terminal:
`git clone `
2. Once you're in the new project, set virtual environments (You do not have to do this in GitPod) with the following command in your terminal:
`python3 -m .venv venv`
3. Initialize the environment by using the following command:
`.venv\bin\activate`
4. Install all required modules with the command 
```pip3 install -r requirements.txt```
5. In your local IDE create a file called `env.py`.
6. Inside the env.py file, add ...
7. Make sure to add env.py to a .gitignore file so it's not pushed to the repository.

11. The website is now running locally. 

[Back to Top](#table-of-contents) 

# Credits
1. General credits
https://learndjango.com/tutorials/django-search-tutorial for inspiration on queryset and search feature.

[Back to Top](#table-of-contents) 

# Special thanks

[Back to Top](#table-of-contents) 