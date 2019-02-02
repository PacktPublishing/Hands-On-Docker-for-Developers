# docker build -t gosstest .
# docker run --name=gosstest -d -p 8080:80 gosstest
# curl http://localhost:8080
# docker inspect gosstest | jq .[].State.Health
# docker exec gosstest sh -c "echo 'olleh' > /var/www/index.html"
# curl http://localhost:8080
# docker inspect gosstest | jq .[].State.Health
FROM busybox
RUN echo "hello" > /var/www/index.html
CMD httpd -fv -h /var/www/
EXPOSE 80

RUN wget -q -O /bin/goss  https://github.com/aelsabbahy/goss/releases/download/v0.3.6/goss-linux-amd64 \
     && chmod +rx /bin/goss
ADD goss.yaml /goss/goss.yaml
HEALTHCHECK --interval=10s \
            --timeout=10s \
            --start-period=5s \
            --retries=3 \
            CMD goss -g /goss/goss.yaml validate
            