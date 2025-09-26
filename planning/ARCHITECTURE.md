# Architecture

Architectural style
- Monolithic server-side web application
- Layered architecture (UI → Application → Domain → Persistence)
- Single PostgreSQL database

Core modules
- Identity & Access
    - Authentication: session-based login
    - Authorization: role-based (Technical Admin, Employee, HR)
    - Password lifecycle: invite/reset with must-change-password
- Master Data Management
    - Customers and Projects (with active flag)
- Time Tracking
    - Time entries with validation rules (15-minute increments, End > Start, no overlaps, no cross-midnight)
- Monthly Workflow
    - Month state per employee and month (Open, Submitted, Approved; HR can Reopen)
    - Locking behavior tied to state

Layers and responsibilities
- UI (Vaadin)
    - Server-side views for login, time entry, approvals, customer/project management, user management
    - Navigation and access control based on roles and month states
- Application layer
    - Orchestrates use cases: user provisioning, time entry management, month submission/approval/reopen
    - Enforces business rules and transaction boundaries
- Domain layer
    - Core business concepts and rules (employees/users, customers, projects, time entries, month states)
    - Validation and state transitions
- Persistence layer
    - JPA-based repositories for data access
    - PostgreSQL schema managed via migrations