From nginx:1.17.5-alpine
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./html/ /usr/share/nginx/html/
CMD ["nginx","-g","daemon off;"]