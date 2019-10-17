# Or multiple instruments, yes, that too.

right_hand = stream.Part()
right_hand.append(note.Note('c4'))
right_hand.append(note.Note('d4'))
right_hand.append(note.Note('e4'))
right_hand.append(note.Note('f4'))

left_hand = stream.Part()
left_hand.append(note.Note('c5'))
left_hand.append(note.Note('d5'))
left_hand.append(note.Note('e5'))
left_hand.append(note.Note('f5'))

tune = stream.Score()
tune.append(right_hand)
tune.append(left_hand)
