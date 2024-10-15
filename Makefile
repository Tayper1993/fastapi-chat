run:
	uvicorn app.main:app
pre-commit:
	pip install pre-commit && pre-commit run --all-files
