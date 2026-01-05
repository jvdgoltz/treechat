FROM node:20

COPY . /app
WORKDIR /app

RUN npm ci
RUN npm run build

ENTRYPOINT [ "npm", "run", "start" ]