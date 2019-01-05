# To build the container image: `docker build -t rainbows-and-unicorns .`
# To run the app: `docker run -ti --rm -p 5000:5000 rainbows-and-unicorns`
# To run the tests: `docker run -ti --rm rainbows-and-unicorns pytest`
FROM python:3.7.2-stretch

RUN apt-get update && \
    apt-get -y install locales

RUN echo "Japan/Tokyo" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i -e 's/# ja_JP.UTF-8 UTF-8/ja_JP.UTF-8 UTF-8/' /etc/locale.gen && \
    echo 'LANG="ja_JP.UTF-8"'>/etc/default/locale && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=ja_JP.UTF-8

RUN pip install Flask pytest

ENV FLASK_APP="rainuni.py" LC_ALL="ja_JP.UTF-8" PYTHONPATH="/src/rainbows-and-unicorns"

COPY rainbows-and-unicorns /src/rainbows-and-unicorns

WORKDIR /src/rainbows-and-unicorns

EXPOSE 5000

CMD flask run --host=0.0.0.0
