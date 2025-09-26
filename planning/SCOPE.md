# Scope

- Tenancy/deployment: Single-tenant per company. One company-wide timezone. Simple desktop-first web app.
- Roles:
    - Technical Admin: set up software, invite/manage users (set initial passwords, manual resets).
    - Employee: create/edit time entries; submit month (locks); cannot edit after submission.
    - Human Resources (HR): approve submitted months; reopen months; manage customers and projects.
- Data model (minimal):
    - Employee: firstName, lastName, email, passwordHash, role.
    - Customer: name.
    - Project: name, customer, active (true/false).
    - TimeEntry: employee, day, startTime, endTime, project, note (optional).
    - MonthState: employee, yearMonth, status [Open|Submitted|Approved], timestamps, actor.
- Time entry rules:
    - Granularity: 15-minute increments.
    - Validation: End > Start; no overlaps per employee per day; no cross-midnight entries.
    - Project is mandatory; Note optional.
- Month workflow:
    - Employee clicks “Submit Month” → status becomes Submitted; entries locked for employee.
    - HR can Approve (status Approved) or Reopen (back to Open). Only HR can reopen. No edits by HR unless reopened.
    - Approval prerequisite: must be Submitted by employee.
- Management:
    - HR can create/edit/delete Customers and Projects.
    - Inactive projects hidden from selection but retained in data.
    - Employees can log time to any active project (no per-project assignment).
- Auth:
    - Email/password only.
    - Technical Admin invites users with initial password; manual resets; no “forgot password” flow.
- UI:
    - Simple navigation (no dashboards). Plain listings (no totals, no filters).
- Reporting/exports/auditing:
    - None (no exports, no audit logs, no status history beyond current state).

Open assumptions to confirm later (if needed post-1.0.0):

- Password policy and email delivery for invitations.
- Basic notification emails on submit/approve/reopen are not required.

Would you like me to draft:

- A minimal feature backlog with acceptance criteria, or
- A simple milestone/sprint plan for delivering 1.0.0?