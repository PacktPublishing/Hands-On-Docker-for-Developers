FROM fedora
RUN dnf -y update
RUN dnf install -y httpd
RUN rm /etc/httpd/conf.d/welcome.conf
CMD httpd -DFOREGROUND
