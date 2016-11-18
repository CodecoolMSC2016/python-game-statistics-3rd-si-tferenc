# Report functions
import operator
import math

def get_most_played(file_name):
    games_per_sold = []
    with open(file_name) as inputfile:
        for line in inputfile:
            temp = line.strip().split('\t') 
            temp[1] = float(temp[1])
            games_per_sold.append(temp)
            games_per_sold = sorted(games_per_sold, key=operator.itemgetter(1))
        return games_per_sold[-1][0]


def sum_sold(file_name):
    total = []
    with open(file_name) as inputfile:
        for line in inputfile:
            temp = line.strip().split('\t') 
            temp[1] = float(temp[1])
            total.append(temp[1])
            all_games = sum(total)
        return(all_games)
            

def get_selling_avg(file_name):
    total = []
    with open(file_name) as inputfile:
        for line in inputfile:
            temp = line.strip().split('\t') 
            temp[1] = float(temp[1])
            total.append(temp[1])
            all_games = sum(total)
            lenght = len(total)
            avarage = all_games/lenght
        return avarage


def count_longest_title(file_name):
    titles = []
    with open(file_name) as inputfile:
        for line in inputfile:
            temp = line.strip().split('\t')
            titles.append(temp[0])
            lenght = max(titles, key=len)
        return len(lenght)


def get_date_avg(file_name):
    total = []
    with open(file_name) as inputfile:
        for line in inputfile:
            temp = line.strip().split('\t') 
            temp[2] = float(temp[2])
            total.append(temp[2])
            all_games = sum(total)
            lenght = len(total)
            avarage = all_games/lenght
        return(math.ceil(avarage))

def get_game(file_name, title):
     with open(file_name) as inputfile:
        for line in inputfile:
            temp = line.strip().split('\t')
            temp[1]= float(temp[1])
            temp[2] = int(temp[2])
            if title in temp[0]:
                return temp

def count_grouped_by_genre(file_name):
    genre_dict = {}
    with open(file_name) as inputfile:
        for line in inputfile:
            temp = line.strip().split('\t')
            if temp[3] not in genre_dict:
                genre_dict.update({temp[3]: 1})
            elif temp[3] in genre_dict:
                genre_dict[temp[3]] += 1
        return genre_dict
