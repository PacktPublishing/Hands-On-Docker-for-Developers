# docker build -t healthtest .
# docker run --name=healthtest -d -p 8080:80 healthtest
# curl http://localhost:8080
# docker inspect healthtest | jq .[].State.Health
# docker exec healthtest sh -c "echo 'olleh' > /var/www/index.html"
# curl http://localhost:8080
# docker inspect healthtest | jq .[].State.Health
FROM busybox
RUN echo "hello" > /var/www/index.html
CMD httpd -fv -h /var/www/
EXPOSE 80
HEALTHCHECK --interval=10s \
            --timeout=10s \
            --start-period=5s \
            --retries=3 \
            CMD [[ $(wget -qO - http://localhost) == "hello" ]]