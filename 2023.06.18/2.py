waiting_time = 0
the_cost_of_the_trip = 80
added = 6
one_minute_of_waiting = 3

def taxi_cost(meters, time=0) -> int | None:
    if meters == 0:
        return(the_cost_of_the_trip * 2 + time * one_minute_of_waiting)
    if meters > 1:
        return(round((the_cost_of_the_trip + added * meters/150) + time * one_minute_of_waiting))
    else:
        meters < 0
        return(None)

# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))
# None