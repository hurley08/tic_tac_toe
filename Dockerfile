FROM python: latest


COPY . .
RUN pip install tic-tac-toe 




CMD ["python3", "/library/src/play.py"
