
.PHONY: setup run test report

setup:
	pip install -r requirements.txt

run:
	streamlit run app/streamlit_app.py

test:
	pytest -q

report:
	python scripts/run_weekly_report.py
