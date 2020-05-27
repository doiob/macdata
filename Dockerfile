FROM python
ARG MACAPIKEY
COPY macvendor.py macvendor.py
RUN pip install requests
ENV MACAPIKEY=$MACAPIKEY
ENTRYPOINT [ "python", "./macvendor.py"]
