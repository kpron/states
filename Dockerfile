FROM alpine
RUN apk add --update python py-pip
COPY packages /src/packages
RUN pip install -r /src/packages
COPY app.py /src
COPY states.py /src
CMD python /src/app.py
