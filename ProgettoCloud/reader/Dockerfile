FROM python:3.11-slim
RUN pip install flask redis
COPY reader.py /app/reader.py
EXPOSE 5000
CMD ["python", "/app/reader.py"]