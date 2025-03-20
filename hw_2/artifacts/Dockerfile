FROM delameter/python-texlive:3.10-2022-extra

USER root

WORKDIR /workspace

COPY ./artifacts ./artifacts
COPY ./pa_latex ./pa_latex

WORKDIR /workspace/pa_latex/pa_latex

RUN pip install poetry==1.8.4 && \
    poetry install --no-root

CMD ["poetry", "run", "python", "example.py"]
