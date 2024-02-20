FROM python:3.12

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install pipenv
RUN pip install --upgrade pip 
RUN pip install pipenv

# Install application dependencies
COPY Pipfile Pipfile.lock /app/
# We use the --system flag so packages are installed into the system python
# and not into a virtualenv. Docker containers don't need virtual environments. 
RUN pipenv install --system --dev

# Copy the application files into the image
COPY . /app/

# Expose port 8000 on the container
EXPOSE 8000

ENTRYPOINT ["sh", "-c", "python manage.py migrate && gunicorn vguard.wsgi"]