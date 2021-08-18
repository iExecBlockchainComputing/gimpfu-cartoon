FROM debian:buster-slim

# At the time of writing this, gimp 3 (which supports python 3) has not been released.

# Gimp is not installed by default buster-slim image

RUN apt-get update && apt-get install -y \
	gimp \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

# Python-fu is not installed with the gimp package

RUN apt-get update && apt-get install -y \
	gimp-python \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

# Python-fu is not compatible with python 3

RUN apt-get update && apt-get install -y \
	python2 \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

# Python-fu scripts must be made executable and placed in the plug-ins directory

COPY ./src/python-fu-cartoon.py /usr/lib/gimp/2.0/plug-ins/
RUN chmod +x /usr/lib/gimp/2.0/plug-ins/python-fu-cartoon.py

# The following command will be called inside the docker image by app.py
#RUN gimp -i -b '(python-fu-cartoon RUN-NONINTERACTIVE "n_iterations" "input_folder" "input.png" "output_folder")' -b '(gimp-quit 0)'

COPY ./src /app
ENTRYPOINT ["python", "/app/app.py"]
