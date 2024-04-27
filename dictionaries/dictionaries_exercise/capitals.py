countries = input().split(", ")
#['Bulgaria', 'Romania', 'Germany', 'England']
capitals = input().split(", ")
#['Sofia', 'Bucharest', 'Berlin', 'London']
final_result = {countries[index]: capitals[index] for index in range(len(countries))}
#{'Bulgaria': 'Sofia', 'Romania': 'Bucharest', 'Germany': 'Berlin', 'England': 'London'}
for country, capital in final_result.items():
    print(f"{country} -> {capital}")
    #Bulgaria -> Sofia
    #Romania -> Bucharest
    #Germany -> Berlin
    #England -> London