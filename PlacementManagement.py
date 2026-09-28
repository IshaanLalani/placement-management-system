import tkinter as tk
from tkinter import messagebox, ttk


class PlacementManagementSystem:

  def __init__(self, root):
    self.root = root
    self.root.title("Placement Management System")
    self.root.geometry("800x600")
    self.root.minsize(750, 550)

    # In-memory Data Structures
    self.students = []  # List of dicts: {'name': str, 'cgpa': float, 'email': str}
    self.companies = (
        []
    )  # List of dicts: {'name': str, 'industry': str, 'hr': str}
    self.jobs = (
        []
    )  # List of dicts: {'title': str, 'company': str, 'min_cgpa': float}
    self.applications = (
        []
    )  # List of dicts: {'student': str, 'job': str, 'status': str}

    # Style Configuration (Slate & Mint inspired clean look)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TNotebook.Tab", font=("Segoe UI", 10, "bold"), padding=[12, 8])
    style.configure("TButton", font=("Segoe UI", 10), padding=6)

    # Create Main Notebook (Tabs)
    self.notebook = ttk.Notebook(root)
    self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # Initialize Tabs
    self.setup_students_tab()
    self.setup_companies_tab()
    self.setup_jobs_tab()
    self.setup_portal_tab()

  def setup_students_tab(self):
    frame = ttk.Frame(self.notebook, padding=15)
    self.notebook.add(frame, text="  Students Profile  ")

    # Input Form Frame
    form_frame = ttk.LabelFrame(
        frame, text=" Register New Student ", padding=15
    )
    form_frame.pack(side="left", fill="y", padx=5, pady=5)

    ttk.Label(form_frame, text="Full Name:").anchor = "w"
    form_frame.grid_columnconfigure(0, weight=1)
    ttk.Label(form_frame, text="Full Name:").pack(anchor="w", pady=(0, 2))
    self.s_name_entry = ttk.Entry(form_frame, width=25)
    self.s_name_entry.pack(anchor="w", pady=(0, 10))

    ttk.Label(form_frame, text="Email Address:").pack(anchor="w", pady=(0, 2))
    self.s_email_entry = ttk.Entry(form_frame, width=25)
    self.s_email_entry.pack(anchor="w", pady=(0, 10))

    ttk.Label(form_frame, text="Current CGPA:").pack(anchor="w", pady=(0, 2))
    self.s_cgpa_entry = ttk.Entry(form_frame, width=25)
    self.s_cgpa_entry.pack(anchor="w", pady=(0, 15))

    ttk.Button(
        form_frame, text="Register Student", command=self.add_student
    ).pack(fill="x")

    # Table / Display Frame
    table_frame = ttk.LabelFrame(
        frame, text=" Registered Students Directory ", padding=10
    )
    table_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    self.s_tree = ttk.Treeview(
        table_frame, columns=("Name", "Email", "CGPA"), show="headings"
    )
    self.s_tree.heading("Name", text="Student Name")
    self.s_tree.heading("Email", text="Email")
    self.s_tree.heading("CGPA", text="CGPA")
    self.s_tree.column("Name", width=140)
    self.s_tree.column("Email", width=160)
    self.s_tree.column("CGPA", width=60, anchor="center")

    scrollbar = ttk.Scrollbar(
        table_frame, orient="vertical", command=self.s_tree.yview
    )
    self.s_tree.configure(yscrollcommand=scrollbar.set)

    self.s_tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

  def setup_companies_tab(self):
    frame = ttk.Frame(self.notebook, padding=15)
    self.notebook.add(frame, text="  Partner Companies  ")

    form_frame = ttk.LabelFrame(
        frame, text=" Register Partner Organization ", padding=15
    )
    form_frame.pack(side="left", fill="y", padx=5, pady=5)

    ttk.Label(form_frame, text="Company Name:").pack(anchor="w", pady=(0, 2))
    self.c_name_entry = ttk.Entry(form_frame, width=25)
    self.c_name_entry.pack(anchor="w", pady=(0, 10))

    ttk.Label(form_frame, text="Industry Sector:").pack(anchor="w", pady=(0, 2))
    self.c_ind_entry = ttk.Entry(form_frame, width=25)
    self.c_ind_entry.pack(anchor="w", pady=(0, 15))

    ttk.Button(form_frame, text="Add Company", command=self.add_company).pack(
        fill="x"
    )

    table_frame = ttk.LabelFrame(
        frame, text=" Registered Companies Registry ", padding=10
    )
    table_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    self.c_tree = ttk.Treeview(
        table_frame, columns=("Name", "Industry"), show="headings"
    )
    self.c_tree.heading("Name", text="Company Name")
    self.c_tree.heading("Industry", text="Industry Sector")
    self.c_tree.column("Name", width=180)
    self.c_tree.column("Industry", width=180)

    self.c_tree.pack(side="left", fill="both", expand=True)

  def setup_jobs_tab(self):
    frame = ttk.Frame(self.notebook, padding=15)
    self.notebook.add(frame, text="  Job Openings  ")

    form_frame = ttk.LabelFrame(
        frame, text=" Post Vacancy Criteria ", padding=15
    )
    form_frame.pack(side="left", fill="y", padx=5, pady=5)

    ttk.Label(form_frame, text="Job Title:").pack(anchor="w", pady=(0, 2))
    self.j_title_entry = ttk.Entry(form_frame, width=25)
    self.j_title_entry.pack(anchor="w", pady=(0, 10))

    ttk.Label(form_frame, text="Company Name:").pack(anchor="w", pady=(0, 2))
    self.j_comp_entry = ttk.Entry(form_frame, width=25)
    self.j_comp_entry.pack(anchor="w", pady=(0, 10))

    ttk.Label(form_frame, text="Minimum CGPA Required:").pack(
        anchor="w", pady=(0, 2)
    )
    self.j_cgpa_entry = ttk.Entry(form_frame, width=25)
    self.j_cgpa_entry.pack(anchor="w", pady=(0, 15))

    ttk.Button(form_frame, text="Post Job Opening", command=self.add_job).pack(
        fill="x"
    )

    table_frame = ttk.LabelFrame(
        frame, text=" Active Job Board Vacancies ", padding=10
    )
    table_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    self.j_tree = ttk.Treeview(
        table_frame, columns=("Title", "Company", "MinCGPA"), show="headings"
    )
    self.j_tree.heading("Title", text="Job Role")
    self.j_tree.heading("Company", text="Company")
    self.j_tree.heading("MinCGPA", text="Min CGPA")
    self.j_tree.column("Title", width=150)
    self.j_tree.column("Company", width=140)
    self.j_tree.column("MinCGPA", width=80, anchor="center")

    self.j_tree.pack(side="left", fill="both", expand=True)

  def setup_portal_tab(self):
    frame = ttk.Frame(self.notebook, padding=15)
    self.notebook.add(frame, text="  Eligibility & Matching Portal  ")

    top_frame = ttk.Frame(frame)
    top_frame.pack(fill="x", pady=5)

    ttk.Label(
        top_frame,
        text="Select Student Profile to View Qualified Jobs:",
        font=("Segoe UI", 10, "bold"),
    ).pack(side="left", padx=5)

    self.student_combo = ttk.Combobox(top_frame, state="readonly", width=30)
    self.student_combo.pack(side="left", padx=5)
    self.student_combo.bind("<<ComboboxSelected>>", self.filter_eligible_jobs)

    # Split view for matching jobs and history
    match_frame = ttk.LabelFrame(
        frame,
        text=" Algorithmic Matching (Student CGPA >= Job Min CGPA) ",
        padding=10,
    )
    match_frame.pack(fill="both", expand=True, pady=10)

    self.m_tree = ttk.Treeview(
        match_frame, columns=("Job", "Company", "RequiredCGPA"), show="headings"
    )
    self.m_tree.heading("Job", text="Eligible Job Role")
    self.m_tree.heading("Company", text="Company")
    self.m_tree.heading("RequiredCGPA", text="Min CGPA Required")
    self.m_tree.column("Job", width=220)
    self.m_tree.column("Company", width=180)
    self.m_tree.column("RequiredCGPA", width=120, anchor="center")

    self.m_tree.pack(side="left", fill="both", expand=True)

    btn_frame = ttk.Frame(frame)
    btn_frame.pack(fill="x", pady=5)
    ttk.Button(
        btn_frame,
        text="Apply for Selected Qualified Job",
        command=self.apply_job,
    ).pack(side="right", padx=5)

  # Core Business Logic & Actions
  def add_student(self):
    name = self.s_name_entry.get().strip()
    email = self.s_email_entry.get().strip()
    cgpa_str = self.s_cgpa_entry.get().strip()

    if not name or not email or not cgpa_str:
      messagebox.showerror("Validation Error", "All student fields are required!")
      return

    try:
      cgpa = float(cgpa_str)
      if not (0.0 <= cgpa <= 4.0):
        raise ValueError
    except ValueError:
      messagebox.showerror(
          "Input Error", "CGPA must be a valid decimal number between 0.0 and 4.0."
      )
      return

    self.students.append({"name": name, "email": email, "cgpa": cgpa})
    self.s_tree.insert("", "end", values=(name, email, f"{cgpa:.2f}"))

    # Clear entries & update dropdowns
    self.s_name_entry.delete(0, tk.END)
    self.s_email_entry.delete(0, tk.END)
    self.s_cgpa_entry.delete(0, tk.END)
    self.update_student_dropdown()
    messagebox.showinfo(
        "Success", f"Student profile for {name} registered successfully!"
    )

  def add_company(self):
    name = self.c_name_entry.get().strip()
    industry = self.c_ind_entry.get().strip()

    if not name or not industry:
      messagebox.showerror("Validation Error", "All company fields are required!")
      return

    self.companies.append({"name": name, "industry": industry})
    self.c_tree.insert("", "end", values=(name, industry))

    self.c_name_entry.delete(0, tk.END)
    self.c_ind_entry.delete(0, tk.END)
    messagebox.showinfo("Success", f"Company {name} registered successfully!")

  def add_job(self):
    title = self.j_title_entry.get().strip()
    company = self.j_comp_entry.get().strip()
    cgpa_str = self.j_cgpa_entry.get().strip()

    if not title or not company or not cgpa_str:
      messagebox.showerror("Validation Error", "All job fields are required!")
      return

    try:
      min_cgpa = float(cgpa_str)
    except ValueError:
      messagebox.showerror(
          "Input Error", "Minimum CGPA must be a valid number."
      )
      return

    self.jobs.append(
        {"title": title, "company": company, "min_cgpa": min_cgpa}
    )
    self.j_tree.insert("", "end", values=(title, company, f"{min_cgpa:.2f}"))

    self.j_title_entry.delete(0, tk.END)
    self.j_comp_entry.delete(0, tk.END)
    self.j_cgpa_entry.delete(0, tk.END)
    messagebox.showinfo(
        "Success", f"Job vacancy for {title} posted successfully!"
    )

  def update_student_dropdown(self):
    student_list = [f"{s['name']} (CGPA: {s['cgpa']})" for s in self.students]
    self.student_combo["values"] = student_list

  def filter_eligible_jobs(self, event):
    # Clear current match view
    for row in self.m_tree.get_children():
      self.m_tree.delete(row)

    selected_idx = self.student_combo.current()
    if selected_idx == -1:
      return

    student = self.students[selected_idx]
    student_cgpa = student["cgpa"]

    # Core Eligibility Algorithm: Student CGPA >= Job Min CGPA
    for job in self.jobs:
      if student_cgpa >= job["min_cgpa"]:
        self.m_tree.insert(
            "", "end", values=(job["title"], job["company"], job["min_cgpa"])
        )

  def apply_job(self):
    selected_student_idx = self.student_combo.current()
    selected_job_item = self.m_tree.selection()

    if selected_student_idx == -1:
      messagebox.showwarning(
          "Selection Warning", "Please select a student profile from the top!"
      )
      return
    if not selected_job_item:
      messagebox.showwarning(
          "Selection Warning",
          "Please select a qualified job from the list below to apply!",
      )
      return

    student = self.students[selected_student_idx]
    job_values = self.m_tree.item(selected_job_item[0], "values")

    messagebox.showinfo(
        "Application Success",
        f"Application submitted successfully!\n\nCandidate: {student['name']}\nRole:"
        f" {job_values[0]}\nCompany: {job_values[1]}",
    )


if __name__ == "__main__":
  root = tk.Tk()
  app = PlacementManagementSystem(root)
  root.mainloop()