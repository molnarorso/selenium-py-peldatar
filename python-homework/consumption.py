# motorway_consumption = 7
# urban_consumption = 9
# motorway_road = 170
# urban_road = 35
# petrol_price = 350
#
# consumption_one_way = motorway_road / 2 / 100 * motorway_consumption + urban_road / 2 / 100 * urban_consumption
# consumption_both_ways = motorway_road / 100 * motorway_consumption + urban_road / 100 * urban_consumption
# price_both_ways = consumption_both_ways * petrol_price
#
# print(consumption_one_way, "liter")
# print(consumption_both_ways, "liter")
# print(price_both_ways, "forint")

motorway_consumption = int(input("országúti fogyasztás: "))
urban_consumption = int(input("városi fogyasztás: "))
motorway_road = int(input("országúton megteendő út: "))
urban_road = int(input("városban megteendő út: "))
petrol_price = int(input("benzin ára: "))

consumption_one_way = motorway_road / 2 / 100 * motorway_consumption + urban_road / 2 / 100 * urban_consumption
consumption_both_ways = motorway_road / 100 * motorway_consumption + urban_road / 100 * urban_consumption
price_both_ways = consumption_both_ways * petrol_price

print(consumption_one_way, "liter")
print(consumption_both_ways, "liter")
print(price_both_ways, "forint")