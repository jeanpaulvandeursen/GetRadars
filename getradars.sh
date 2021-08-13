curl https://api.anwb.nl/v2/incidents/desktop-light\?apikey\=QYUEE3fEcFD7SGMJ6E7QBCMzdQGqRkAi | jq '.roads[].segments[].radars[]? | .road,.HM'
