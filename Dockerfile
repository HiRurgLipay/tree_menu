FROM python:3.11


ENV PYTHONUNBUFFERED=1


WORKDIR /tmp


COPY ./requirements.txt /app/


RUN pip install poetry


FROM python:3.11


COPY --from=requirements_stage /tmp/requirements.txt /project/requirements.txt


RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y gettext \
  && pip install --no-cache-dir  --upgrade -r /project/requirements.txt

COPY . /project


CMD ["python", "manage.py", "runserver"]
