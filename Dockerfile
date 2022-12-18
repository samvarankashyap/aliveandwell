# pull from quay.io registry
from quay.io/fedora/fedora:36
# Run a dnf update
RUN dnf -y update
# Install python3-pip
RUN dnf -y install python3-pip
# install Flask package using pip
RUN pip install Flask
# create a workdir App
WORKDIR /tmp/
# copy the main.py in current directory 
COPY ./main.py /tmp/main.py
# Run python as entrypoint
ENTRYPOINT [ "python" ]
# run the app main.py
CMD [ "/tmp/main.py" ]
