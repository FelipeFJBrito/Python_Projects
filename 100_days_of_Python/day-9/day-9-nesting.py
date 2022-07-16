
capitals =  {
    "France" : "Paris",
    "Germany": "Berlin",
}

#Nesting a list in a Dictionay
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting a Dictionary in a Dictionay
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits" : 12},
}

#Nesting Dictionary in a list
travel_log = [
    {
    "contry": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits" : 12,
    },
    {
    "contry": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits" : 12,
    },
]