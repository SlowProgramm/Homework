FROM tiangolo/uwsgi-nginx-flask:python3.10

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app
RUN chmod ugo+rwx static && \
    chmod ugo+rwx static/css && \
    chmod ugo+rwx static/js && \
    chmod ugo+rwx static/css/bootstrap.min.css && \
    chmod ugo+rwx static/css/bootstrap.min.css.map && \
    chmod ugo+rwx static/js/bootstrap.bundle.min.js && \
    chmod ugo+rwx static/js/product-details.js && \
    chmod ugo+rwx static/js/bootstrap.bundle.min.js.map

