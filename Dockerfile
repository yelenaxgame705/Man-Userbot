# We're using Ubuntu 20.10
FROM koala21/kampangbot:buster
#
# Clone repo and prepare working directory
#
RUN git clone -b alpha https://github.com/mrismanaziz/Man-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://github.com/mrismanaziz/Man-Userbot/raw/alpha/requirements.txt

CMD ["python3","-m","userbot"]
