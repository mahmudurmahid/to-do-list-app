# 📝 To-Do List App

The To-Do List App is a productivity-focused application that allows users to manage daily tasks through three different interfaces: a **command-line interface (CLI)**, a **graphical user interface (GUI)** using FreeSimpleGUI, and a **web-based interface** built with Streamlit.

This project was developed as part of the Python Mega Course, using foundational programming principles, modular file structures, and interactive components. Users can add, edit, complete, and remove tasks in any of the three environments.

[Live Streamlit App](https://mahmudurmahid-to-do-list-app-web-deofrp.streamlit.app/)

---

## 📑 CONTENTS

- [User Experience](#user-experience-ux)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Wireframes](#wireframes)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
- [Features](#features)
  - [General Features](#general-features)
  - [Future Implementations](#future-implementations)
- [Technologies Used](#technologies-used)
  - [Languages](#languages-used)
  - [Libraries](#frameworks-libraries--programs-used)
- [Deployment & Local Development](#deployment--local-development)
  - [Deployment](#deployment)
  - [Local Development](#local-development)
    - [How to Fork](#how-to-fork)
    - [How to Clone](#how-to-clone)
- [Testing](#testing)
- [Credits](#credits)

---

## 🧠 User Experience (UX)

### User Stories

As a user, I want to:

- Add new to-do items easily so I can plan my tasks.
- View all tasks in a clear list format.
- Mark tasks as complete to track my progress.
- Edit existing tasks if I make a mistake or need to update them.
- Use the app in the terminal, GUI, or a browser depending on what’s convenient.

---

## 🎨 Design

### Wireframes

Wireframes were drafted based on standard productivity app layouts for mobile and desktop screens. They include:

- A top section for titles and input fields.
- A middle section showing the list of to-dos.
- A bottom section for controls like edit, complete, and exit.

### Colour Scheme

- **Web version:** Uses Streamlit’s default light theme.
- **GUI version:** Uses the `DarkPurple4` theme for contrast and accessibility.
- **CLI version:** Minimalistic and text-based, using Python’s input/output.

### Typography

- **Web:** Inherits from Streamlit defaults (sans-serif).
- **GUI:** Uses Helvetica font for readability.
- **CLI:** Console output formatting for clarity.

---

## 🛠 Features

### General Features

- Persistent to-do storage via a plain text file (`todos.txt`).
- Modular functions in `functions.py` to separate logic.
- Three modes of interaction:
  - `cli.py`: Command line interface with input prompts.
  - `gui.py`: GUI using FreeSimpleGUI.
  - `web.py`: Streamlit-based interactive web version.
- Each interface supports:
  - Adding new tasks
  - Editing existing tasks
  - Completing (removing) tasks
  - Exiting or clearing state safely

### Future Implementations

- Add user authentication and save todos per user.
- Add due dates, priorities, and categories to tasks.
- Integrate with a database instead of a plain text file.
- Add confirmation dialogs in GUI and web versions.
- Dark/light mode toggle for Streamlit version.

---

## 💻 Technologies Used

### Languages Used

- Python

### Frameworks, Libraries & Programs Used

- **Streamlit** – for building the web interface
- **FreeSimpleGUI** – for desktop GUI
- **Built-in Python modules** – for CLI (e.g. `time`)
- **Git & GitHub** – for version control and deployment
- **VS Code** / Vim – for code editing

---

## 🚀 Deployment & Local Development

### Deployment

The Streamlit web version is deployed on **Streamlit Community Cloud**.

**To deploy your own version:**

1. Push your code to GitHub.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo and select the Python file to run (e.g., `web.py`).
4. Ensure `requirements.txt` is present in the repo.
5. Click **Deploy**.

### Local Development

To run the app locally:

```bash
# CLI version
python cli.py

# GUI version
python gui.py

# Web version
streamlit run web.py
```

#### How to Fork

1. Log in to GitHub.
2. Navigate to the repo: [to-do-list-app](https://github.com/mahmudurmahid/to-do-list-app)
3. Click the **Fork** button (top right).

#### How to Clone

```bash
git clone https://github.com/mahmudurmahid/to-do-list-app.git
cd to-do-list-app
```

---

## ✅ Testing

Manual testing was performed on all interfaces:

### CLI:

- Tested command inputs like `add`, `edit`, `complete`, and `exit`.
- Validated handling of invalid index values.

### GUI:

- Verified button functionality (`Add`, `Edit`, `Complete`, `Exit`).
- Popups used for error handling when no task was selected.

### Web:

- Checked rerun behavior and session state with `st.rerun()`.
- Added, removed, and refreshed todos on different devices and browsers.

All interfaces functioned correctly with valid inputs and gracefully handled invalid ones.

---

## 🧾 Credits

### Code

- Inspired by examples and challenges in the **Python Mega Course**.
- Used official documentation for **Streamlit** and **FreeSimpleGUI** to implement UI features.

### Acknowledgments

- Thanks to the **Python Mega Course** team for their structured and practical learning approach.
- Shoutout to the **Streamlit** and **PySimpleGUI** communities for their helpful documentation and open-source support.
