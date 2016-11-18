# Printing functions
import reports
filename = 'game_stat.txt'
title = 'Counter-Strike'


print(reports.get_most_played(filename))
print(reports.sum_sold(filename))
print(reports.get_selling_avg(filename))
print(reports.count_longest_title(filename))
print(reports.get_date_avg(filename))
print(reports.get_game(filename,title))
print(reports.count_grouped_by_genre(filename))