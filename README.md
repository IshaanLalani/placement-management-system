# Placement Management System

A desktop-based talent acquisition and recruitment workflow application built with **Python** and **Tkinter**, designed to streamline the connection between academic records and corporate opportunities.

---

## 📂 Core Modules

1. **Student Module:** Manages comprehensive candidate profiles, email registries, and cumulative GPA tracking.
2. **Company Module:** Maintains a dedicated registry of partner organizations and industry sectors.
3. **Job Portal Module:** Handles criteria-based job vacancy postings and minimum GPA thresholds.
4. **Algorithmic Matching Portal:** Automatically cross-references candidate credentials with active listings to populate qualified application pathways.

---

## ⚙️ The Selection Algorithm
The system utilizes a strict conditional evaluation to automate recruitment screening:

> **Student CGPA ≥ Job Min CGPA**

Only when this condition is satisfied does the application interface expose the qualified job listing for submission.

---

## 💻 Code Overview & Implementation

The application is encapsulated within a single object-oriented class (`PlacementManagementSystem`) utilizing Python's built-in GUI library (`tkinter`).

### 1. In-Memory Data Structures
State management is handled using standard Python lists containing dictionaries to store records dynamically without requiring an external database setup:
* `self.students`: Stores dictionaries with keys `name`, `email`, and `cgpa`.
* `self.companies`: Stores dictionaries with keys `name` and `industry`.
* `self.jobs`: Stores dictionaries with keys `title`, `company`, and `min_cgpa`.

### 2. Graphical User Interface (GUI) & Layout
* **`ttk.Notebook`**: Creates a tabbed container interface (`Students Profile`, `Partner Companies`, `Job Openings`, and `Eligibility & Matching Portal`) to separate workflow views cleanly.
* **`ttk.Treeview`**: Used across modules to present tabular data sets with scrollbars and structured columns.

### 3. Key Functions
* **`add_student()` / `add_company()` / `add_job()`**: Capture text inputs from entry fields, validate data types (ensuring CGPA is a valid float between `0.0` and `4.0`), append dictionaries to local data structures, update tree view tables, and refresh dynamic selection dropdowns.
* **`filter_eligible_jobs(event)`**: Implements the core matching logic. When a student profile is selected from the dropdown, it iterates through active jobs and checks whether `student_cgpa >= job['min_cgpa']`. Qualified positions are filtered and displayed in real time.
* **`apply_job()`**: Handles final application validation and logs success message boxes.

---

## 🏗️ System Architecture & Workflow

```mermaid
flowchart TD
    subgraph Data Input
        S[Student Profiles<br/>CGPA Tracking] --> M[Core Logic Engine<br/>Python Lists & Dictionaries]
        C[Partner Companies<br/>Industry Registry] --> M
        J[Job Openings<br/>Min CGPA Criteria] --> M
    end

    M --> Alg[Eligibility Matching Algorithm<br/>Student CGPA >= Job Min CGPA]
    Alg --> UI[Tkinter Notebook Dashboard<br/>Real-Time Filtering & Applications]
