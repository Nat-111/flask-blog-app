# Flask Blog

A simple Flask blog application with user registration, login, flash messages, and a clean Bootstrap-based layout.

## Features

- Home and About pages
- User registration form
- Login form
- Flash-based success and error messages
- Responsive Bootstrap layout
- Simple blog post listing

## Tech Stack

- Python
- Flask
- Flask-WTF
- WTForms
- Bootstrap 4

## Project Structure

- `flask_blog.py` - main Flask app
- `forms.py` - form definitions
- `static/` - CSS assets
- `templates/` - HTML templates
- `venv/` - local virtual environment (ignored in Git)

## Setup

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd my_flask_app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   ```

   On Windows:
   ```bash
   .\venv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   python flask_blog.py
   ```

5. Open in browser:
   ```text
   http://127.0.0.1:5000
   ```

## GitHub Repo Recommendation

Project name suggestion:
- `flask-blog-app`

Project description suggestion:
- `A simple Flask blog application with registration, login, and responsive templates.`

## Notes

The following are excluded from Git using `.gitignore`:
- `venv/`
- `__pycache__/`
- `.env`
- `.vscode/`
- OS-generated files

## License

This project is for educational/demo use.
