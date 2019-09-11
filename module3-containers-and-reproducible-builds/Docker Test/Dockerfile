FROM debian

# To make logging/IO reliable in Docker
ENV PYTHONUNBUFFERED=1

# Get dependencies
RUN apt update && \
    apt upgrade -y && \
    apt install python3-pip curl nano -y && \
    pip3 install pandas numpy scikit-learn && \
    pip3 install -i https://test.pypi.org/simple/ lambdata-GwenStacey && \
    python3 -c "import lambdata_GwenStacey; print('Success!')"
