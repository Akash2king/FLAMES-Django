

# Flames Finder

Flames Finder is a web application that helps you find the flames relationship between two people based on their names. It uses a simple algorithm to calculate and display the relationship type, such as friends, lovers, affection, marriage, enemies, or siblings.

## Features

- Enter two names and discover their relationship type.
- Stylish login page for user authentication.
- Responsive design for a seamless experience on different devices.
- Reset form automatically after submission.
- Modern and clean user interface.

## Getting Started

These instructions will help you set up and run the Flames Finder project on your local machine.

### Prerequisites

- Python (3.6 or later)
- Django (3.0 or later)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Akash2king/FLAMES-Django.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd FLAMES-Django
   ```

3. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Create a superuser (admin account):**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create your admin account.

### Usage

1. **Run the Django development server:**

   ```bash
   python manage.py runserver
   ```

2. **Open your web browser and go to [http://localhost:8000/](http://localhost:8000/) to access the Flames Finder application.**

3. **Log in using the admin credentials you created.**

## Contributing

Contributions are welcome! Please follow the [CONTRIBUTING.md](CONTRIBUTING.md) guidelines.




These steps guide users through the process of setting up the project, including cloning the repository, creating a virtual environment, installing dependencies, and running initial migrations. Make sure to customize the instructions based on your project's specific requirements.
