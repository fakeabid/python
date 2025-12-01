# You are organizing participants for three different workshops in a coding bootcamp: Web Development, Data Science, and UI/UX Design.
# Create a list for each workshop containing the names of 3 participants.
# Combine all three workshop lists into a single nested list called all_participants.
# A new participant joins the Web Development workshop — add their name to that list.
# Insert one more participant at the 2nd position in the Data Science list.
# Remove the last participant from the UI/UX Design list.
# Copy the list of Data Science participants to a new list and clear the original.
# From the Web Development list, display only the first two participants.
# Use list comprehension to create a list of the length of each name in the copied Data Science list.
# Check whether “Asha” is in any of the workshop lists.
# Finally, create a tuple that stores the name of the first participant from each workshop list (use slicing and indexing as needed).

web_dev = ['abid', 'hadi','afnas']
data_sc = ['avin', 'aadil', 'rony']
ui_ux = ['abin', 'abhishek', 'aswin']

all_participants = [web_dev, data_sc, ui_ux]

web_dev.append('ali')
data_sc.insert(1, 'hari')
ui_ux.pop()

data_sc_bkp = list(data_sc)
data_sc.clear()

print(web_dev[:2])

data_sc_name_lengths = [len(x) for x in data_sc_bkp]

all_participants[1] = data_sc_bkp

print('Asha' in all_participants[0] or 'Asha' in all_participants[1] or 'Asha' in all_participants[2])

first_names = tuple([x[0] for x in all_participants])
print(first_names)