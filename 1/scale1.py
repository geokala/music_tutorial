# This is our first lesson, so play a scale with our right hand

# Create the first bar, in the default 4/4 time
bar1_right = stream.Measure()
# Add each note we want to play in turn to the bar
bar1_right.append(note.Note('c4'))
bar1_right.append(note.Note('d4'))
bar1_right.append(note.Note('e4'))
bar1_right.append(note.Note('f4'))

# Create the second bar
bar2_right = stream.Measure()
# Add each note we want to play in turn to the bar
bar2_right.append(note.Note('g4'))
bar2_right.append(note.Note('a4'))
bar2_right.append(note.Note('b4'))
bar2_right.append(note.Note('c5'))

# You can try putting in the bars to play back down to middle C here.
# Don't forget to add them to the right hand's bars below!

# Add both of these bars to the right hand's part
right_hand = stream.Part()
right_hand.append(bar1_right)
right_hand.append(bar2_right)

# Add the right hand to the score
tune = stream.Score(right_hand)

# Add a title
tune.metadata = metadata.Metadata(
    title='Python TTTGLS: Lesson 1',
    composer='New programmer',
)
