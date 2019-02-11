############################
# STEP 1 build executable binary
############################
FROM golang AS builder
WORKDIR $GOPATH/src/httpd-go
COPY . .
# Using go get.
# RUN go get -d -v
# Build the binary.
RUN CGO_ENABLED=0 go build -a -installsuffix cgo -o /go/bin/httpd-go
############################
# STEP 2 build a small image
############################
FROM scratch
# Copy our static executable.
COPY --from=builder /go/bin/httpd-go /go/bin/httpd-go
# Run the hello binary.
ENTRYPOINT ["/go/bin/httpd-go"]