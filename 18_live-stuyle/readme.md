# K18: Serving Looks
# Topher's Lovers

## Overview:

This project involves refactoring a mimic.html to serve content via a live Flask web server. The resulting web page should displays same content and structure as in the previous assignment, but it will now be dynamically served using Flask.

### Notable Points:

- **Flask Integration**: migrated from a purely static HTML/CSS structure to a Flask-based app. This allows us to serve the webpage dynamically using a Python backend.
  
- **Flask Server**: 
  - The `app.py` file contains the code for running the Flask server. Navigate to terminal and run the command python app.py to open the website.
  
- **Routing**: 
  - The root URL `/` in `app.py` serves the `index.html` file via Flask's `render_template()` method.
