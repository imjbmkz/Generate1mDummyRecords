FROM python:3.11

WORKDIR /app

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy only specific files or directories
COPY src/ src/

CMD ["python", "src/generate_fake_data.py"]
