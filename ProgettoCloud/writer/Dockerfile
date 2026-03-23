FROM python:3.11-slim
RUN pip install redis
COPY writer.py /app/writer.py
CMD ["python", "/app/writer.py"]