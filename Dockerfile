FROM public.ecr.aws/sam/build-python3.12:latest

WORKDIR /workspace
ENV PYTHONPATH=/workspace

RUN pip install --no-cache-dir pytest

COPY . .

CMD ["bash"]
