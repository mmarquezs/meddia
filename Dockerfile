# docker.exe run --name spacemacs -e DISPLAY="host.docker.internal:0" -v C:\Users\minij\repositoris\meddia\:/mnt/workspace spacemacs/emacs25:develop
# Sets DISPLAY environment to Host, requires an X Server

FROM spacemacs/emacs25:develop
ENV DISPLAY="host.docker.internal:0"
VOLUME ["/mnt/workspace"]

