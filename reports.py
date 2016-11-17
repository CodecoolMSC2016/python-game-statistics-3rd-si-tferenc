# Report functions
import operator


def count_games(file_name):
    results = []
    with open(file_name) as inputfile:
        for line in inputfile:
            results.append(line.strip().split(','))
        
        return len(results)



def decide(file_name, year):
    years = []
    true_or_false = []

    with open(file_name) as inputfile:
        for line in inputfile:
            years.append(line.strip().split('\t'))
        for lines in years:
            if lines[2] == str(year):
                true_or_false.append(True)
            else:
                true_or_false.append(False)
        if True in true_or_false:
            return True
        else:
            return False


def get_latest(file_name):
    names = []
     
    with open(file_name) as inputfile:
        for line in inputfile:
            names.append(line.strip().split('\t'))
        names_sort = sorted(names, key= operator.itemgetter(2))
        return names_sort[-1][0]


def count_by_genre(file_name, genre):
    with open(file_name) as inputfile:
        counter = 0   
        for line in inputfile: 
            temp=line.strip().split('\t')
            if genre == temp[3]:
                counter = counter + 1
        return counter

        
def get_line_number_by_title(file_name, title):
    with open(file_name) as inputfile:
        counter = 1  
        for line in inputfile: 
            temp=line.strip().split('\t')
            if title != temp[0]:
                counter +=1
            elif title == temp[0]:
                return counter
        raise ValueError

def sort_abc(file_name):
    titles = []
    with open(file_name) as inputfile:
        for line in inputfile:
            temp=line.strip().split('\t')
            titles.append(temp[0])
        titles = sorted(titles, key=str.lower)
        return titles



def get_genres(file_name):
    genres = []
    with open(file_name) as inputfile:
        for line in inputfile:
            temp = line.strip().split('\t')
            if temp[3] not in genres:
                genres.append(temp[3])
            else:
                continue
        
        genre_sorted = sorted(genres, key=str.lower)
        return genre_sorted


def when_was_top_sold_fps(file_name):
    fps = []
    with open(file_name) as inputfile:
        for line in inputfile:
            temp = line.strip().split('\t') 
            if temp[3] == "First-person shooter":
                temp[1] = float(temp[1])
                fps.append(temp)
            fps = sorted(fps, key=operator.itemgetter(1))
        return int(fps[-1][2])
    
     




        
            
      


                
        


