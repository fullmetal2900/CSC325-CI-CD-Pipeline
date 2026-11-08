# CSC325 CI/CD Pipeline

Django + Django REST Framework classroom backend.

## Run locally

Use Python 3.14 (matching the verified local environment).

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py test --verbosity 2
.\.venv\Scripts\python.exe manage.py runserver
```

- Home page: http://127.0.0.1:8000/
- API: http://127.0.0.1:8000/api/status/
- GET returns application name and status; POST returns 405.
- Three tests cover the home page, API response, and unsupported POST method.

## GitHub Actions

`.github/workflows/csc325_ci_cd.yml` has four sequential jobs:
Setup → Dependencies → Test → Deploy.
`needs: test` prevents deployment until tests succeed. Pull requests run the
first three jobs; pushes to main run all four. Deploy is the assignment's
permitted echo simulation and does not host an application.

## Demonstration

Make the demo change on `feature/api-endpoint-update`, run tests locally,
then record the commit and push. Open a PR, wait for checks, and merge.
Show the resulting main-branch run and Deploy confirmation. Keep the video
under five minutes and narrate it in your own voice.
