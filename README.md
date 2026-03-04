# Blueprint-Flask-Task

You have to create a simple Flask web application that demonstrates how Blueprints help organize code into modules. The application will consist of three parts:

- **Main page** (no prefix) – blue window.
- **User part** (prefix `/user`) – gray window.
- **Admin part** (prefix `/admin`) – pink window.

---

### Project Structure

```
myapp/
├── app.py                      # Main application file
├── static/                      # Global static files (for main page)
│   └── style.css
├── templates/                   # Global templates
│   └── index.html
├── user/                        # User module
│   ├── __init__.py
│   ├── routes.py                # User module routes
│   ├── static/
│   │   └── style.css            # Styles for user part
│   └── templates/
│       └── user/                 # User module templates
│           ├── index.html        # For /user/
│           └── profile.html      # For /user/profile
└── admin/                       # Admin module
    ├── __init__.py
    ├── routes.py                 # Admin module routes
    ├── static/
    │   └── style.css             # Styles for admin part
    └── templates/
        └── admin/                 # Admin module templates
            ├── index.html         # For /admin/
            ├── profile.html       # For /admin/profile
            └── users.html         # For /admin/users
```

There must be the following URLs:

| URL | Expected Result |
|-----|-----------------|
| `http://127.0.0.1:5000/` | Blue background, text «Hello, human being.» |
| `http://127.0.0.1:5000/user/` | **Blue** background, text «Hello, human being.» |
| `http://127.0.0.1:5000/user/profile` | Gray background, text «Your profile.» |
| `http://127.0.0.1:5000/admin/` | Pink background, text «Hello, admin being.» |
| `http://127.0.0.1:5000/admin/profile` | Pink background, text «Your profile.» |
| `http://127.0.0.1:5000/admin/users` | Pink background, list: John, Carla, Mathew |

---

### Each blueprint must:
1. use its own style.css or global style.css
2. have its own error handler and requsts handler