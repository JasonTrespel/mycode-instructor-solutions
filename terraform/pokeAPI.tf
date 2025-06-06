 The following example shows how to issue an HTTP GET request supplying
# an optional request header.
# data "http" "iss" {
#  url = "http://api.open-notify.org/astros.json"      // API to send HTTP GET to

  # Optional request headers
#  request_headers = {
 #   Accept = "application/json"
#  }
#}

data "http" "poke" {
  url = "https://pokeapi.co/api/v2/pokemon/darkrai" # GET to cool mon
  request_headers = {
    Accept = "application/json"
  }
}
