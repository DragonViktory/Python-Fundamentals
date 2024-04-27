countries = input().split(", ")
capitals = input().split(", ")
final_result = dict(zip(countries, capitals))
#[('Bulgaria', 'Sofia'), ('Romania', 'Bucharest'), ('Germany', 'Berlin'), ('England', 'London')]#[('Bulgaria', 'Sofia'), ('Romania', 'Bucharest'), ('Germany', 'Berlin'), ('England', 'London')]
#zip raboti i s 3 i t.n promenlivi -> 03.lists_basics_lab i dict
#zip
for country, capital in final_result.items():
    print(f"{country} -> {capital}")
