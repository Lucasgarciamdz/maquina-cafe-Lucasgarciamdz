FROM python:3
RUN git clone https://github.com/Lucasgarciamdz/maquina-cafe-Lucasgarciamdz.git
WORKDIR maquina-cafe-Lucasgarciamdz
RUN pip install -r requirements.txt
CMD ["python3","-m", "unittest"]