FROM python:3

WORKDIR /usr/src/app

# Copy requirements and install first (layer caching)
COPY requirements.txt ./
RUN apt-get update && apt-get install -y ca-certificates
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of your app files into the container
COPY . .

EXPOSE 3001

CMD [ "python", "./src/server.py" ]
