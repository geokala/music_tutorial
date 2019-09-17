# requires addition of volume and instrument to import statement. 

# This lesson will look at the volume of MIDI notes. 
# The volume of a MIDI note is controlled by a property known as velocity. 

my_title = "Volume Exercise"
my_name = "Programmer name"
i = instrument.Harp()
# Create the first bar, in the default 4/4 time
bar1_right = stream.Measure()
bar2_right = stream.Measure()

# Defining four notes and setting their velocities:

n1 = note.Note('c4')
n2 = note.Note('c4')
n3 = note.Note('c4')
n4 = note.Note('c4')

n1.volume.velocity = 30
n2.volume.velocity = 60
n3.volume.velocity = 90
n4.volume.velocity = 120

# Adding these to bar1_right and bar2_right
list_n_bar_1 = [n1,n2,n3,n4]
list_n_bar_2 = [n4,n3,n2,n1]

for i_note in list_n_bar_1:
    bar1_right.append(i_note)

for i_note in list_n_bar_2:
    bar2_right.append(i_note)

# Creating a right-hand part from bar1_right and bar2_right:
right_hand = stream.Part()
right_hand.append(i)
right_hand.append(bar1_right)
right_hand.append(bar2_right)

# Creating a left-hand part using only rests:
left_hand = stream.Part()
left_hand.append(i)
left_hand.append(note.Rest(quarterLength=4))
left_hand.append(note.Rest(quarterLength=4))


# Add the left-hand and right-hand parts to the score:
tune = stream.Score()
tune.insert(0,right_hand)
tune.insert(0,left_hand)

# Adding metadata to the tune:
tune.metadata = metadata.Metadata(
    title=my_title,
    composer=my_name,
)
