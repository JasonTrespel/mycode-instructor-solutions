 produces an output value named "space_heroes"
# output "space_heroes" {
#  description = "API that documents folks in space"
#  value       = data.http.iss.response_body
# }

# produces legal JSON output value named "space_heroes_json"
# output "space_heroes_json" {
#  description = "API that documents folks in space"
#  value       = jsondecode(data.http.iss.response_body)    // note the jsondecode()
#}

# produces output value from poke request
output "monpoke" {
  description = "API GET from fun API"
  value       = jsondecode(data.http.poke.response_body)
}
