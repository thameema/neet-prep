FROM python:3.11-slim

WORKDIR /app

COPY index.html questions_database.js questions_bank.json neet_server.py NEET_Tamil_Nadu_Mastery_Guide.md ./
COPY scripts ./scripts

ENV PORT=8090
EXPOSE 8090

CMD ["python3", "neet_server.py"]
