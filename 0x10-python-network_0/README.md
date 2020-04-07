# 0x10. Python - Red # 0

cURL is a computer software project providing a library and command-line tool for transferring data using various protocols. It’s a command line tool for getting or sending files using URL syntax.


## Some wording/vocabulary


*  URL: “Uniform Resource Locator”, defines the web address to a specific resource. An URL is composed in 4 parts:
*  protocol: http:// or https:// or ftp://… => defines also on which port the server will be requested
*  host: www.example.com or intranet.hbtn.io… => will be resolved by the DNS = hostname to IP address
*  path: /index.html or /states/1/cities… => path from the root of the website or webservice on this host
*  query string: ?name=Jon or ?q=dress&color=FF0000… => always starts by the symbol ? and follow by a list of parameters (key=value) separated by the symbol &
*  request: action of client to send “data” to a specific URL and return a response
*  response: result of a request return from the server to the client
*  HTTP method: or called “verb” for a RestAPI. It’s part of the HTTP protocol only (http and https request):
-  GET: most common method to retreive information from the server (read). When you are surfing in Google or other website, your web browser is doing GET requests to each website to reteive HTML/CSS/JS etc… to render correctly the website. Client can send some information to the server via query string.
-  POST: use to send datas to the server (write) contain in the request body (see below)
- HEAD: same as GET but with an empty response. It’s mainly used to check if a resource is available but without get it.
-  PUT/PATCH: to update a resource with datas contain in the request body
-  DELETE: to remove a resource in the server (mainly used for an RestAPI)
others…
*  Header: an header is a hash of Key-Value information. You can have request header (informations from the client to the server), but also response header (server to client). Headers are really useful and some “Keys-Values” are standardized:
*  User-Agent: from the client to the server for describing the client. Ex: Chrome used as User-Agent: “Mozilla/5.0 (Macintosh; Intel Mac OS X 10116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36”
*  Origin: from the client to the server for giving information of where come from the request to the server
*  Content-Type: define how the body can be read. Ex: “http://swapi.co/api/planets/1/” => “Content-Type: application/json” because the response body is a JSON
*  *  Content-Length: size in Bytes of the request/response body
others
Body: a body is Bytes transmitted in HTTP. You can have request body (parameters from the client to the server) and response body (return result of the server to the client)
*  URL encoding: action to transcode regular string to query string. It’s also used for request body in case of Content-Type: application/x-www-form-urlencoded

## cURL --help
[ cURL man ](https://www.computerhope.com/unix/curl.htm)
