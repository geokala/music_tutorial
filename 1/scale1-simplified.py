# This is our first lesson, to play a scale

# Create the first set of notes, and add them to the score
notes = stream.Score()

# Add each note we want to play in turn
notes.append(note.Note('c4'))
notes.append(note.Note('d4'))
notes.append(note.Note('e4'))
notes.append(note.Note('f4'))

############################################################################
# Questions...                                                             #
# What happens if you change the numbers in the above code?                #
# Can you add more lines of code to complete the scale?                    #
# Can you find the part of the code that controls the title of the score?  #
# Can you change the title and add your name as the composer?              #
############################################################################

# Add these notes to the score
tune = stream.Score(notes)

# Add a title
tune.metadata = metadata.Metadata(
    title='Python TTTGLS: Lesson 1',
    composer='New programmer',
)
