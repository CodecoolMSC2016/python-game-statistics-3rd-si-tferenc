# Export functions
import reports

filename = 'game_stat.txt'

def report(filename):
    savefile.write(str(reports.count_games(filename)))
    savefile.write('\n')
    savefile.write(str(reports.decide(filename, 2000)))
    savefile.write('\n')
    savefile.write(str(reports.get_latest(filename)))
    savefile.write('\n')
    savefile.write(str(reports.count_by_genre(filename, "First-person shooter")))
    savefile.write('\n')
    savefile.write(str(reports.get_line_number_by_title(filename, "The Sims")))
    savefile.write('\n')
    savefile.write(str(reports.sort_abc(filename)))
    savefile.write('\n')
    savefile.write(str(reports.get_genres(filename)))
    savefile.write('\n')
    savefile.write(str(reports.when_was_top_sold_fps(filename)))
    savefile.write('\n')


def export_to_file(file_name):
    savefile = exported
    report(filename)

    savefile.close()


exported = open('reports.txt','w')
savefile = exported
export_to_file(exported)