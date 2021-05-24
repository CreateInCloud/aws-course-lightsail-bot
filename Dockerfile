FROM python:3.8

ENV TG_BOT_KEY=YOUR_TG_BOT_KET

# Python package management and basic dependencies
RUN apt-get -y update && apt-get -y upgrade

COPY ./ ./

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "./main.py"]


