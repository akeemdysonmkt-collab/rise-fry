# RISE Tracking System

Django implementation of the Resilience In Service of Excellence (RISE)
tracking system. The current build covers the Phase 1 operational foundation:
member/term records, intake data, values-only house recommendations,
accountability and mentorship records, check-in windows, dues records, events
and attendance, service records, campus affiliations, acknowledgments, roles,
and anonymous concerns.

## Local setup

1. Create a `.env` file with a non-empty `SECRET_KEY` and, for development,
   `DEBUG=True`.
2. Run `\.venv\Scripts\python.exe manage.py migrate`.
3. Run `\.venv\Scripts\python.exe manage.py runserver`.
4. Run the checks with `\.venv\Scripts\python.exe manage.py test`.

## September corrections

See [the fix checklist and setup requirements](docs/backend-fixes.md).
The latest [Website Overview follow-up](docs/website-overview-followup.md)
adds permanent account links and applications that save progress between steps.
Intake requires the approved licensed questions and agreement
versions. Configure SMTP for email verification and two concern recipients before
opening submissions. The source documents and production infrastructure remain
required; this checkout is not ready to collect real member data.

## Safety and scope

- The system does not process payments or store payment details.
- Anonymous concerns intentionally store no member identity, session, network
  address, or timestamp; verified submissions retain only a boolean.
- Member-facing surfaces must not expose engagement scores or tiers.
- Officer dashboards require a staff account until role-scoped authorization is
  wired to the organization’s final role-assignment process.
- Placement confirmation/timeout jobs, rotating-token scans, deployment scheduling,
  office permissions, and the WordPress integration need the current source
  documents and deployment decisions listed in the checklist.
