FROM python:3.9.5-slim-buster

ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_4
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV FLASK_APP=wsgi.py

RUN apt-get update && \
    apt-get install -y libpq-dev zlib1g-dev build-essential shared-mime-info libaio1 libaio-dev unzip wget --no-install-recommends && \
    wget https://download.oracle.com/otn_software/linux/instantclient/214000/instantclient-sdk-linux.x64-21.4.0.0.0dbru.zip && \
    wget https://download.oracle.com/otn_software/linux/instantclient/214000/instantclient-sqlplus-linux.x64-21.4.0.0.0dbru.zip && \
    wget https://download.oracle.com/otn_software/linux/instantclient/214000/instantclient-basic-linux.x64-21.4.0.0.0dbru.zip && \
    mkdir -p /opt/oracle && \
    cp instantclient-* /opt/oracle/ && \
    cd /opt/oracle/ && \
    unzip instantclient-basic-linux.x64-21.4.0.0.0dbru.zip && \
    unzip instantclient-sdk-linux.x64-21.4.0.0.0dbru.zip && \
    unzip instantclient-sqlplus-linux.x64-21.4.0.0.0dbru.zip && \
    rm -rf /var/lib/apt/lists/* instantclient-basic-linux.x64-21.4.0.0.0dbru.zip instantclient-sdk-linux.x64-21.4.0.0.0dbru.zip instantclient-sqlplus-linux.x64-21.4.0.0.0dbru.zip && \
    apt -y clean && \
    apt -y remove wget unzip && \
    apt -y autoremove && \
    rm -rf /var/cache/apt

WORKDIR /backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY credentials.json .

COPY . .

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000" ]
