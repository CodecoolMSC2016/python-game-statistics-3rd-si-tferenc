# Printing functions
import reports

filename = 'game_stat.txt'
print(reports.count_games(filename))
print(reports.decide(filename, 2000))
print(reports.get_latest(filename))
print(reports.count_by_genre(filename, "First-person shooter"))
print(reports.get_line_number_by_title(filename, "The Sims"))
print(reports.get_genres(filename))
print(reports.when_was_top_sold_fps(filename))
print(reports.sort_abc(filename))