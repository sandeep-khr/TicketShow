
# TicketShow
The Ticket Show web app is a platform designed for movie enthusiasts to easily book show tickets. The app provides a seamless user experience, allowing users to explore theaters, discover shows, and make bookings effortlessly. Admin users have the added capability to manage theaters, shows, and user roles. The app also includes scheduled reminders and monthly entertainment reports to enhance user engagement.

# Screenshots
![page1](https://github.com/sandeep-khr/TicketShow/assets/70543525/b0ff3233-ec17-4744-a976-bff20e9de49a)


https://github.com/sandeep-khr/TicketShow/assets/70543525/9df51b81-d18b-44df-9150-f8855edd4bf5


![page2](https://github.com/sandeep-khr/TicketShow/assets/70543525/0afb794e-9b16-43bc-abe6-f1a14d654016)

![page3](https://github.com/sandeep-khr/TicketShow/assets/70543525/4023a1ef-49d8-413a-8f44-6567fa293b45)

![page4](https://github.com/sandeep-khr/TicketShow/assets/70543525/ff9d3d87-7788-469c-8037-6e7602a64988)

# Getting Started
### Prerequisites
To run TicketShow on your local device, you will need to have the following installed:

- Python 3
- Pip
- Node.js

### Installation
#### Frontend

```sh
npm install
```

```sh
npm run dev
```

#### Backend
Create a virtual enviroment
```
virtualenv venv
source venv/bin/activate

```

Install the required packages
```
pip install -r requirements.txt

```
edit .env file and fill all the required details like email, password, omdb api-key etc.

start the redis server
```
redis-server
```
start the celery worker
```
celery -A app.celery worker --loglevel=info
```
```
celery -A app.celery beat --loglevel=info

```
start the app

```
pyhton app.py
```
## Usage
### User Registration and Login
Open your browser and navigate to the app's URL (e.g., http://localhost:5000).
Click on the "Sign Up" link to create a new account.
Fill in the required information, including a unique username and a secure password. Once registered, use the "Login" link to access your account by entering your credentials.

### Browsing Theaters and Shows
After logging in, you'll be directed to the app's home page.
Explore the available theaters and shows displayed on the homepage.
Use search and filter options to discover shows based on location, tags, and ratings.

### Booking Show Tickets
Select a show that interests you. On the show's details page, you can view information such as show name, rating, and ticket price.
Choose the desired quantity of tickets and click the "Book Now" button. After that you'll get redirected to ticekets page where you can view all of your tickets.

### Admin Control (Admin Users Only)
If you're an admin user, log in with your admin credentials.
Admin users have access to additional functionalities, such as theater and show management. Admin can export details about theater and show in csv format to his email.

