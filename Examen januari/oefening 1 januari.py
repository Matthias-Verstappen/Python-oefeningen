# r0851784
# Verstappen Matthias
# 1ITF11


def write_to_file(list):
    with open('most_popular_xmas_songs.txt', 'a', encoding='UTF-8') as output:
        output.writelines(list)


all_best_songs = []
write_to_file(["Year;Ranking;Song\n"])
title = "Most popular Christmas songs"
print(title)
print("-"*len(title))

with open('christmas_songs.txt', encoding='utf-8') as file:
    line = file.readline().rstrip()
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        year_ind = record[2]
        highest = int(record[3])
        highest_complete = record
        print(year_ind)
        while line and record[2] == year_ind:
            if int(record[3]) < int(highest):
                highest = record[3]
                highest_complete = record
            line = file.readline().rstrip()
            record = line.split(';')

        print(f'\t{highest}th place with the song {highest_complete[0]} ({highest_complete[1]})')

        output_line = f"{highest_complete[2]};{highest_complete[3]};{highest_complete[0]} ({highest_complete[1]})\n"
        all_best_songs.append(output_line)
write_to_file(all_best_songs)
