import os
import csv

csvpath = os.path.join("/Users/meixi/Desktop/bootcamp/Homework/HW3/python-challenge/PyPoll", "Resources", "election_data.csv")
out_path = os.path.join("/Users/meixi/Desktop/bootcamp/Homework/HW3/python-challenge/PyPoll","analysis","analysis.txt")
total_votes = 0

with open(csvpath) as election_file:
    election_reader = csv.reader(election_file, delimiter = ",")

    header = next(election_reader)
    candidates = []
    Votes = []
    max_vote = 0
    max_candidates = []



    for row in election_reader:
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            Votes.append(1)
        else:
            candidates_index = candidates.index(row[2])
            Votes[candidates_index] += 1

    for i in range(len(Votes)):

        if Votes[i] > max_vote:
            max_vote = Votes[i]
            candidate = candidates[i]
            # overwrite original list with just 1 candidate
            max_candidates = []
            max_candidates.append(candidate)
        elif Votes[i] == max_vote:
            candidate = candidates[i]
            max_candidates.append(candidate)




with open(out_path, 'w') as text_file:



    print("Election Results",file=text_file)
    print("-----------------------",file=text_file)
    print("Total Votes: {}".format(total_votes),file=text_file)
    print("-----------------------",file=text_file)
    print(f"{candidates[0]}: {Votes[0]/total_votes*100:.3f}% ({Votes[0]})",file=text_file)
    print(f"{candidates[1]}: {Votes[1]/total_votes*100:.3f}% ({Votes[1]})",file=text_file)
    print(f"{candidates[2]}: {Votes[2]/total_votes*100:.3f}% ({Votes[2]})",file=text_file)
    print(f"{candidates[3]}: {Votes[3]/total_votes*100:.3f}% ({Votes[3]})",file=text_file)
    print("-----------------------",file=text_file)
    print(f"Winner: {max_candidates}",file=text_file)
    print("-----------------------",file=text_file)

text_file.close()