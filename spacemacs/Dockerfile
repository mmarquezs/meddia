# docker.exe run --name spacemacs -e DISPLAY="host.docker.internal:0" -v C:\Users\minij\repositoris\meddia\:/mnt/workspace spacemacs/emacs25:develop
# Sets DISPLAY environment to Host, requires an X Server

FROM spacemacs/emacs25:develop

ENV DISPLAY="host.docker.internal:0"
ENV UNAME="spacemacser"
ENV UID="1000"

COPY .spacemacs "${UHOME}/.spacemacs"
COPY private "${UHOME}/.emacs.d/private"

RUN install-deps
RUN apt-get update && apt-get install \
      global python3-jedi python3-flake8 python3-pytest \
      python3-yapf python3-pip
RUN pip3 install autoflake jsonrpc \
      importmagic epc 

VOLUME ["/MNT/WORKSPACE"]

