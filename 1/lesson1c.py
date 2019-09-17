# In this lesson, notes are added to the bars using for loop

bar_1_notes = ['c4', 'd4', 'e4', 'f4']
bar_2_notes = ['g4', 'a4', 'b4', 'c5']

# Create bar1
bar1 = stream.Measure()
# Use a for loop to iterate over the notes and add them to the bar.
for note_pitch in bar_1_notes:
    bar1.append(note.Note(note_pitch))

# Do the same as already seen, but for bar 2.
bar2 = stream.Measure()
for note_pitch in bar_2_notes:
    bar2.append(note.Note(note_pitch))

# Create a Part and add the bars to the part.
my_part = stream.Part()
my_part.append(bar1)
my_part.append(bar2)

# Add the part to the score.
tune = stream.Score(my_part)

# Add a title
tune.metadata = metadata.Metadata(
    title='Python TTTGLS: Lesson 1c - loops',
    composer='New programmer',
)
