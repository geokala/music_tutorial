# This is our first lesson, so play a phrase with four notes

# Create the first bar, in the default 4/4 time
bar1 = stream.Measure()
# Add each note we want to play in turn to the bar.
# each takes up 1/4 of a bar by default.
bar1.append(note.Note('c4'))
bar1.append(note.Note('d4'))
bar1.append(note.Note('e4'))
bar1.append(note.Note('f4'))

# You can try putting in the bars to play back down to middle C here.

# Create a bar which will contain the part.
my_part = stream.Part()

# Add the bar to the part.
my_part.append(bar1)

# Add the part to the score.
tune = stream.Score(my_part)

# Add a title
tune.metadata = metadata.Metadata(
    title='Python TTTGLS: Lesson 1a',
    composer='New programmer',
)
