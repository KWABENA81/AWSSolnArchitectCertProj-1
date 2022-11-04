FROM node:14-slim

WORKDIR /user/src/app

COPY ./package.json ./

COPY ./yarn.lock ./

RUN npm install

ENV TZ="America/Toronto"

COPY . .

EXPOSE 3000

CMD ["npm", "start"]