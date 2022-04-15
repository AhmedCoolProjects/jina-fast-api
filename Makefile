dev:
	uvicorn --port 5000 --host 127.0.0.1 main:app --reload
dev2:
	uvicorn main:app --reload
freeze:
	pip freeze > requirements.txt