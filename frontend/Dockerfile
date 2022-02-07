#build
FROM node:14.19-alpine as build
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY package.json .
RUN npm install
COPY . .
RUN npm run -- ng build --prod


FROM nginx:1.17.1-alpine
EXPOSE 80

COPY --from=build /opt/app/dist/frontend /usr/share/nginx/html
COPY --from=build /opt/app/src/proxy/nginx.conf /etc/nginx/conf.d/default.conf
