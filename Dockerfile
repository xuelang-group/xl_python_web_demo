ARG PYTHON_VERSION=3.7

FROM registry.xuelangyun.com/shuzhi-amd64/suanpan-python-sdk:${PYTHON_VERSION} as builder

ENV PYPI_MIRROR "https://mirrors.aliyun.com/pypi/simple"

RUN pip config set global.index-url ${PYPI_MIRROR}

RUN pip install --upgrade pip

RUN pip install --no-cache-dir pyarmor

WORKDIR /build

COPY . /build

RUN pip install --no-cache-dir -r requirements.txt

