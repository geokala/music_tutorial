# In this lesson, a second bar is added.

# This bar is the same as in lesson 1a
bar1 = stream.Measure()
bar1.append(note.Note('c4'))
bar1.append(note.Note('d4'))
bar1.append(note.Note('e4'))
bar1.append(note.Note('f4'))

# create a bar that will be put as the second into the stream
bar2 = stream.Measure()
bar2.append(note.Note('g4'))
bar2.append(note.Note('a4'))
bar2.append(note.Note('b4'))
bar2.append(note.Note('c5'))

# Create a Part as seen before, and add the first bar
my_part = stream.Part()
my_part.append(bar1)
# now add the second bar:
my_part.append(bar2)

# Add the part to the score.
tune = stream.Score(my_part)

# Add a title
tune.metadata = metadata.Metadata(
    title='Python TTTGLS: Lesson 1b',
    composer='New programmer',
)
