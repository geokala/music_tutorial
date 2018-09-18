# This is our first lesson, so play a scale with our right hand

# Let's play the first bar, in the default 4/4 time
bar1_right = stream.Measure()
# Now we need to add the notes to it
for next_note in ('c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4', 'c5'):
    bar1_right.append(note.Note(
        next_note,
        quarterLength=0.5,
        ))

# You can try putting in the bars to play back down to middle C here.
# Try to make them be faster, or slower.
# Don't forget to add them to the right hand's bars below!

# Add both of these bars to the right hand's part
right_hand = stream.Part()
right_hand.append(bar1_right)

# Add the right hand to the score
tune = stream.Score(right_hand)

# Add a title
tune.metadata = metadata.Metadata(
    title='Python TTTGLS: Lesson 2',
    composer='New programmer',
)
