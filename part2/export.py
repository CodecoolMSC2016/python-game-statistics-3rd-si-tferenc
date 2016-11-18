# Export functions
import reports

filename = 'game_stat.txt'
title = 'Counter-Strike'

def report(filename):
    savefile.write(str(reports.get_most_played(filename)))
    savefile.write('\n')
    savefile.write(str(reports.sum_sold(filename)))
    savefile.write('\n')
    savefile.write(str(reports.get_selling_avg(filename)))
    savefile.write('\n')
    savefile.write(str(reports.count_longest_title(filename)))
    savefile.write('\n')
    savefile.write(str(reports.get_date_avg(filename)))
    savefile.write('\n')
    savefile.write(str(reports.get_game(filename,title)))
    savefile.write('\n')
    savefile.write(str(reports.count_grouped_by_genre(filename)))

def export_to_file(file_name):
    report(filename)
    savefile.close()


savefile = open('reports.txt','w')
export_to_file(savefile)