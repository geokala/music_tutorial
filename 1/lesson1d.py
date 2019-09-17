# In this lesson notes and bars are added to the bars using a for loop

bar_notes = ['c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4', 'c5']

# create a Part that we can add notes into:
my_part = stream.Part()

# have an empty bar for the loop to put notes into
current_bar = stream.Measure()

for idx, note_pitch in enumerate(bar_notes):
    current_bar.append(note.Note(note_pitch))
    if (idx + 1) %4 == 0:
        # four notes have been played, so add this bar to the part
        # and create a new one.
        my_part.append(current_bar)
        current_bar = stream.Measure()
    
    
# Add the part to the score.
tune = stream.Score(my_part)

# Add a title
tune.metadata = metadata.Metadata(
    title='Python TTTGLS: Lesson 1d - big loop',
    composer='New programmer',
)
