FROM a772bnsz/maya:2019 AS MAYA

WORKDIR /root/workdir

COPY ./ /root/workdir

ENV PYMEL_SKIP_MEL_INIT=1

ENTRYPOINT ["./localentrypoint.sh"]