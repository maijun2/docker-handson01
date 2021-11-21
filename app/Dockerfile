From python:3.8-alpine
Label author="maijun2@gmail.com"
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY ./app.py /app.py
COPY ./server_secret.key /server_secret.key
COPY ./cert.crt /cert.crt
ENV PORT 443
CMD ["python","-u", "/app.py"]