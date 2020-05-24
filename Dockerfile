FROM a772bnsz/maya:2019 AS MAYA

WORKDIR /root/workdir

COPY ./ /root/workdir

ENV PYMEL_SKIP_MEL_INIT=1
ENV PYTHONPATH=/root/workdir/venv/lib/python2.7/site-packages

ENTRYPOINT ["./localentrypoint.sh"]