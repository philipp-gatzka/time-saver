# Milestones

Milestone 0: Foundations and Tooling (Week 1)
- Decide tech stack versions and baseline project structure (layers, modules).
- Set up project skeleton, CI, code style, static analysis, and test framework.
- Configure PostgreSQL locally; add migration tooling and empty baseline schema.
- Basic Vaadin app boot with a health page.
- Definition of Done/branching and release strategy.

Milestone 1: Identity & Access (Weeks 2–3)
- Domain: User/Employee model with roles.
- Persistence: Migrations for users/roles.
- AuthN: Session-based login/logout; password hashing; invite/reset flow (manual).
- AuthZ: Role-based guards in UI navigation and endpoints.
- Admin UI: Minimal user management (create, edit, set/reset password).
- Acceptance: Only authenticated users can access app; role-based visibility enforced.

Milestone 2: Master Data (Customers & Projects) (Week 4)
- Domain: Customer, Project, active flag.
- Persistence: Migrations, repositories.
- Application: CRUD use cases.
- UI: Simple listings and forms; active toggle; inactive hidden in selectors.
- Acceptance: HR can manage customers/projects; Employees see only active projects.

Milestone 3: Time Tracking Basics (Weeks 5–6)
- Domain: TimeEntry with rules scaffolding.
- Persistence: Migrations, repositories.
- Application: Create/update/delete entries; per-employee access.
- UI: Daily entry view and simple list; pick project; optional note.
- Validation v1: 15-minute increments; End > Start; no cross-midnight.
- Acceptance: Employee can CRUD valid entries for their own days.

Milestone 4: Advanced Time Rules & Overlap Checks (Week 7)
- Domain/Application: No overlaps per employee per day; consolidation of validation errors.
- UI: Clear validation messages; prevent save on invalid data.
- Acceptance: Overlapping entries are blocked; all rules enforced consistently.

Milestone 5: Monthly Workflow (Weeks 8–9)
- Domain: MonthState with Open/Submitted/Approved and transitions.
- Persistence: MonthState schema.
- Application: Submit Month (employee), Approve/Reopen (HR), invariants.
- Locking: Entries locked post-submission; unlocked only on reopen.
- UI: Month header/status; actions per role; disabled editing when locked.
- Acceptance: Workflow transitions and locking behavior match scope.

Milestone 6: Access Control Hardening & Navigation (Week 10)
- Route-level guards by role and month state.
- Hide/disable actions and navigation for unauthorized users.
- Session handling hardening; login redirects.
- Acceptance: Users cannot reach or act on disallowed views/actions.

Milestone 7: UX Polish and Non-Functional (Week 11)
- Usability: Simple navigation, empty states, error toasts.
- Performance: N+1 avoidance, indexes for common queries.
- Auditing-lite: Timestamps/actor on MonthState per scope.
- Security pass: Password lifecycle, session config, CSRF, headers.

Milestone 8: Stabilization and Release 1.0.0 (Week 12)
- End-to-end tests for core flows.
- Data migration dry runs; seed minimal data.
- Release notes, deployment runbook, rollback plan.
- 1.0.0 tag and deployment.